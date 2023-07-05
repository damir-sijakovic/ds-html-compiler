import http.server
import socketserver
import os
from app import functions

PORT = 8000
WORK_DIR = os.path.dirname(os.path.abspath(__file__))


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			
			index_content = functions.load_view()

			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(index_content.encode('utf-8'))
		else:
			super().do_GET()

address = ('localhost', PORT)
os.chdir('public')  
httpd = socketserver.TCPServer(address, MyRequestHandler)

print(f"Server running at http://{address[0]}:{address[1]}/")
httpd.serve_forever()
