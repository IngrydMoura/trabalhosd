import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
print s.main()  # Returns 2**3 = 8

# Print list of available methods
print s.system.listMethods()