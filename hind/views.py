from flask import render_template
from flask_login import logout_user

from hind import app


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('_home.html')


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

"""
# Edit routes.
@app.route('/edit_elements', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/edit_elements/<int:page>', methods=['GET', 'POST'])
def edit_elements(page):
    return render_template('edit_elements.html', current_page=page)


@app.route('/edit_sources', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/edit_sources/<int:page>', methods=['GET', 'POST'])
def edit_sources(page):
    return render_template('edit_sources.html', current_page=page)


@app.route('/edit_tags', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/edit_tags/<int:page>', methods=['GET', 'POST'])
def edit_tags(page):
    return render_template('edit_tags.html', current_page=page)


@app.route('/edit_users', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/edit_users/<int:page>', methods=['GET', 'POST'])
def edit_users(page):
    return render_template('edit_users.html', current_page=page)
"""

@app.route('/edit_<string:category>', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/edit_<string:category>/<int:page>', methods=['GET', 'POST'])
def edit(category, page):
    template = 'edit_{0}.html'.format(category)
    return render_template(template, current_page=page)

"""
# Information routes.
@app.route('/element/<str:element>', methods=['GET', 'POST'])
def info_element(element):
    return render_template('info_element.html', item=element)


@app.route('/source/<str:source>', methods=['GET', 'POST'])
def info_source(source):
    return render_template('info_source.html', item=source)


@app.route('/tag/<str:tag>', methods=['GET', 'POST'])
def info_tag(tag):
    return render_template('info_tag.html', item=tag)


@app.route('/user/<str:user>', methods=['GET', 'POST'])
def info_user(user):
    return render_template('info_user.html', item=user)
"""

@app.route('/<string:category>/<string:name>', methods=['GET', 'POST'])
def information(category, name):
    template = 'info_{0}.html'.format(category)
    return render_template(template, item=name)