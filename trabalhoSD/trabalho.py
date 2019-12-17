import sys, os
import time

sys.path.append(os.environ['PYDFHOME'])
f = lambda x: 1/(1+x**2)

from pyDF import *


class Teste:
    
    def psum(self,args):
        stride, my_id, nprocs = args[0]
        print (stride, my_id, nprocs)

        sump = 0.0 
        print "Doing partial summation"

        x = stride * my_id
        while x < 1.0:
            sump += f(x) * stride
            x += stride * nprocs 

        print "Finished partial summation %f"  %sump
        return sump

    def sum_total(self,args):
        total = 0.0
        print "Partials %s" %args
        for partial in args:
            total += partial

            pi = total * 4
        print "Reduction: %f" %pi

    def main(self):
    	f = lambda x: 1/(1+x**2)

        nprocs = int(2)
        stride = float(0.01)

        graph = DFGraph()
        sched = Scheduler(graph, nprocs, mpi_enabled = False)

        R = Node(self.sum_total, nprocs)
        graph.add(R)


        for i in range(nprocs):
            Id = Feeder([stride, i, nprocs])
            graph.add(Id)

            Spartial = Node(self.psum, 1)
            graph.add(Spartial)

            Id.add_edge(Spartial, 0)
            Spartial.add_edge(R, i)
            
        return sched
