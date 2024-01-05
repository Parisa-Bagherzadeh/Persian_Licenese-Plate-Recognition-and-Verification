# License Plate Detection, Recognition and Verification
This project consists of three parts :  
1 - YOLOV8 is used to detect license plates on images  
2 - Deep Text Recognition Benchmark is used to recognize the lincense plates which have been detected in the previous step  
3 - In this step, license plate verification is implemented to know which license plate is stored in the database

## How to Install
```
pip install -r requirements
```

## Usage  
1 - git clone ```https://github.com/Parisa-Bagherzadeh/Persian_Licenese-Plate-Recognition-and-Verification.git```  
2 - Download the [pretrained weights of YOLOV8](https://drive.google.com/file/d/10nf2bbfsfFf24WMTK9XbrL1VojWsRac1/view?usp=sharing) and put it in weights/yolov8-detector folder  
3 - Download the [pretrained weights of Text Recognizer](https://drive.google.com/file/d/1--Fmea7nsWD5EAKPM7qL7nO14ecSIyjP/view?usp=sharing) and put it in weights/dtrb_recognizer   
4 - Put your images in io/input folder  
5 - Run the following commands :  
```
python main.py --input_image YOUR_IMAGE.jpg --threshold YOUR_ARGUMENT 
```  
```
python verification.py
```

### Result
<table>
  <tr>
    <th colspan="2">License Plate Detection</th>
  </tr>
  <tr>
    <td colspan="2"><img src="io\input_plates\plate_image_result.jpg" alt="License Plate Image"></td>
  </tr>
  <tr>
    <td><b>License Plate Recognition</b></td>
    <td><b>License Plate Recognition</b></td>
  </tr>  
  <tr>
    <td><img src="io\output\image_result_0.jpg" alt="Recognition Result 0"></td>
    <td><img src="io\output\image_result_1.jpg" alt="Recognition Result 1"></td>
  </tr>
  <tr>
    <th colspan="2">Drivers Table</th>
  </tr>
  <tr>
    <td colspan="2"><img src="verification_result\table.png" alt="Verification Table"></td>
  </tr>
  <tr>
    <th colspan="2">Verification Result</th>
  </tr>
  <tr>
    <td colspan="2"><img src="verification_result\verification_output.png" alt="Verification Result"></td>
  </tr>
</table>
