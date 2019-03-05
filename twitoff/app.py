"""Main application and routing logic for TwitOff."""
from flask import Flask, render_template
from .models import DB, User


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('home.html')

    @app.route('/users')
    def users():
        all_users = User.query.all()
        return render_template('users.html', 
                                all_users=all_users)

    return app