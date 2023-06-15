from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()


# Įrašyti naują darbuotoją
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(
        first_name=data['first_name'],
        last_name=data['last_name'],
        birth_date=data['birth_date'],
        position=data['position'],
        salary=data['salary'],
        start_date=datetime.now().strftime('%Y-%m-%d')
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Darbuotojas pridėtas'}), 201

# Peržiūrėti visus darbuotojus
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.serialize() for employee in employees])

# Ištrinti darbuotoją pagal ID
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Darbuotojas ištrintas'}), 200
    else:
        return jsonify({'message': 'Darbuotojas nerastas'}), 404

# Atnaujinti darbuotoją pagal ID
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    employee = Employee.query.get(employee_id)
   
# Pagrindinis maršrutas
@app.route('/')
def index():
    return render_template('index.html')

# Flask aplikacijos paleidimas
if __name__ == '__main__':
    app.run(debug=True)
