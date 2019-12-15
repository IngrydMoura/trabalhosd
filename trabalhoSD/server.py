from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

from trabalho import Teste

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

def main():
    sched = Teste.main()
    t0 = time.time()
    print __name__
    
    if __name__ == '__main__':
        freeze_support()
        sched.start()

    t1 = time.time()

    print "Execution time %.3f" %(t1-t0)
server.register_function(main, 'main')

# Run the server's main loop
server.serve_forever()