from http.server import BaseHTTPRequestHandler,CGIHTTPRequestHandler, HTTPServer
from gather_html import init_server_pages
import time

hostName = "localhost"
serverPort = 8080
def get_pages():
    return init_server_pages("pages")
class MyServer(BaseHTTPRequestHandler):
    # def __init__(self):
    #     self.pages = get_pages()
    pages = get_pages()
    def do_GET(self):
        
        if(self.requestline.count("index.html") > 0):

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))
        
            for line in self.pages["index.html"]:
                self.wfile.write(bytes(line, "utf-8"))
        elif(self.requestline.count("work.html") > 0):

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            for line in self.pages["work.html"]:
                self.wfile.write(bytes(line, "utf-8"))
    
        

        
    
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")