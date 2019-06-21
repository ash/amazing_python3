# Creating a simple web server that
# serves the contents of the directory
# and displays files

import http.server
import socketserver

handler = \
    http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ('', 5000), handler) as httpd:
    # ^ ip (all ips)
    #    ^ port
    httpd.serve_forever()
