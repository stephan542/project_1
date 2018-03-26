from . import db

class UserProfile(db.Model):
    __tablename__ = "user_profiles"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(90))
    location = db.Column(db.String(90))
    bio = db.Column(db.String(1500))
    photo  = db.Column(db.String(100))
    gender = db.Column(db.String(8))
    datte = db.Column(db.String(20))
    
    def __init__(self, first_name, last_name,email,location,bio,photo,gender,datte):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.bio = bio
        self.gender = gender
        self.photo = photo
        self.datte = datte
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def __repr__(self):
        return '<User %r>' %  self.id