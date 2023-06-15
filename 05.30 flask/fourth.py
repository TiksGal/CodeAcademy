from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/patikrinti', methods=['POST'])
def check():
    year = int(request.form['metai'])
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Metai yra keliamieji."
    else:
        return "Metai nėra keliamieji."

if __name__ == '__main__':
    app.run(debug=True)
