#!/usr/bin/env python3

class Stack:

	def __init__(self):
		self.STACK = []
	
	def push(self, item):
		self.STACK.append(item)
	
	def pop(self):
		self.STACK.pop()

	def peek(self):
		return self.STACK[-1]
	
	def empty(self):
		return self.STACK == []
	
	def count(self):
		return len(self.STACK)
	
	def stack(self):
		return self.STACK
	
	def dump(self):
		self.STACK.clear()