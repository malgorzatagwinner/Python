#!/usr/bin/env python3
# -*- coding: utf-8-*-
import sys

def numberofwords(line):
	print('W tym stringu jest ', len(line.split()), ' wyrazów') 

line = ' '.join(sys.stdin.readlines())
numberofwords(line)

if __name__ == '__main__':
	#testy
	assert 1 == numberofwords('test1')
	assert 2 == numberofwords('test 2')
	assert 2 == numberofwords('test    \t3')
	assert 2 == numberofwords('test \n 4')

