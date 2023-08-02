from flask import Flask,request
from flask_wtf.csrf import CSRFProtect
import os
import json
from werkzeug.utils import secure_filename


SECRET_KEY = os.urandom(32)

from blueprints_view.index import index_blueprint
from blueprints_view.kredit import kredit_blueprint
from blueprints_view.manual import manual_blueprint
from blueprints_view.auto import auto_blueprint
import os


app = Flask(__name__)
# app.config['SECRET_KEY'] = SECRET_KEY
app.config['SECRET'] = 'secret!123'

app.register_blueprint(index_blueprint)
app.register_blueprint(kredit_blueprint)
app.register_blueprint(manual_blueprint)
app.register_blueprint(auto_blueprint)

# csrf = CSRFProtect(app)
app.run(port='3000',debug=True)