# Audio-Book
This project will be helpful in reading the pdfs/iamge of anything as per the users interest.

It's very simple to use and impliment using Flask and Python. If you should have basic knowledge of Flask and Python you can understand the code and costomize it by own.
We searched alot for this type of api but got nothing. Then we decided to work on it and finally we have done it.


Here is a good reference where we copied the web page style and flask template: [Click here](https://dev.to/siddheshshankar/build-a-text-to-speech-service-with-python-flask-framework-3966)

The above link will help you alot for this API.
I have used the same code but customize it to read the text of given PDF file path.

If you wanna change anything in this, write in comment section or clone it and do some fun on it.

## Modules Used
- Flask
- pyttsx3
- PyPDF2
- CV2
- pytesseract

## Language Used
- Python
- HTML
- CSS
- JavaScript

## How to Download?
Using Git Bash Terminal, copy the below code and paste it in your git terminal.
```
git clone git@github.com:krishn-kant-raj/Audio-Book.git
```

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
***
Thanks!

Team Paradox

> **Project Members:**
1. Krishn Kant Raj
2. Intekhab Ahmad

Motihari College of Engineering, Motihari
Computer Science and Engineering
Batch - 2K17
