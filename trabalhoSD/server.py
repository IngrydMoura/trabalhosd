from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

from multiprocessing import Process, freeze_support
from trabalho import Teste
import time

PORT = 8000

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


def main():
    teste = Teste()
    sched = teste.main()
    t0 = time.time()
    print __name__
    
    if __name__ == '__main__':
        freeze_support()
        sched.start()

    t1 = time.time()
    return (t1-t0)

server.register_function(main,'main')


if __name__ == '__main__':
	# Start the server
	try:
	    print('Use Control-C to exit')
	    server.serve_forever()
	except KeyboardInterrupt:
	    print('Exiting')