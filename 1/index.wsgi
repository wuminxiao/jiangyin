import sae
from chihuo import wsgi

application = sae.create_wsgi_app(wsgi.application)
