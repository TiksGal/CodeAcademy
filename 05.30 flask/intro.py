# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<h1>Čia mano naujas puslapis</h1>"

# @app.route("/kitas")
# def next():
#     return "<h2>Čia mano kitas puslapis</h2>"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def user(name):
    return f"Labas, {name}"

if __name__ == "__main__":
    app.run(debug=True)