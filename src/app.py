from flask import Flask
from flask import render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'empleados'

mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connection
    cursor = conn.cursor()

    sql = "SELECT * FROM empleados;"
    cursor.execute(sql)

    empleados = cursor.fetchall() # OJO, esto no lo toma como a el, supuestamente es un metodo del flaskext

    conn.commit()

    return render_template('empleados/index.html', empleados=empleados)

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=["POST"])
def store():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']

    sql = "INSERT INTO empleados (nombre, correo, foto) values (%s, %s, %s);"
    datos = (_nombre, _correo, _foto.filename)

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)

    conn.commit()

    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)
    