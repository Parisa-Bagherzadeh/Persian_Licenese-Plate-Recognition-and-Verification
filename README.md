# Deep Text Recognition Benchmark  
This is an object oriented implementation of [this repository](https://github.com/clovaai/deep-text-recognition-benchmark.git)  
The pretrained model of the repository is trained on Persian license plates images

## Usage  
1 - Download the pretrained model 
``` !gdown 1-0ZKUUu3ZdMvYVaz-v05mdqi-EyuquJ6 ```  
2 - Put the downloaded model in weights folder  
3 - Put your images in io/input folder  
4 - Run the following command :  
``` python3 main.py \
--Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn \
--image_folder io/input/ \
--saved_model weights/best_accuracy_license_plate_recognition_model.pth
