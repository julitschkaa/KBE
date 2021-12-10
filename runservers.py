#!/usr/bin/env python

import glob
import os.path
import socket
import subprocess
import sys

# manage.py must be made executable in order for this to work

# an interable of tuples in format:
# (SERVER_IP, SERVER_PORT, DJANGO_SETTINGS)
# SERVER_IP and/or SERVER_PORT can be None
SERVERS = (
    ('localhost', None, 'tax_calc_api.settings'),
    ('localhost', None, 'products_service_api.settings'),
)

# at which port to start attempt binding, when SERVER_PORT is empty
PORT_START = 8000

# you might want to run runserver_plus when using django-extensions
COMMAND = 'runserver'

################################################################################
# it shouldn't be necessary to edit below this line ############################
################################################################################

cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

servers_clean = []
last_port = PORT_START
for server in SERVERS:
    ip = server[0] or '127.0.0.1'
    if server[1]:
        port = server[1]
    else:
        while True:
            try:
                s = socket.socket()
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((ip, last_port))
                s.close()
                break
            except socket.error:
                last_port += 1
        port = last_port
        last_port += 1
    settings = server[2]
    manage_py = glob.glob(cwd + '/*/manage.py')
    try:
        env = os.environ.copy()
        env["TAX_CALC_API_URL"]="http://localhost:8000/"
        subprocess.Popen((manage_py[0],
                          'runserver',
                          '%s:%s' % (ip, port),
                          '--settings=%s' % settings), cwd=cwd, env=env)
    except IndexError:
        print ('Cannot find manage.py')
        sys.exit(1)

try:
    while True:
        pass
except KeyboardInterrupt:
    print ('All %d servers terminated' % len(SERVERS))
