from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html")

@app.route("/calc")
def calculation():
    return render_template("calculations.html")

@app.route("/name")
def home():
    names = ['Jonas', 'Antanas', 'Petras']
    return render_template("name.html", my_list=names)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
