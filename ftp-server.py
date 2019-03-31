from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.authorizers import FTPHandler
from pyftpdlib.authorizers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user('user', '12345', '/home/dtolbertcooke', perm='elradfmw')
authorizer.add_anonymous('/home/dtolbertcooke', perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizers
server = FTPServer(('127.0.0.1', 1026), handler)
server.serve_forever()
