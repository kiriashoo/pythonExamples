''' My GOOGLE FORM Test Auto-complete '''

import requests

payload = {
    'entry.1371035425': 'Harley Davidson',
    'entry.1757680857': 'https://erepublik.com/en'
}

import sys

with requests.Session() as c:
    r = c.post('https://docs.google.com/forms/d/1PkHsFwu8dJ_qYpun8DskfgCub9piEF5LvIYxkAUIXws/formResponse', data=payload)
    print 'Your response has been recorded.' in r.content
    print r.url
    print r.status_code
    print r.reason
    print r.elapsed  
    print r.content
