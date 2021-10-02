import os
 
class Config:
    
    hostname     = os.environ['HOSTNAME']
    database     = os.environ['DATABASE']
    userDB       = os.environ['USERDB']
    passwordDB   = os.environ['PASSWORD_DB']
    secret       = os.environ['SECRET']
    algorithm    = os.environ['ALGORITHM']
    ROLES        = os.environ['ROLES']
