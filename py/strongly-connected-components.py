#!/usr/bin/python

import time
import sys
import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**9)

t = time.clock()

def main():
    max_n = 123456
    filename = "./stronglyconnectedcomponents.txt"
    # print "init twopass"
    twopass = TwoPass(max_n, filename)
    # print "running passes", time.clock() - t
    largest_groups = twopass.passes()
    print "---------------"
    print largest_groups
    print "---------------\ndone.\n", time.clock() - t


class TwoPass(object):
    def __init__(self, nodes, filename):
        self.nodes_len = nodes
        self.nodes = [Node(self, x) for x in xrange(nodes)]
        self.process_file(filename)
        self.pass_number = 0
        self.finish_times = []
        self.last_node = None


    def run(self):
        out = self.passes()
        return out


    def process_file(self, filename):
        fh = open(filename)
        for line in fh:
            line = line.split()
            x, y = line[0:2]
            x, y = int(x)-1, int(y)-1
            self.nodes[x].add_forward(y)
            self.nodes[y].add_backward(x)
        fh.close()


    def passes(self):
        ## first pass
        n = self.nodes_len -1
        while n >= 0:
            if not self.nodes[n].is_explored(self.pass_number):
                self.dfs(n)
            n -= 1

        ## second pass
        self.pass_number += 1
        while self.finish_times:
            n = self.finish_times.pop()
            if not self.nodes[n].is_explored(self.pass_number):
                self.last_node = n
                self.dfs(n)

        return self.find_groups()


    def dfs(self, n):
        self.nodes[n].set_explored(self.pass_number)

        if self.pass_number == 1: 
            self.nodes[n].set_leader(self.last_node)
        
        next_n = self.nodes[n].get_node(self.pass_number)
        while next_n is not None:
            self.dfs(next_n)
            next_n = self.nodes[n].get_node(self.pass_number)

        if self.pass_number == 0:
            self.finish_times.append(n)


    def find_groups(self):
        groups = {}
        for n in self.nodes:
            if n.leader in groups:
                groups[n.leader] += 1
            else:
                groups[n.leader] = 1
        largest_groups = [0,0,0,0,0]
        for k,v in groups.iteritems():
            for i in xrange(5):
                if v > largest_groups[i]:
                    largest_groups.insert(i, v)
                    largest_groups.pop()
                    break

        return largest_groups


class Node(object):
    __slots__ = ["parent", "pos", "forward", "backward", "is_explored_first", "is_explored_second", "leader"]
    def __init__(self, parent, pos):
        self.parent = parent
        self.pos = pos
        self.forward = []
        self.backward = []
        self.is_explored_first = False
        self.is_explored_second = False
        self.leader = None


    def add_forward(self, node):
        self.forward.append(node)


    def add_backward(self, node):
        self.backward.append(node)


    def set_explored(self, pass_number):
        if pass_number == 0:
            self.is_explored_first = True
        else:
            self.is_explored_second = True


    def set_leader(self, leader):
        self.leader = leader


    def is_explored(self, pass_number):
        if pass_number == 0:
            return self.is_explored_first
        else:
            return self.is_explored_second


    def get_node(self, pass_number):
        if pass_number == 0:
            for n in self.backward:
                if not self.parent.nodes[n].is_explored(pass_number): 
                    return n
        else:
            for n in self.forward:
                if not self.parent.nodes[n].is_explored(pass_number):
                    return n
        return None


if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()