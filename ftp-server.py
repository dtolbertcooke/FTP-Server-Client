from pyftpdlib import DummyAuthorizer
from pyftpdlib import FTPHandler
from pyftpdlib import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/dtolbertcooke", perm="elradfmw")
authorizer.add_anonymous("/home/dtolbertcooke", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()
