from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '79a351ceff5ba5ff9b6d308345304032'

from app import views

