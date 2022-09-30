from flask import Flask , render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
class Period(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subj_1 = db.Column(db.String(30))
    subj_2 = db.Column(db.String(30))
    subj_3 = db.Column(db.String(30))
    subj_4 = db.Column(db.String(30))
    subj_5 = db.Column(db.String(30))
    subj_6 = db.Column(db.String(30))    

with app.app_context():
    db.create_all()
@app.route('/', methods=['GET' ,'POST'])
def sub():
    if request.methods == 'POST':
        
        sube_1 = request.form.get('sub_1') 
        sube_2 = request.form.get('sub_2') 
        sube_3 = request.form.get('sub_3') 
        sube_4 = request.form.get('sub_4') 
        sube_5 = request.form.get('sub_5') 
        sube_6 = request.form.get('sub_6') 
        subject = Subject(subj_1=sube_1, subj_2=sube_2 ,subj_3=sube_3 ,subj_4=sube_4, subj_5=sube_5, subj_6=sube_6)
        db.session.add(subject)
        db.session.commit()
        return redirect('/')

  
if request.method == 'GET':
    subject = Subject.query.all()
    context = {
            'students': subject
        }
        return render_template('hello.html',**context)

   
 
    