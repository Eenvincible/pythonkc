import sys
import os

project_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0]
sys.path.append(project_path)
sys.path.append(project_path + '/pythonkc/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pythonkc.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
