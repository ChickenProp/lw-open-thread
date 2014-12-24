#! /usr/bin/python

import requests
import flask
from lxml import html

app = flask.Flask(__name__)
app.debug = True

@app.route("/")
def redirect():
    try:
        r = requests.get('http://lesswrong.com/r/discussion/api/side_open')
        h = html.fromstring(r.text)
        a = h.xpath('./h2/a')[0]
        return flask.redirect(a.get('href'))
    except Exception as e:
        return failed(e)

def failed(err):
    app.logger.error('Something failed', exc_info=True)
    err_msg = """
        <html><head><title>Whoops!</title><body>

        <p>Something went wrong. There's currently no mechanism to alert me when
        this happens, so please let me know, either by
        <a href="http://lesswrong.com/message/compose/?to=philh">private
        message</a> or <a href="mailto:philip.hazelden@gmail.com">email</a>.<p>

        <p>Please quote this error message:</p>
        <p><code>{{ msg|e }}</code></p></body></html>
    """
    return flask.render_template_string(err_msg, msg=repr(err))


if __name__ == "__main__":
    app.run()
