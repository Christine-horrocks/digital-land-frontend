from flask import (
    Blueprint,
    render_template,
    request,
    json)

frontend = Blueprint('frontend', __name__, template_folder='templates')

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/buttons')
def buttons():
    return render_template('buttons.html')

@frontend.route('/contribution-bars')
def contribution_bars():
    return render_template('contribution-bars.html')

@frontend.route('/hero')
def hero():
    return render_template('hero.html')

@frontend.route('/contents-section')
def contents_section():
    return render_template('contents.html')

@frontend.route('/panels')
def panels():
    return render_template('panels.html')

@frontend.route('/search')
def search():
    return render_template('search.html')

@frontend.route('/task-list')
def task_list():
    return render_template('task-list.html')

@frontend.route('/js/mhclg-maps')
def mhclg_maps():
    return render_template('js-docs/mhclg-maps.html')

@frontend.route('/js/accessible-autocomplete')
def accessible_autocomplete():
    return render_template('js-docs/accessible-autocomplete.html')

# set the assetPath variable for use in 
# jinja templates
@frontend.context_processor
def asset_path_context_processor():
    return {'assetPath': '/static/govuk-frontend/assets'}
