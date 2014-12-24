#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from lw_open_thread import app

if __name__ == '__main__':
    # I set this to .sock in lighttpd.conf, but apparently need .sock-0 here?
    WSGIServer(app, bindAddress='/tmp/lw-open-thread-fcgi.sock-0').run()
