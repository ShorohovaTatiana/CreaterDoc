from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

DATABASE_CONNECTION = "postgresql://postgres:Tatisha2001@localhost/tanyaDiplom"

engine = create_engine(DATABASE_CONNECTION)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_PRE_PING'] = True
db = SQLAlchemy(app=app)






