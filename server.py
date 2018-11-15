from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
Bootstrap(app)

#Configure db
db = yaml.load (open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #return 'Successfully registered!'
        return request.form['password']
    cur = mysql.connection.cursor()
    #cur.execute("INSERT INTO user VALUES(%s)", ['Vinay'])
    #mysql.connection.commit()
    result_value = cur.execute("SELECT * FROM user")
    if result_value > 0:
       users = cur.fetchall()
       print (type(users[0]))
       return str(users[0])
    return render_template('index.html')

@app.route('/about')
def about():
    fruits= ['Apple', 'Banana']
    cur = mysql.connection.cursor()
    if cur.execute("INSERT INTO user(user_name) VALUES('Ben')"):
      mysql.connection.commit()
      return 'success', 201
    return render_template('about.html', fruits=fruits)
@app.route('/css')
def css():
    return render_template('css.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'This page is not found'


if __name__ == '__main__':
    app.run(debug=True, port=5001)


