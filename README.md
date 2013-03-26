# Flask Simple OpenID
*One line OpenID login*


## Setup

Import the module:

`from flask_simple_openid import SimpleOpenID`

Configure it:

`openid = SimpleOpenID(app, 'YOUR_APP_SECRET')`

### Arguments

#### Required

- `app` - Your Flask App
- `secret` - Flask App secret

#### Optional

- `valid_domain` - Domains to restrict login to. Defaults to `''`, which allows login with emails from any domain.
- `login_url` - URL to your login page. This page should contain a link to `/login_redirect`. Defaults to `login.html` 
- `openid_url` - Auth URL for OpenID provider. Defaults to Google.

## Use

### Restricting Login

To restrict access to a page, use the `require_login` decorator.

Example:

    @app.route('/hello')
    @openid.require_login
    def main():
        return 'Hello World'

Access user info with the `user_realname` and `user_email` properties.
    
    @app.route('/hello')
    @openid.require_login
    def main():
        return '{email}, {realname}'.format(email=openid.user_email, realname=openid.user_realname