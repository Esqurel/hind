from flask import redirect, render_template, url_for
from flask_login import current_user, logout_user

from hind import app
import hind.models as models


@app.route('/', methods=['GET', 'POST'])
def home():
    dict1 = {'English': 17, 'French': 13, 'German': 11, 'Italian': 9, 'Spanish': 7}
    dict2 = {'John': ['English', '12th century', '13th century', '14th century', 'Withycombe', 'common'],
             'de': ['English', 'French', '12th century', 'R&W', 'common'],
             'Woode': ['English', '12th century', 'R&W']}
    return render_template('_home.html', dict1=dict1, dict2=dict2)


# User routes.
@app.route('/register', methods=['GET', 'POST'])
def user_register():
    return render_template('user_register.html')


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    return render_template('user_login.html')


@app.route('/logout', methods=['GET'])
def user_logout():
    logout_user()
    return render_template('_home.html')


@app.route('/edit_<string:category>', methods=['GET', 'POST'])
@app.route('/edit_<string:category>/<int:page>', methods=['GET', 'POST'])
def edit(category, page=1):
    template = 'edit_{0}.html'.format(category)
    users = [{'name': 'Pelican', 'email': 'pelican@esqurel.com', 'roles': ['Admin'], 'is_active': True},
             {'name': 'Senior', 'email': 'senior@esqurel.com', 'roles': ['Editor'], 'is_active': True},
             {'name': 'Herald', 'email': 'herald@esqurel.com', 'roles': [], 'is_active': False}]
    roles = ['Admin', 'Editor']
    sources = [{'title': 'An Index to the Given Names in the 1292 Census of Paris', 'author': 'Comn Dubh'},
               {'title': 'Yorkshire Given Names from 1379', 'author': 'Talan Gwynek'},
               {'title': 'German Names from Nürnberg, 1497', 'author': 'Aryanhwy merch Catmael'},
               {'title': 'Deutsches Nameslexikon', 'alias': 'Bahlow', 'author': 'Hans Bahlow'},
               {'title': 'Etymologisches Wörterbuch der Deutschen Familiennamen', 'alias': 'Brechenmacher', 'author': 'Josef Karlmann Brechenmacher'},
               {'title': 'The Old Norse Name', 'alias': 'Geirr Bassi', 'author': 'Geirr Bassi Haraldsson'},
               {'title': 'Oxford Dictionary of English Christian Names', 'alias': 'Withycombe', 'author': 'E. G. Withycombe'}]
    return render_template(template, current_page=page, users=users, roles=roles, sources=sources)


@app.route('/<string:category>/<string:name>', methods=['GET', 'POST'])
def information(category, name):
    try:
        pass
    except Exception:
        print(Exception)
    template = 'info_{0}.html'.format(category)
    return render_template(template, item=name)


@app.route('/users/me', methods=['GET', 'POST'])
def my_profile():
    return redirect(url_for('information', category='users', name=current_user.name))