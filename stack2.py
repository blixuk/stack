#!/usr/bin/env python3

class Stack:

	def __init__(self):
		self.STACK = []
	
	def push(self, item):
		self.STACK.append(item)
	
	def __setitem__(self, point, item):
		self.STACK[point] = item
	
	def pop(self):
		self.STACK.pop()
	
	def __getitem__(self, key):
		if isinstance(key, int):
			return self.STACK.pop(key)
		else:
			return self.STACK.pop()
		raise TypeError('Cannot get key %s' % key)
	
	def peek(self):
		return self.STACK[-1]
	
	def __contains__(self, item):
		return item in self.STACK
	
	def empty(self):
		return self.STACK == []
	
	def count(self):
		return len(self.STACK)
	
	def __len__(self):
		return len(self.STACK)
	
	def stack(self):
		return self.STACK
	
	def dump(self):
		self.STACK.clear()
	
	def __iter__(self):
		while self.STACK:
			yield self.STACK.pop()