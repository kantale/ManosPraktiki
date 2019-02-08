import json
import requests

from http.server import BaseHTTPRequestHandler, HTTPServer

class My_Server(BaseHTTPRequestHandler):
	'''
	https://gist.github.com/bradmontgomery/2219997
	'''


	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

	def do_OPTIONS(self):
		'''
		https://stackoverflow.com/questions/16583827/cors-with-python-basehttpserver-501-unsupported-method-options-in-chrome
		TODO: ALLOW FROM A GIVEN ORIGIN
		'''

		self.send_response(200, "ok")
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS') # GET ??
		#self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
		self.send_header("Access-Control-Allow-Headers", "Content-Type")
		self.send_header("Access-Control-Allow-Headers", "x-csrftoken")
		self.send_header("Access-Control-Allow-Headers", "access-control-allow-origin")
		self.end_headers()

	def do_POST(self):
		'''
		TODO: check origin
		r = requests.post("http://127.0.0.1:8080", data=json.dumps({'action': 'GET EMPTY'}))0
		r.json()['p_index']
		'''

		#Check origin
		host = self.headers.get('Host')
		print ('### HOST:', host)
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		#header = {'Content-Type' : 'application/json'}
		#content_length = add_content_length(header,data)
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		print (post_data)

		try:
			#bashFile = open("bashscript.txt","w")
			data = json.loads(post_data)
		except Exception as e:
			print ('Could not parse JSON DATA..')
		
		ret_data = data['key1']
		#bashFile.write(data)
		ret_bytes = str.encode(json.dumps(ret_data))

		self._set_headers()
		self.wfile.write(ret_bytes)

def add_content_length(header, data):
	header['Content-Length'] = str(len(json.dumps(data)))


def run(server_class=HTTPServer, handler_class=My_Server, port=8080):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print ('Starting httpd : http://127.0.0.1:{}'.format(port))
	httpd.serve_forever()

if __name__ == '__main__':
	run()
