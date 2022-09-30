from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("WebAPI")


@app.route("/englishToFrench")
def englishToFrench():
    texttotranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(texttotranslate)
    return translated_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    texttotranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(texttotranslate)
    return translated_text


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)