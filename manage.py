import flask.ext.script

import myapp.flask


manager = flask.ext.script.Manager(myapp.flask.app)


@manager.command
def hello():
    print "hello"


if __name__ == "__main__":
    manager.run()
