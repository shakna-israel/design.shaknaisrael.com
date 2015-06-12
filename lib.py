import datetime
import glob
import os
import re
import requests

def get_date():
    if datetime.datetime.today().weekday() == 0:
        day = 'mon'
    if datetime.datetime.today().weekday() == 2:
        day = 'tues'
    if datetime.datetime.today().weekday() == 3:
        day = 'wed'
    if datetime.datetime.today().weekday() == 4:
        day = 'thurs'
    if datetime.datetime.today().weekday() == 5:
        day = 'fri'
    if datetime.datetime.today().weekday() == 6:
        day = 'sat'
    if datetime.datetime.today().weekday() == 0:
        day = 'sun'
    year = datetime.date.today().year
    day_no = datetime.date.today().day + 1
    if datetime.datetime.today().month == 0:
        month = 'jan'
    if datetime.datetime.today().month == 1:
        month = 'feb'
    if datetime.datetime.today().month == 2:
        month = 'mar'
    if datetime.datetime.today().month == 3:
        month = 'apr'
    if datetime.datetime.today().month == 4:
        month = 'may'
    if datetime.datetime.today().month == 5:
        month = 'jun'
    if datetime.datetime.today().month == 6:
        month = 'jul'
    if datetime.datetime.today().month == 7:
        month = 'aug'
    if datetime.datetime.today().month == 8:
        month = 'sep'
    if datetime.datetime.today().month == 9:
        month = 'oct'
    if datetime.datetime.today().month == 10:
        month = 'nov'
    if datetime.datetime.today().month == 11:
        month = 'dec'
    return (day, day_no, month, year)

def get_portfolio():
    portfolio = []
    balcc = {'url': 'balcc.png', 'alt': 'Ballarat Christian College', 'page':'Balcc'}
    portfolio.append(balcc)
    haddon = {'url': 'haddon.png', 'alt': 'Haddon Community Learning Center', 'page': 'Haddon'}
    portfolio.append(haddon)
    return portfolio

def get_navigation():
    navigation = ["Home"]
    nav_exclude = ["Balcc","Haddon"]
    nav_last = ["Contact"]
    pages = glob.glob('views/content/*.tpl')
    for page in pages:
        if os.name == 'nt':
            dir_path = os.path.splitext(page)[0].split("\\")
        else:
            dir_path = os.path.splitext(page)[0].split("/")
        for listing in dir_path:
            filename = listing
            if filename in navigation:
                filename = False
            if filename in nav_exclude:
                filename = False
            if filename in nav_last:
                filename = False
        navigation.append(filename)
    navigation = navigation + nav_last
    return ( navigation, nav_exclude )

def get_content(title):
    fileToOpen = 'views/content/' + str(title) + '.tpl'
    content = ''
    openFile = open(fileToOpen, 'r')
    for line in openFile:
        line = line.strip()
        line = re.sub('<[^<]+?>', '', line)
        line = line.replace("{{ title }}", '*' + title + '*')
        content = content + line + '\n'
    return content

def send_email(email, message):
    requests.post(
        'https://api.mailgun.net/v2/shaknaisrael.com/messages',
        auth=("api", os.environ['MAILGUN_API']),
        data={"from": email,
              "to": 'contact@shaknaisrael.com',
              "subject": 'jm-design Contact Form Submitted',
              "text": message,
              "html": message,
              "o:tracking": True})
