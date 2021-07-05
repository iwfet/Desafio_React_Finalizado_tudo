from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salario.db'
app.config['SECRET_KEY'] = 'salario'
db = SQLAlchemy(app)
CORS(app)

from API.Admin import rotas