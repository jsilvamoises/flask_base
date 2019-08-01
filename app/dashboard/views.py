from flask import render_template
from . import views

@views.route('/dashboard/franquias')
def franquias_dash():
    return render_template('dashboards/franquias_dashboard.html')