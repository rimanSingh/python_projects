from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/userlogin_credential'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    password=db.Column(db.String(30))

    def __init__(self, email, password):
        self.email = email
        self.password = password

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        password = request.form['password_name']
        print(email, password)
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data=Data(email, password)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template("index.html", text="Email already exists")

if __name__ == '__main__':
    app.debug=True
    app.run()