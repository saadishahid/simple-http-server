class RequestHandler:
    def __init__(self, client_socket, encoding='utf-8'):
        self.client_socket = client_socket
        self.encoding = encoding

    def handle_request(self):
        try:
            # Receive and decode the client request
            request = self.client_socket.recv(1024).decode(self.encoding)
            print("Received request:", request)
            # Generate and send response
            response = self.generate_response(request)
            self.client_socket.sendall(response.encode(self.encoding))
        except UnicodeDecodeError:
            self.client_socket.sendall("HTTP/1.1 400 Bad Request\n\nInvalid character encoding.".encode(self.encoding))
        except Exception as e:
            print(f"Error handling request: {e}")
            self.client_socket.sendall("HTTP/1.1 500 Internal Server Error\n\nAn error occurred.".encode(self.encoding))
        finally:
            self.client_socket.close()


    def generate_response(self, request):

        if "GET / " in request:
            # Send a properly formatted HTTP response
            return (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                "Connection: close\r\n"
                "\r\n"
                "Welcome to My Simple Server!"
            )
        else:
            return (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/plain\r\n"
                "Connection: close\r\n"
                "\r\n"
                "Page Not Found"
            )
