import pyttsx3
import PyPDF2

def text_to_speech(text, gender):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 140)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()

def read_text_from_pdf(fname,s_pgnum, e_pgnum):
    book = open(fname, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    if s_pgnum == 1:
        s_pgnum = 0
    elif s_pgnum > pages:
        s_pgnum = 0
    elif s_pgnum > 1 and s_pgnum < pages:
        s_pgnum = s_pgnum + 1
    else:
        s_pgnum = 0

    if e_pgnum > pages:
        e_pgnum = pages
    elif e_pgnum == s_pgnum:
        e_pgnum = pages
        s_pgnum = s_pgnum - 1

    for num in range(s_pgnum, e_pgnum):
        page = pdfReader.getPage(num)
        text = page.extractText()
        text = text.replace('\n', ' ')
    return text

s_pgnum = 0
e_pgnum = 1
fname = ""
try:
    text = read_text_from_pdf(fname,s_pgnum,e_pgnum)
except FileNotFoundError:
    text =""

gender = 'Male'
text_to_speech(text, gender)
