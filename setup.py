"""Simple OpenID. One-line setup for OpenID login for Flask.
"""

from distutils.core import setup

doclines = __doc__.split("\n")

setup(name="simple_openid",
      version="1.0.4",
      maintainer="Max Goedjen",
      maintainer_email="max.goedjen@gmail.com",
      url = "http://github.com/maxgoedjen/simple_openid",
      platforms = ["any"],
      py_modules=['simple_openid'],
      description = doclines[0],
      install_requires = ['flask_openid'],
      long_description = "\n".join(doclines[2:])
      )
