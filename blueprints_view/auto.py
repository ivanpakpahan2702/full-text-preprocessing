from flask import Blueprint, render_template

auto_blueprint = Blueprint('auto', __name__)

@auto_blueprint.route("/auto")
def auto():
    return render_template('auto.html', title="Data Mining 2023 || Auto")