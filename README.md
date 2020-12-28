# Audio-Book
This project will be helpful in reading the pdfs/image of anything as per the users interest.

It's very simple to use and implement using Flask and Python. If you should have basic knowledge of Flask and Python you can understand the code and customize it by own.
We searched alot for this type of API but got nothing. Then we decided to work on it and finally we have done it.
Now you can give the path of an image and hear the text on it. (Only English Text)

Here is a good reference where we copied the web page style and flask template: [Click here](https://dev.to/siddheshshankar/build-a-text-to-speech-service-with-python-flask-framework-3966)


The above link will help you alot for this API.
I have used the same code but customize it to read the text of given PDF file path.

If you wanna change anything in this, write in comment section or clone it and do some fun on it.
***
## Modules Used
- Flask
- Flask-Cors
- pyttsx3
- PyPDF2
- CV2
- pytesseract (Tesseract to perform OCR (optical character recognition). 

Download 32bit or 64 bit as per the requirement to your system.) [More Details](https://github.com/UB-Mannheim/tesseract/wiki) [Tesseract User Manual](https://tesseract-ocr.github.io/tessdoc/Home.html)
 [Tesseract Repo on GitHub](https://github.com/tesseract-ocr/tesseract)

***
The latest installers (v5.0.0) can be downloaded here:

[tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe) (32 bit) and

[tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe) (64 bit) resp.

***
## How to install the modules?
> Open the cmd terminal and copy-paste the commmand or in PyCharm Create a Project and open the Terminal paste the commands for each modules. [More...](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)

Command to Install Flask [More..](https://pypi.org/project/Flask/)
```
pip install Flask
```
Command to Install Flask-Cors [More...](https://pypi.org/project/Flask-Cors/)
```
pip install Flask-Cors
```
Command to Install Python Text to Speech [More...](https://pypi.org/project/pyttsx3/)
```
pip install pyttsx3
```
Command to Install PyPDF2[More...](https://pypi.org/project/PyPDF2/)
```
pip install PyPDF2
```
Command to Install CV2 [More... ](https://pypi.org/project/opencv-python/) |  [  StackOverFlow](https://stackoverflow.com/questions/57883178/how-to-install-cv2)
```
pip install opencv-python
```
Command to Install pytesseract [More...](https://pypi.org/project/pytesseract/)
```
pip install pytesseract
```
***
## Language Used
- Python
- HTML
- CSS
- JavaScript
***
## How to Download?
Using Git Bash Terminal, copy the below code and paste it in your git terminal. or Create an account on GitHub and [Click here](https://github.com/krishn-kant-raj/Audio-Book/archive/master.zip)
```
git clone git@github.com:krishn-kant-raj/Audio-Book.git
```
***
## What you have to do after cloning/Downloading it in your system? 

1. Open the downloaded directory (AudioBook) in PyCharm
2. Run the app.py and after some second you will get a link like this http://127.0.0.1:8000/
3. Click on the link and then Select the file type (PDF File or Image)
4. Enter or paste file path with proper extension (for Image use .jpg,.png file)
4. Enter page number (Starting and End, both are optional)
5. Select the voice Male or Female (It's optional and default is 'Male' voice) 
6. Select Speech Rate as Normal, Very Slow, Slow, Fast or Very Fast (It's optional and default is 'Normal' speech rate)
7. Finally, click on (Listen Text...) button and here you go.

# Issues
We are working to solve issue for page number. For simple pdf it works fine but have some issues in pdf contain images or contents in tabular form.

If any image contains other than English alpabets, this API will not read that words correctly. 
***
Thanks!

Team Paradox

> **Project Members:**
1. Krishn Kant Raj
2. Intekhab Ahmad

Motihari College of Engineering, Motihari
Computer Science and Engineering
Batch - 2K17
