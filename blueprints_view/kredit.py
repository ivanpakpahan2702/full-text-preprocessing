from flask import Blueprint, render_template

kredit_blueprint = Blueprint('kredit', __name__)

@kredit_blueprint.route("/kredit")
def kredit():
    return render_template('kredit.html', title="Data Mining 2023 || Kredit")