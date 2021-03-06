try:
    from gevent import monkey; monkey.patch_all()
except ImportError:
    pass
import os
from bottle import route, run, CherryPyServer, template, view, error, redirect, get, static_file, post, request, auth_basic, response, hook
from lib import get_date, get_portfolio, get_navigation, get_content, send_email, merge_dicts, password_confirm, register_user

site_name = "jm | Design"
site_author = "James Milne"
site_support = os.environ.get("SUPPORT")
if os.environ.get("PRODUCTION"):
    site_host = "jm-design.herokuapp.com"
else:
    site_host = "192.168.1.2"
site_port = os.environ.get("PORT", 5000)
site_globals = {'site_name':site_name,'site_author':site_author,'site_host':site_host,'site_port':site_port,'day':get_date()[0],'day_no':get_date()[1],'month':get_date()[2],'year':get_date()[3]}

@hook('before_request')
def strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')

@error(404)
@view('templates/error')
def error404(error):
    crash_data = {'requests': request.environ}
    other_dict = {'title':error}
    send_email(site_support, crash_data)
    return merge_dicts(crash_data, other_dict)

@route('/')
@view('templates/page')
def root(title='Home',site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    page_dict = {'title':title,'site_name':site_name,'site_author':site_author,'user':userStatus, 'navigation':navigation}
    return merge_dicts(page_dict, site_globals)

@route('/<title>')
@view('templates/page')
def page(title,site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    nav_exclude = get_navigation()[1]
    if title not in navigation:
        if title not in nav_exclude:
            title='Home'
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    if title == 'Portfolio':
        portfolio = get_portfolio()
        page_dict = {'title':title,'navigation':navigation,'portfolio':portfolio, 'user':userStatus}
    else:
        page_dict = {'title':title,'navigation':navigation,'user':userStatus}
    return merge_dicts(page_dict, site_globals)

@route('/<title>/json')
def return_json(title):
    content = get_content(title)
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title': title, 'content': content, 'date-returned': str(day_no-1)+str(month).upper()+str(year), "userStatus":userStatus}

@get('/Contact')
@view('templates/contact_get')
def get_contact(title='Contact',site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    nav_exclude = get_navigation()[1]
    if title not in navigation:
        if title not in nav_exclude:
            title='Home'
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    page_dict = {'title':title,'navigation':navigation,'user':userStatus}
    return merge_dicts(page_dict, site_globals)

@post('/Contact')
@view('templates/contact_got')
def submit_contact(title='Contact',site_name=site_name,site_author=site_author):
    email = request.forms.get('email')
    message = request.forms.get('message')
    send_email(email, message)
    navigation = get_navigation()[0]
    nav_exclude = get_navigation()[1]
    if title not in navigation:
        if title not in nav_exclude:
            title='Home'
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    page_dict = {'title':title,'navigation':navigation,'user':userStatus}
    return merge_dicts(page_dict, site_globals)

@get('/login')
@auth_basic(password_confirm)
def login():
    response.set_cookie("authID", str(True))
    redirect("/")

@get('/logout')
def logout():
    response.set_cookie("authID", str(False))
    if os.environ['PRODUCTION']:
        redirect("//log:out@" + str(site_host))
    else:
        redirect("//log:out@" + str(site_host) + ":" + str(site_port))

@get('/register')
@auth_basic(password_confirm)
@view('templates/register_users')
def register_get(title='Register User',site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    nav_exclude = get_navigation()[1]
    if title not in navigation:
        if title not in nav_exclude:
            title='Home'
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    page_dict = {'title':title,'navigation':navigation,'user':userStatus}
    return merge_dicts(page_dict, site_globals)

@post('/register')
@auth_basic(password_confirm)
def register_got(title='Register User',site_name=site_name,site_author=site_author):
    email = request.forms.get('email')
    passWord = request.forms.get('pass')
    register_user(email, passWord)

@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='views/assets/img')

if __name__ == '__main__':
    run(debug=True,server='cherrypy', host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
