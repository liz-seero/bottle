#!/usr/bin/env python

"""
Simple class example for OpenExVis.

This is a simple class that initialises a couple of variables and then runs a
while loop with them printing a result.
"""

class Visclass:

    def simple_loop(self):
        while self.count < self.to_loop:
            self.count += 1
        print self.count

    def __init__(self):
        self.count = 0
        self.to_loop = 3

def main():
	v = Visclass()
	v.simple_loop()

if __name__=='__main__':
	main()

