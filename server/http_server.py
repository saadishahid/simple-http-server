import socket
from server.config import ENCODING
from server.request_handler import RequestHandler


class HTTPServer:

    def __init__(self, host='localHost', port=8080):
        self.host = host
        self.port = port
        self.encoding = ENCODING
        self.server_socket = None

    def start_server(self):
        try:
            # Set up the server socket
            self.server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f'Server is running on http://{self.host}:{self.port}')

            # Main loop to handle client connections
            while True:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    print(f'Connection from {client_address}')
                    handler = RequestHandler(client_socket, self.encoding)
                    handler.handle_request()
                except Exception as client_error:
                    if 'client_address' in locals():
                        print(f"Error handling client {client_address}: {client_error}")
                    else:
                        print(f'Error handling client {client_error}')
        except Exception as e:
            print(f"Failed to start server: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()
                print("Server socket closed.")

