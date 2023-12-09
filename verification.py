import argparse
import sqlite3
from difflib import  SequenceMatcher
import cv2
from ultralytics import YOLO
from dtrb.dtrb import DTRB


parser = argparse.ArgumentParser()
# parser.add_argument('--image_folder', required=True, help='path to image_folder which contains text images')
parser.add_argument('--workers', type=int, help='number of data loading workers', default = 0)
parser.add_argument('--batch_size', type=int, default=192, help='input batch size')
# parser.add_argument('--saved_model', required=True, help="path to saved_model to evaluation")
""" Data processing """
parser.add_argument('--batch_max_length', type=int, default=25, help='maximum-label-length')
parser.add_argument('--imgH', type=int, default=32, help='the height of the input image')
parser.add_argument('--imgW', type=int, default=100, help='the width of the input image')
parser.add_argument('--rgb', action='store_true', help='use rgb input')
parser.add_argument('--character', type=str, default='0123456789abcdefghijklmnopqrstuvwxyz', help='character label')
parser.add_argument('--sensitive', action='store_true', help='for sensitive character mode')
parser.add_argument('--PAD', action='store_true', help='whether to keep ratio then pad for image resize')
""" Model Architecture """
parser.add_argument('--Transformation', type=str, default="TPS", help='Transformation stage. None|TPS')
parser.add_argument('--FeatureExtraction', type=str, default="ResNet", help='FeatureExtraction stage. VGG|RCNN|ResNet')
parser.add_argument('--SequenceModeling', type=str, default="BiLSTM", help='SequenceModeling stage. None|BiLSTM')
parser.add_argument('--Prediction', type=str, default="Attn", help='Prediction stage. CTC|Attn')
parser.add_argument('--num_fiducial', type=int, default=20, help='number of fiducial points of TPS-STN')
parser.add_argument('--input_channel', type=int, default=1, help='the number of input channel of Feature extractor')
parser.add_argument('--output_channel', type=int, default=512,
                    help='the number of output channel of Feature extractor')
parser.add_argument('--hidden_size', type=int, default=256, help='the size of the LSTM hidden state')
parser.add_argument("--detector_weights", type = str, default="weights/yolov8-detector/license_plate_detection.pt")
parser.add_argument("--recognizer_weights", type = str, default = "weights/dtrb_recognizer/license_plate_recognition.pth")
parser.add_argument("--input_image", type = str, default = "io/input/img.jpg")
parser.add_argument("--threshold", type = float, default= 0.7)
opt = parser.parse_args()


plate_detector = YOLO(opt.detector_weights)
plate_rcognizer = DTRB(opt.recognizer_weights, opt)

image = cv2.imread(opt.input_image)
results = plate_detector.predict(image)

for result in results:
    for i in range(len(result.boxes.xyxy)):
        if result.boxes.conf[i] > opt.threshold:
            bbox = result.boxes.xyxy[i]
            # print(bbox)
            bbox = bbox.cpu().detach().numpy().astype(int)
            plate_image = image[bbox[1]:bbox[3], bbox[0]:bbox[2]].copy()
            # cv2.imwrite(f"io/output/image_result_{i}.jpg", plate_image)
            plate_image = cv2.resize(plate_image, (100, 32))
            plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
            cv2.rectangle(image, (bbox[0], bbox[1]),(bbox[2], bbox[3]),(0, 255, 0), 4)
            preds = plate_rcognizer.predict(plate_image, opt)

connection = sqlite3.connect("LicensePlate.db")
my_cursor = connection.cursor()


for driver in my_cursor.execute("SELECT * FROM drivers"):
    if SequenceMatcher(None, driver[2], preds).ratio() > 0.80:
        print(f"{driver[1]} can enter")
        break
    else:
        print("Not Enter!")    
        
       

# cv2.imwrite("io/input_plates/plate_image_result.jpg", image)







