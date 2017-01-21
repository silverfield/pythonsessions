# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import sys
import socket as sckt
import select
import time
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from s12_chat import chat_settings

# ---------------------------------------------------------------
# Class - chat server
# ---------------------------------------------------------------


class ChatServer:
    """Simple chat server"""

    # ---------------------------------------------------------------
    # Constants
    # ---------------------------------------------------------------

    LISTEN_BACKLOG = 10

    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, host_name, port):
        self._sockets = []
        self._host_name = host_name
        self._port = port
        self._socket2nick = {}

        # set up server socket
        self._server_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)  # TCP socket for internet communication
        self._server_socket.setsockopt(sckt.SOL_SOCKET, sckt.SO_REUSEADDR, 1)  # address reusing... ??
        self._server_socket.bind((host_name, port))
        self._server_socket.listen(self.LISTEN_BACKLOG)
        self._sockets.append(self._server_socket)

        print("[INFO] Chat server listening on " + str(self._server_socket.getsockname()))

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def start_server(self):
        print("[INFO] Chat server started")

        while True:
            time.sleep(0.01)  # have this to guard CPU consumption

            # get the list sockets which are ready to be read
            r_sockets, _, _ = select.select(self._sockets, [], [], 0)  # 4th arg is time out. If 0, we don't block

            for sock in r_sockets:
                if sock == self._server_socket:  # a new connection request recieved
                    new_sock, addr = self._server_socket.accept()  # socket bound to the address
                    new_sock.settimeout(1)  # put to timeout mode
                    nick = self.__receive(new_sock)
                    if nick is None:
                        print("[ERR] Client on ({}) failed to join".format(new_sock.getpeername()))
                        continue
                    print("[INFO] Client on ({}) successfully joined as {}".format(new_sock.getpeername(), nick))
                    new_sock.settimeout(0)  # put to timeout mode
                    self._sockets.append(new_sock)
                    self._socket2nick[new_sock] = nick
                    self.__broadcast("User " + nick + " has joined the chat", new_sock)
                else:  # a message from a client, not a new connection
                    nick = self._socket2nick[sock]
                    msg = self.__receive(sock)
                    if msg is None:
                        print("[INFO] User " + nick + " sent a null message - disconnecting him")
                        self.__handle_broken_socket(sock)
                    else:
                        self.__broadcast('[' + nick + '] ' + msg, sock)

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __handle_broken_socket(self, sock):
        nick = self._socket2nick[sock]
        del self._socket2nick[sock]
        self._sockets.remove(sock)
        self.__broadcast("User " + nick + " has left the chat")

    def __receive(self, sock):
        """Tries to get a message from given socket.
        :return: the stripped and decoded message. None in case of error
        """
        try:
            data = sock.recv(chat_settings.BUFFER_SIZE)
            if data:
                return data.strip().decode()
            else:
                print("[ERR] Message expected on socket " + str(sock) + ", but not found")
        except Exception as e:
            print("[ERR] Exception occurred getting message on socket " + str(sock) + ": " + str(e))

        return None

    def __broadcast(self, message, except_for=None):
        """Broadcasts the message as it is on all user-sockets (possibly except for the one mentioned by argument)

        Handles broken sockets by removing them
        """
        broken_sockets = []
        print("[BCAST] " + message)
        for sock in self._sockets:
            if sock == self._server_socket or (except_for is not None and sock == except_for):
                continue
            try:
                sock.send(message.rstrip().encode())
            except Exception as e:
                print("[ERR] Exception sending message on socket " + str(sock) + ": " + str(e))
                broken_sockets.append(sock)

        for broken_sock in broken_sockets:
            self.__handle_broken_socket(broken_sock)

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main(argv):
    print("Arguments: [hostname] [port]")
    port = chat_settings.SERVER_PORT
    host_name = 'localhost'
    if len(argv) >= 1:
        host_name = argv[0]
    if len(argv) >= 2:
        port = int(argv[1])
    server = ChatServer(host_name, port)
    server.start_server()

if __name__ == '__main__':
    main(sys.argv[1:])