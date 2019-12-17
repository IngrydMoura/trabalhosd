import copy
import time

import sys, os
sys.path.append(os.environ['PYDFHOME'])

from pyDF import *

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(A)

class Teste:
    def pdet(self,args):
        stride, my_id, nprocs = args[0]
        print (stride, my_id, nprocs)

        print "Doing partial summation"

        AM = copy.copy(A)

        stride = int(stride)
        my_id = int(my_id)
        x = stride * my_id
        while x < n:
            for fd in range(x-stride,x):  
                for i in range(fd + 1, x): 
                    if AM[fd][fd] == 0:  
                        AM[fd][fd] == 1.0e-18  

                    crScaler = AM[i][fd] / AM[fd][fd]
                    
                    for j in range(x-stride,x):
                        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            x += stride * nprocs
   
        print "Finished partial summation %s\n" %AM
        return AM


    def det_total(self,args):
        # product = 1.0
        # print "Partials %s" %args
        # for partial in args:
        #     obj = args[partial]
        #     for hue in obj
        #         product *= float(obj[hue][hue])
        # product = round(product,9)+0
        # print "Reduction: %f" %product

    def main(self):

        nprocs = int(2)
        stride = float(2)

        graph = DFGraph()
        sched = Scheduler(graph, nprocs, mpi_enabled = False)

        R = Node(self.det_total, nprocs)
        graph.add(R)


        for i in range(nprocs):
            Id = Feeder([stride, i, nprocs])
            graph.add(Id)

            Spartial = Node(self.pdet, 1)
            graph.add(Spartial)

            Id.add_edge(Spartial, 0)
            Spartial.add_edge(R, i)
            
        return sched