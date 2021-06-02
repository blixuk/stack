class Stack3:

	def __init__(self):
		self.STACK = []

	def __call__(self):
		print(self.STACK) 
	
	def push(self, item):
		self.STACK.append(item)

	def __add__(self, item):
		self.STACK.append(item)
	
	def __setitem__(self, pointer: int, item):
		try:
			if len(self.STACK) >= pointer:
				self.STACK[pointer] = item
		except:
			return None
	
	def pop(self):
		del self.STACK[-1:]

	def __sub__(self, count: int):
		if len(self.STACK) >= count:
			del self.STACK[-count:]

	def __del__(self):
		if len(self.STACK) > 0:
			del self.STACK[-1:]

	def __getitem__(self, pointer: int):
		try:
			if len(self.STACK) >= pointer:
				return self.STACK[pointer]
		except:
			return None
	
	def peek(self, pointer: int = -1):
		try:
			if len(self.STACK) >= pointer:
				return self.STACK[pointer]
		except:
			return None
	
	def __contains__(self, item):
		return item in self.STACK
	
	def empty(self):
		return self.STACK == []
	
	def len(self):
		return len(self.STACK)
	
	def __len__(self):
		return len(self.STACK)
	
	def stack(self):
		return self.STACK

	def __repr__(self):
		return str(self.STACK)

	def __str__(self):
		return str(self.STACK)[1:-1]
	
	def dump(self):
		self.STACK.clear()

	def iter(self):
		for item in reversed(self.STACK):
			yield item
	
	def __iter__(self):
		while self.STACK:
			yield self.STACK.pop()

	def reverse(self):
		return self.STACK[::-1]

	def __reversed__(self):
		return self.STACK[::-1]

	def __eq__(self, item): #equal to
		return self.STACK == item

	def __lt__(self, item): # lessthan
		return self.STACK < item

	def __le__(self, item): # lessthan or equal to
		return self.STACK <= item

	def __gt__(self, item): # greaterthan
		return self.STACK > item

	def __ge__(self, item): # greaterthan or equal to
		return self.STACK >= item

	def __ne__(self, item): # not equal to
		return self.STACK != item