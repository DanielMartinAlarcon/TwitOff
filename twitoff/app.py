"""Main application and routing logic for TwitOff."""
from flask import Flask, render_template, request
from .models import DB, User


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', 
                title='Home', users=users)

    @app.route('/users')
    def users():
        all_users = User.query.all()
        return render_template('users.html', 
                                all_users=all_users)

    return app