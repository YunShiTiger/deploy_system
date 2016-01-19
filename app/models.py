#coding=utf-8
from werkzeug import generate_password_hash,check_password_hash
from app import app,db 


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique=True)
    passwdhash = db.Column(db.String(54))

    def __init__(self,email,password):
        self.email = email.lower()
        self.set_password(password)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(str(self.uid))
    def set_password(self, password):
        self.passwdhash = generate_password_hash(password)             
    def check_password(self, password):
        return check_password_hash(self.passwdhash, password)


''' 
添加版本库表结构
'''
class RepoInfo(db.Model):
    __tablename__='repos_info'
    uid=db.Column(db.Integer,primary_key=True)
    repo_name=db.Column(db.String(120),unique=True)
    repo_address=db.Column(db.String(120))
    repo_user=db.Column(db.String(50))
    repo_passwd=db.Column(db.String(50))
    local_checkout_path=db.Column(db.String(50))
    repo_type=db.Column(db.String(50))
    remote_deploy_path=db.Column(db.String(50))
    def __init__(self,repo_name,repo_address,repo_user,repo_passwd,local_checkout_path,repo_type,remote_deploy_path):
        self.repo_name=repo_name
        self.repo_address=repo_address
        self.repo_user=repo_user
        self.local_checkout_path=local_checkout_path
        self.repo_type=repo_type
        self.repo_passwd=repo_passwd
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(str(self.uid))


