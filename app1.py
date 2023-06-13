
from flask import Flask, render_template, request, url_for, Response
import pytesseract
import cv2
import time
import schedule
from PIL import Image
import os, werkzeug
from math import floor
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' 

app = Flask(__name__)
    
@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    try:
        imagefile = request.files.get('imagefile', '')
        file = request.files['imagefile'].read()
        img = Image.open(imagefile)
        img1 = img.convert('LA')
        text = pytesseract.image_to_string(img1)
        f = open("sample.txt", "a")
        f.truncate(0)
        f.write(text)
        f.close()
        # usertime = request.form.get("utime")
        return render_template('result.html', var=text)
    except Exception as e:
        print(e) 
        return render_template('index.html')
            
        
if __name__ == "__main__": 
        app.run()


    
    