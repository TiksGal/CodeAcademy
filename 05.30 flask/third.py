from flask import Flask
app = Flask(__name__)

@app.route('/keliamieji')
def leap_years():
    leap_years = [year for year in range(1900, 2101) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
    return 'Keliamieji metai: ' + ', '.join(map(str, leap_years))

if __name__ == '__main__':
    app.run(debug=True)
