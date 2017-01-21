# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import sys
import socket
import select
import time
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from s12_chat import chat_settings

# ---------------------------------------------------------------
# Class
# ---------------------------------------------------------------


class ChatClient:
    """Simple implementation of a chat client"""

    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, nick, server_hostname, server_port=chat_settings.SERVER_PORT):
        self._server_hostname = server_hostname
        self._server_port = server_port
        self._nick = nick

        # set up client socket
        self._client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client_sock.settimeout(2)  # put to timeout mode
        try:
            self._client_sock.connect((self._server_hostname, self._server_port))
        except ConnectionRefusedError:
            print("Server probably not running at {}:{}".format(server_hostname, server_port))
            exit(0)
        self._client_sock.send(self._nick.encode())

        print("Chat server on " + str(self._client_sock.getpeername()))
        print("You are on " + str(self._client_sock.getsockname()))

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def start_chatting(self):
        print("Hi " + str(self._nick) + "! You're connected to the chat server. You can start sending messages")
        self.__prompt()

        socket_list = [sys.stdin, self._client_sock]

        while True:
            time.sleep(0.01)

            # get the list sockets which are readable
            r_sockets, _, _ = select.select(socket_list, [], [])

            for sock in r_sockets:
                if sock == self._client_sock:  # incoming message from server
                    data = sock.recv(chat_settings.BUFFER_SIZE).decode()
                    if not data:
                        print("Server shut down. Terminating...")
                        exit(0)
                    print()
                    print(data)
                    self.__prompt()
                else:  # user entered a message
                    msg = sys.stdin.readline()
                    self._client_sock.send(msg.encode())
                    self.__prompt()

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __prompt(self):
        sys.stdout.write("[" + self._nick + "] ")
        sys.stdout.flush()

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main(argv):
    if len(argv) < 2:
        print("Provide arguments: nick server_hostname [server_port]")
        exit(1)
    nick = argv[0]
    server_hostname = argv[1]
    server_port = chat_settings.SERVER_PORT
    if len(argv) >= 3:
        server_port = int(argv[2])

    client = ChatClient(nick, server_hostname, server_port)
    client.start_chatting()

if __name__ == '__main__':
    main(sys.argv[1:])