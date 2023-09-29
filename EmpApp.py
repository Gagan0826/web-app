from flask import Flask, render_template, request
from pymysql import connections
from config import *
app = Flask(__name__)


db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)
table = 'employee'

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')

@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')

@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location))
        db_conn.commit()
        emp_name = f"{first_name} {last_name}"
    finally:
        cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name)

@app.route("/fetchemp", methods=['POST'])
def FetchEmp():
    fetch_emp_id = request.form['fetch_emp_id']

    select_sql = "SELECT * FROM employee WHERE emp_id = %s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(select_sql, (fetch_emp_id,))
        fetched_employee = cursor.fetchone()
        if fetched_employee:
            emp_id, first_name, last_name, pri_skill, location = fetched_employee
            emp_name = f"{first_name} {last_name}"
            return render_template('FetchEmpOutput.html', emp_id=emp_id, name=emp_name, pri_skill=pri_skill, location=location)
        else:
            return "Employee not found"
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

