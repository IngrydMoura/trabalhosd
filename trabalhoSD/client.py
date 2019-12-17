import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
time = s.main()

print "Execution time %.3f" %time