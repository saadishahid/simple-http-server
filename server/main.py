from server.http_server import HTTPServer
from server.config import HOST, PORT

if __name__ == "__main__":
    server = HTTPServer(host=HOST, port=PORT)
    server.start_server()

