import cv2
from ultralytics import YOLO
from dtrb import DTRB


image = cv2.imread("io/input/")
plate_detector = YOLO("weights/")
result = plate_detector.predict(image)
result = result[0]

for i in range(len(result.boxes.xyxy)):
    if result.boxes.conf[i] > 0.8:
        bbox = result.boxes.xyxy[i]
        print(bbox)
        bbox = bbox.cpu().detach().numpy().astype(int)
        plate_image = image[bbox[1]:bbox[3], bbox[0]:bbox[2]].copy()
        plate_image = cv2.resize(plate_image, (32, 100))
        plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(image, (bbox[0], bbox[1]),(bbox[2], bbox[3]),(0, 255, 0), 4)
        
        plate_rcognizer.predict(plate_image)  


cv2.imwrite("io/output/image_result.jpg", image)
cv2.imwrite("io/output/plate_image_result.jpg", plate_image)

plate_rcognizer = DTRB("weiths/best_accuracy_license_plate_recognition_model.pth")





