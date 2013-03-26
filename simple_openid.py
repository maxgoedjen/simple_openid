from flask import *
from flask_openid import OpenID
from functools import wraps

class SimpleOpenID(object):

    def __init__(self, app, secret='', valid_domain='', login_url='login.html', openid_url='https://www.google.com/accounts/o8/id'):
        
        app.config.update(SECRET_KEY = secret)
        openid = OpenID(app,'oid')
        self.login_url = login_url
        
        @app.before_request
        def lookup_current_user():
            g.user = None
            if 'user' in session:
                g.user = session['user']
        
        @app.route('/login')
        def login():
            return send_file(self.login_url)
        
        @app.route('/logout')
        def logout():
            session.pop('user', None)
            return redirect('/login')

        @app.route('/login_redirect')
        @openid.loginhandler
        def login_handler():
            return openid.try_login(openid_url, ask_for=['email','fullname'])
                    
        @openid.after_login
        def after_login(resp):
            if resp.email and (resp.email.endswith('@{0}'.format(valid_domain)) or not valid_domain):
                session['user'] = {
                    'openid' : resp.identity_url,
                    'email' : resp.email,
                    'fullname' : resp.fullname,
                }
                session.permanent = True
            if 'unauth_route' in session:
                return redirect(session.pop('unauth_route', None))
            return redirect('/')
        
        @openid.errorhandler
        def on_error(message):
            print('Error: ' + message)

    def require_login(self, f, *arg, **kw):
        @wraps(f)
        def wrapper(*arg, **kw):
            if g.user:
                return f(*arg, **kw)
            else:
                def unauthorized(*arg, **kw):
                    session['unauth_route'] = '/{route}'.format(**kw)
                    return redirect('/login')
                return unauthorized(*arg, **kw)
        return wrapper
        
    @property
    def user_realname(self):
        if g.user:
            return g.user['fullname']
        return ''
        

    @property
    def user_email(self):
        if g.user:
            return g.user['email']
        return ''