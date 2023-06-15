from flask import Flask
app = Flask(__name__)

@app.route('/<word>/<int:repeat>')
def repeat_word(word, repeat):
    return '<br>'.join([word for _ in range(repeat)])

if __name__ == '__main__':
    app.run(debug=True)


