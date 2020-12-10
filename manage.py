#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# List of Potential Commands #

# 1. Run Server. Website Run Locally. 127.0.0.8:8000/ #
# $ python manage.py runserver #

# 1. Install the requirements.txt file for packages #
# $ pip install -r requirements.txt #

# 2. Collect Static Files for Deployment #
# $ python manage.py collectstatic #

# 3. Install Anaconda #
# $ pip install conda #

# 4. Install django_heroku, and django #
# $ pip install django_heroku #
# $ pip install django #

# Anaconda is the environment you operate in. #
# Mine should come with this but any IDE will let you make one with anaconda. #

# Django is your back end. It tells the host where to look for files and manages everything complicated. #
# Heroku is the hosting platform holding our database, and website online. #

# We install the packages in requirements. #
# Collect our static files (when deploying). #
# Run Server #
# The ip provided will take you there and can be entered manually with any url we have in urls. #
# To close server be in terminal where the runserver command entered. #
# Ctrl+C #

# Yes everything in the project is critical at one stage or another. #
# If it ends in .py, .exe, or .txt., be aware it probably connects to a few different things. #

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nccovid19.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
