from flask import Flask 
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .models import db as root_db

from flask_migrate import Migrate

app = Flask(__name__)

# @app.route("/") #simple route on the homepage
# def hello_world():
    # return "<p>Hello, World!</p>"

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)


root_db.init_app(app)
migrate = Migrate(app, root_db)