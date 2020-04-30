# this code take care of the client side of the p2p network
# and the download of the file

from server_and_client.constants import *

class Client:
    def __init__(self,addr):
        # socket setup
        self.sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # set flags to resuse socket in time_wait state
        self.sckt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        # connect
        self.sckt.connect((addr,PORT))

        self.previews_data = None

        # create thread to 
        send_thread = threading.Thread(target=self.send_message)
        send_thread.daemon = True
        send_thread.start()
        
        while 1:
            receive_thread = threading.Thread(target=self.receive_message)
            # receive_thread.daemon = True
            receive_thread.start()
            receive_thread.join()

            recv_data = self.receive_message()

            if not recv_data:
                print("server connection failed")
                break
            elif recv_data[0:1] == b'\x11':
                # the 1st byte x\11 lets the program know we have peers
                print("list of peers obtained")
                # update peers list
                self.update_peers(recv_data[1:])


    def send_message(self):
        try:
            self.sckt.send(REQUEST_STRING.encode('utf-8'))
            print("request sent")
        except KeyboardInterrupt:
            self.send_disconnect_signal()

            
    def receive_message(self):
        try:
            print("Recieving data")
            data = self.sckt.recv(BYTE_SIZE)
            rData = data.decode("utf-8")
            print(rData)
            print("Message recieved on client side")
            if self.previews_data != data and data[0:1] != b'\x11':
                fileIO.create_file(data)
                self.previews_data = data
            return data
        except KeyboardInterrupt:
            self.send_disconnect_signal()

    def update_peers(self,peer_list):
        #the last value is None, so we nee it exclude using -1
        import p2p
        p2p.peers = str(peer_list,"utf-8").split(',')[:-1]
        

    def send_disconnect_signal(self):
        print("Disconnecting from server")
        self.sckt.send("q".encode("utf-8"))
        sys.exit()
        pass

        