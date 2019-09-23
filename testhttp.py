#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request

url = 'https://api.spotify.com/v1/search?type=artist&q=snoop'


f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))


# In[ ]:


import requests
r = request.get("http://www.itb.ac.id, headers=("content-type":"text/html","")")
print(r.status_code)
print(r.headers)
print(r.content)


# In[ ]:


from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




