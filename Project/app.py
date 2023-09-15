from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['target_language']

        try:
            translator = Translator(to_lang=target_language)
            translation = translator.translate(text)
            return render_template('index.html', text=text, translation=translation)
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
