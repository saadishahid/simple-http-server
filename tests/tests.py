# tests/test_server.py
import socket
from server.config import HOST, PORT

def test_server_response():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"GET / HTTP/1.1\nHost: localhost\n\n")
        response = client_socket.recv(1024).decode('utf-8')
        assert "200 OK" in response
