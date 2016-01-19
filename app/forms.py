from flask.ext.wtf import Form
from wtforms import StringField,BooleanField,SelectField,TextField,SubmitField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo,Regexp

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."),Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])

class ReposForm(Form):
    repo_name=StringField('Repo_Name',validators=[DataRequired("please enter Repository name")])
    repo_address=StringField('Repo_Address',validators=[DataRequired("Please enter full url for Repository")])
    repo_user=StringField('Repo_Address',validators=[DataRequired("Please enter user")])
    repo_passwd=PasswordField('Repo_Passwd',validators=[DataRequired("Please enter password")])
    local_checkout_dir=StringField('local_checkout_dir',validators=[Regexp('^/.*'),DataRequired("Please enter local checkout dir")])
    remote_deploy_url=StringField('Remote_Deploy_Url',validators=[DataRequired("Please enter remote deploy path")])
    repo_type=SelectField('Repo_Type',choices=[('svn','Svn'),('git','Git')])




