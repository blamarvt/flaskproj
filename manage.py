#!/usr/bin/python
import ConfigParser
import importlib
import os
import sys

import flask.ext.script


_APP_NAME = "myapp"
_CONFIG = None
_APP = None


def _get_app(config):
    """
    Create Flask app given a config.
    """
    static_folder = config.get("flask", "static_dir")
    template_folder = config.get("flask", "template_dir")
    debug = config.get("flask", "debug")
    flask_module = importlib.import_module("%s.flask" % _APP_NAME)

    app = flask.Flask(
        _APP_NAME,
        static_folder=static_folder,
        template_folder=template_folder,
    )

    for view, view_func_name, url in flask_module.VIEWS:
        module = importlib.import_module(view)
        view_func = getattr(module, view_func_name)
        view_func.methods = [view_func_name.split("_")[0]]
        app.add_url_rule(url,
            endpoint=".".join([view, view_func_name]),
            view_func=view_func,
        )

    app.debug = debug

    return app


def _get_config():
    """
    Load config from one of 4 locations:

        1) The local etc directory
        2) ~
        3) /etc/myapp
        4) MYAPP_CONF environment variable

    If the config can't be found in any of those places an
    error will be raised.
    """
    cp = ConfigParser.ConfigParser()

    loc_list = (
        os.path.join(os.path.dirname(__file__), "etc"),
        os.path.expanduser("~"),
        "/etc/%s" % _APP_NAME.lower(),
        os.environ.get("%s_CONF" % _APP_NAME.upper()),
    )

    for loc in loc_list:
        if loc is None:
            continue
        path = os.path.join(loc, "%s.conf" % _APP_NAME.lower())
        if os.path.exists(path):
            cp.read(path)
            return cp

    raise Exception("Unable to load config!", printme=True)


def run():
    """
    Run the Flask app with loaded config.
    """
    _APP.run()


def main():
    """
    Create manager, setup commands.
    """
    global _APP, _CONFIG
    _CONFIG = _get_config()
    _APP = _get_app(_CONFIG)

    manager = flask.ext.script.Manager(_APP)
    manager.command(run)

    manager.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        if hasattr(error, "printme"):
            sys.exit(error)
        else:
            raise
