#!/usr/bin/env python

from __future__ import print_function

# Set the path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_script.commands import Shell, ShowUrls
from flask_migrate import MigrateCommand, Migrate

from places import create_app
from places.database import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(use_debugger=True, use_reloader=True, host='0.0.0.0'))

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('show_urls', ShowUrls)

# from flask_api_app.core.accounts.commands import *

if __name__ == "__main__":
    manager.run()
