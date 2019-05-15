#! usr/bin/env python

"""
The QuickFind, QuickUnion and weighted QuickUnion 
UnionFind class from Coursera Algorithms Pt1 
Used to solve the dynamic connectivity problem
"""

class QuickFind():

    def __init__(self, N):
        self.id = list(range(N))

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for index, value in enumerate(self.id):
            if self.id[index] == pid:
                self.id[index] = qid

    
class QuickUnion():

    def __init__(self, N):
        """Set each element to be its own root"""
        self.id = list(range(N))

    def root(self, i):
        """Find the root of i"""
        while (i != self.id[i]):
            i = self.id[i]
        return i

    def connected(self, p, q):
        return root(p) == root(q)

    def union(self, p, q):
        i = root(p)
        j = root(q)

        self.id[i] = j


class WeightedQuickUnion():

    def __init__(self, N):
        """Set each element to be its own root 
            and maintain a size array to keep track of the 
            number of connections"""
        self.id = list(range(N))
        self.sz = [1] * N

    def root(self, i):
        """Find the root of i"""
        while (i != self.id[i]):
            i = self.id[i]
        return i

    def connected(self, p, q):
        return root(p) == root(q)

    def union(self, p, q):
        i = root(p)
        j = root(q)
        if (i == j):
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
            


