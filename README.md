# License Plate Recognition and Verification
This project consists of three parts :  
1 - YOLOV8 is used to detect license plates on images  
2 - Deep Text Recognition Benchmark is used to recognize the lincense plates which have been detected in the previous step  
3 - In this step, license plate verification is implemented to know which license plate is stored in the database

## How to Install
```
pip install -r requirements
```

## Usage  
1 - Download the [pretrained weights of YOLOV8](https://drive.google.com/file/d/1-0ZKUUu3ZdMvYVaz-v05mdqi-EyuquJ6/view?usp=drive_link) and put it in weights/yolov8-detector folder  
 2 - Download the [pretrained weights of Text Recognizer](https://drive.google.com/file/d/1--Fmea7nsWD5EAKPM7qL7nO14ecSIyjP/view?usp=sharing) and put it in weights/dtrb_recognizer   
3 - Put your images in io/input folder  
4 - Run the following commands :  
```
python main.py --input_image YOUR_IMAGE.jpg --threshold YOUR_ARGUMENT 
```  
```
python verification.py
```
