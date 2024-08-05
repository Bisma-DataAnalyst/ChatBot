from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'mssql+pyodbc:///?odbc_connect=' + \
                                         r'DRIVER={SQL Server};' + \
                                         r'SERVER=BISMA-CHANDA\SQLEXPRESS;' + \
                                         r'DATABASE=DatabaseForProject;' + \
                                         r'Trusted_Connection=Yes;'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template('index.html')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    assigned_code = db.Column(db.String(20))

    def __repr__(self):
        return f"<User {self.student_name}>"

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Admin {self.admin_name}>"
