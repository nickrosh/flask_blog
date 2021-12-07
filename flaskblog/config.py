

class Config:
    SECRET_KEY = '56ee563ebf03882044dd258d8cb54cc6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '' #put yor email server credentials here
    MAIL_PASSWORD = ''