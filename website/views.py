from flask import Blueprint, render_template
from flask_login import current_user
from sqlalchemy.sql.functions import user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/games', methods=['GET'])
def games():
    return render_template('game.html')

@views.route('/webscraper', methods=['GET'])
def webscraper():
    return render_template('webscraper.html')

@views.route('/gui', methods=['GET'])
def gui():
    return render_template('gui.html')

@views.route('/schoolProjects', methods=['GET'])
def other_projects():
    return render_template('schoolProjects.html')
