#class empleado
from Database import db
from datetime import datetime
class Employee(db.Model):
    __tablename__="employee"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=True)
    email=db.Column(db.String(200),unique=True,nullable=True)
    phone=db.column(db.String(100),nillable=True)
    birthday=db.Column(db.String(20),nullable=True)


    def __init__(self,name,email,phone,birthday):
        self.name=name
        self.email=email
        self.phone=phone
        self.birthday=datetime.strptime(birthday,"%Y-%m-%d").date()
    

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "phone":self.phone,
            "birthday":self.birthday
        }
        