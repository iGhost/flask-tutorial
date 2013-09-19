CSRF_ENABLED = True
SECRET_KEY = '6sd4f6asdf3a21v5y4t65ui4p984b51xc321z654vabs98df79a8wr7ga65h4514b'
OPENID_PROVIDERS = [
    {'name': 'Google',   'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo',    'url': 'https://me.yahoo.com'},
    {'name': 'AOL',      'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr',   'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
