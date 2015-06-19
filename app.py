try:
    from gevent import monkey; monkey.patch_all()
except ImportError:
    pass
import os
from bottle import route, run, CherryPyServer, template, view, error, redirect, get, static_file, post, request, auth_basic, response, hook
from lib import get_date, get_portfolio, get_navigation, get_content, send_email
import bcrypt
import pickle

site_name = "jm | Design"
site_author = "James Milne"
site_support = "fake@email.address"

@hook('before_request')
def strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')

@error(404)
@view('templates/error')
def error404(title='404',site_name=site_name,site_author=site_author):
    crash_data = {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus, 'requests': request.environ}
    send_email(site_support, crash_data)
    return crash_data

@route('/')
@view('templates/page')
def root(title='Home',site_name=site_name,site_author=site_author):
    navigation = get_navigation()[0]
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

@route('/<title>')
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
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    if title == 'Portfolio':
        portfolio = get_portfolio()
        return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year,'portfolio':portfolio, 'user':userStatus}
    else:
        return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

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
    day = get_date()[0]
    day_no = get_date()[1]
    month = get_date()[2]
    year = get_date()[3]
    if request.get_cookie("authID") == str(True):
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
    if request.get_cookie("authID") == str(True):
        userStatus = request.get_cookie("authID")
    else:
        userStatus = False
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

def passwordConfirm(userName, passWord):
    passwordList = pickle.load(open("data.pk", "rb"))
    passWord = passWord.encode('utf-8')
    hashed = bcrypt.hashpw(passWord, bcrypt.gensalt(12))
    try:
        if passwordList[userName]:
            if bcrypt.hashpw(passWord,passwordList[userName]) == passwordList[userName]:
                return True
            else:
                return False
        else:
            return False
    except KeyError:
        return False

@get('/login')
@auth_basic(passwordConfirm)
def login():
    response.set_cookie("authID", str(True))
    redirect("/")

@get('/logout')
def logout():
    response.set_cookie("authID", str(False))
    redirect("/")

@get('/register')
@auth_basic(passwordConfirm)
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
    return {'title':title,'site_name':site_name,'site_author':site_author,'navigation':navigation,'day':day,'day_no':day_no,'month':month,'year':year, 'user':userStatus}

@post('/register')
@auth_basic(passwordConfirm)
def register_got(title='Register User',site_name=site_name,site_author=site_author):
    email = request.forms.get('email')
    passWord = request.forms.get('pass')
    register_user(email, passWord)

def register_user(email, passWord):
    passwordList = pickle.load(open('data.pk', 'rb'))
    passWord = passWord.encode('utf-8')
    hashed = bcrypt.hashpw(passWord, bcrypt.gensalt(12))
    passwordList[email] = hashed
    pickle.dump(passwordList, open('data.pk','wb'))

@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='views/assets/img')

if __name__ == '__main__':
    run(server='cherrypy', host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
