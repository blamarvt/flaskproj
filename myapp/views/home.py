import flask


def get_home():
    """
    Render and return the home page.
    """
    return "Welcome from %s" % flask.request.remote_addr
