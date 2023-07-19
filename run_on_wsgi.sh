# Using uwsgi
uwsgi --http 0.0.0.0:8000 --wsgi-file first_step_3.py --callable __hug_wsgi__

# Or, using gunicorn
gunicorn first_step_3:__hug_wsgi__
