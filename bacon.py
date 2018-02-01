'''
----------------------------------
Bacon Number
Author: Asif Mahmud
Student ID: 65123898
Date: 01/31/2018
University of California, Irvine
----------------------------------
'''

import os
import sys

class Node:
    def __init__(self, name, movies = [], next = None):
        self.name = name
        self.movies = movies
        self.next = next

class ActorGraph:
    # Create actor graph from the input file
    def __init__(self, file):
        nodeList = []
        self.graph = {}
        with open(file) as f:
            for line in f:
                line = line.strip().split('|')
                if (line[0] in self.graph.keys()):
                    self.graph[line[0]].movies.append(line[1])
                else:
                    n = Node(line[0], [line[1]])
                    nodeList.append(n)
                    self.graph[line[0]] = n

        for i in nodeList:
            for j in nodeList:
                if (j.name != i.name):
                    for k in j.movies:
                        if (k in i.movies):
                            node = self.graph[i.name]
                            while (node.next != None):
                                node = node.next
                            node.next = Node(j.name)
                            node.next.movies = j.movies
                            break;
    # Print graph
    def __str__(self):
        result = ''
        for k,v in self.graph.items():
            node = self.graph[k]
            while(node != None):
                result += node.name
                if (node.next != None):
                    result += ' -> '
                node = node.next
            result += '\n'
        return result


def main():
    a = ActorGraph('imdb.cslam.txt')
    print(a)
    return 0

if __name__ == '__main__':
    sys.exit(main())
