from app import db

class Patient(db.Model):
    __tablename__ = 'patients'
    lastName = db.Column(db.String(64), index=True, unique=True)
    firstName = db.Column(db.String(120), index=True, unique=True)
    Birthdate = db.Column(db.String(128), index=True, unique =True)
    patientID = db.Column(db.integer(100), index=True, unique=True)
    patientnotes = db.Column(db.String(400), index=True, unique=True)
    
class Patientfiles(db.Model):
    __tablename__ = 'patientfiles'
    patientID = db.Column(db.integer(100), index=True, unique=True)
    patientfile = db.Column(db.LargeBinary, index=True, unique=True)

    def __repr__(self):
        return '<Patient {}>'.format(self.lastName, self.firstName)    