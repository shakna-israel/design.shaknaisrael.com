try:
    from gevent import monkey; monkey.patch_all()
except ImportError:
    pass
import os
from bottle import route, run, CherryPyServer, template, view, error, redirect, get, static_file, post, request, auth_basic, response
from lib import get_date, get_portfolio, get_navigation, get_content, send_email
import bcrypt

site_name = "jm | Design"
site_author = "James Milne"

@route('/')
@view('templates/page')
def root(title='Home',site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID"):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

@route('/<title>')
@route('/<title>/')
@view('templates/page')
def page(title,site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    nav_exclude = get_navigation()[1]
    if title not in navigation:
        if title not in nav_exclude:
            title='Home'
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID"):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    if title == 'Portfolio':
        portfolio = get_portfolio()
        return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year,'portfolio':portfolio, 'user':userStatus}
    else:
        return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

@route('/<title>/json')
@route('/<title>/json/')
def return_json(title):
    content = get_content(title)
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID"):
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
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID"):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

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
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID"):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

def check_auth():
    cookieHandle = request.get_cookie("authID")
    if cookieHandle is not None:
        retValue = auth_db(cookieHandle)
        return retValue
    else:
        return False

def auth_db(string):
    dataBase = open('auth.db','r')
    authorised = False
    for line in dataBase:
        if string in line:
            authorised = True
    dataBase.close()
    return authorised

def set_cookie(username, password):
    password = password.encode('utf-8')
    hashPass = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
    hashID = bcrypt.hashpw(username, bcrypt.gensalt(rounds=12))
    response.set_cookie("authID", str(hashID)+str(hashPass))

@get('/login')
@view('templates/login')
def login(title='Login',site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID"):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

@post('/login')
def login_post(title='Login',site_name=site_name,site_author=site_author):
    user = request.forms.get('user')
    auth = request.forms.get('auth')
    set_cookie(user, auth)
    if check_auth():
        return {"logged-in":True}
    else:
        return {"logged-in":False}

@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='views/assets/img')

if __name__ == '__main__':
    run(server='cherrypy', host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
