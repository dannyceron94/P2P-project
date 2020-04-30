# this class deals witht he upload of the file being shared among peers

from server_and_client.constants import *

class Server:
    def __init__(self,msg):
        try:
            self.msg = msg
            #defining a socket
            self.sckt =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sckt.setsockopt(socket.SOL_SOCKET,  socket.SO_REUSEADDR,1)
            # lists
            self.connections = []
            self.peers = []
            # 
            self.sckt.bind((HOST,PORT))
            
            self.sckt.listen(1)
            print("sever is running")
            # run sever logic
            self.run()
        except:
            sys.exit()
    
    # this method sends the data to a client
    # and closes the connecion if the client
    # disconnects
    def handler(self,connecion,address):
        print("inhandler")
        try:
            while 1:
                data = connecion.recv(BYTE_SIZE)
                for connecion in self.connections:
                    # check if peer wants to disconnect
                    if data and data.decode('utf-8')[0].lower() =='q':
                    # diconnect peer
                        self.disconnect(address,connecion)
                        return 0
                    elif data and data.decode('utf-8')[0].lower() == REQUEST_STRING:
                        print("Uploading file")
                        connecion.send(self.msg)
        except Exception as e:
            print(e)
            sys.exit()

    def disconnect(self,address, connection):
        self.connections.remove(connection)
        self.peers.remove(address)
        connection.close()
        # send peers
        self.send_peers()
        print("{}, is disconnected".format(address))

    def run(self):
        while 1:
            connection, addr = self.sckt.accept()
            #append information to lists
            self.peers.append(addr)
            print("All peers:{}".format(self.peers))
            # send list of all peers connected
            self.send_peers()
            # create a handler thread
            handler_thread = threading.Thread(target=self.handler,
                                              args=(connection,addr))
            handler_thread.daemon=True
            handler_thread.start()
            self.connections.append(connection)
            print("{} is now connected".format(addr))

    # sends a the update list of peers
    def send_peers(self):
        # create list of connected peers
        peer_list =""
        for peer in self.peers:
            peer_list += str(peer) + ","
        # send the list of peers to peers connected
        for connection in self.connections:
            data = PEER_BYTE_DIFFERENTIATOR + bytes(peer_list,'utf-8')
            connection.send(data)