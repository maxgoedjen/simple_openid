"""Flask Simple OpenID. One-line setup for OpenID login.
"""

from distutils.core import setup

doclines = __doc__.split("\n")

setup(name="flask_simple_openid",
      version="1.0.1",
      maintainer="Max Goedjen",
      maintainer_email="max.goedjen@gmail.com",
      url = "http://github.com/maxgoedjen/flask_simple_openid",
      platforms = ["any"],
      description = doclines[0],
      install_requires = ['flask_openid'],
      long_description = "\n".join(doclines[2:])
      )
