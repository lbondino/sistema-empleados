from flask import Flask
from flask import render_template
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

    sql = "insert into empleados (nombre, correo, foto) values ('Juan', 'juan@email.com', 'fotodejuan.jpg');"
    cursor.execute(sql)

    conn.commit()

    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug=True)
    