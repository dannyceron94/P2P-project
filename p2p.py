from server_and_client.constants import *
from server_and_client.client import Client
from server_and_client.server import Server

class p2p:
    peers = ['127.0.0.1']

def main():
    msg = fileIO.convert_to_bytes()
    while True:
        try:
            print("Attempting to connect to perr")
            time.sleep(randint(RAN_TIME_START,RAN_TIME_END))
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

                try:
                    server = Server(msg)
                    print("now a server")
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass
        except KeyboardInterrupt as e:
            print(e)
            sys.exit(0)
if __name__ == "__main__":
    main()