from flask import Blueprint, render_template
from time import sleep

site = Blueprint('site', __name__, template_folder='templates')

@site.route('/')
def index():
    output = [x for x in range(20)]
    return render_template('site/index.html', output = output, change_colour=False)

@site.route('/load')
def load():
    output = [x for x in range(20,40)]
    sleep(3)
    print('waiting ...')
    return render_template('site/index.html', output = output, change_colour=True)
