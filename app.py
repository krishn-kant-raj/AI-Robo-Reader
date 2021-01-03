# Importing the necessary Libraries
from flask_cors import cross_origin
from flask import Flask, render_template, request
from main import text_to_speech, read_text_from_pdf, image_to_text_reader

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        choice = request.form['choice']
        fname = request.form['speech']
        gender = request.form['voices']
        s_pgnum = request.form['pgnum']
        e_pgnum = request.form['end_pgnum']
        v_rate = request.form['voice_rate']
        if choice == 'Image':
            try:
                text = image_to_text_reader(fname)
            except TypeError:
                text = 'sorry! please enter a valid image path'
            text_to_speech(text, gender, v_rate)
            return render_template('index.html')
        else:
            if s_pgnum == '':
                s_pgnum = 0
            else:
                s_pgnum = int(s_pgnum)

            if e_pgnum == '':
                e_pgnum = 1
            else:
                pass
            if v_rate == '':
                v_rate = 'Normal'

            e_pgnum = int(e_pgnum)

            text = read_text_from_pdf(fname, s_pgnum, e_pgnum)
            print(text)
            text_to_speech(text, gender, v_rate)
            return render_template('index.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)