from app.problems.routes import problems_blueprint
from app.ranking.routes import ranking_blueprint
from app.submissions.routes import submissions_blueprint
from app.users.routes import user_blueprint
from app.utils.config import SECRET_KEY
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.template_folder = "../Frontend/pages"
    app.static_folder = "../Frontend"
    app.secret_key = SECRET_KEY
    CORS(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(problems_blueprint)
    app.register_blueprint(submissions_blueprint)
    app.register_blueprint(ranking_blueprint)

    return app
