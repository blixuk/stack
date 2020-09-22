#!/usr/bin/env python3

from stack2 import Stack

stack = Stack()

def main():
	print(f'stack empty: {stack.empty()}')
	print(f'stack count: {stack.count()}')
	print(f'stack items: {stack.stack()}')
	
	print('stack push: A')
	stack.push('A')
	print('stack push: B')
	stack.push('B')
	print('stack push: C')
	stack.push('C')
	
	print(f'stack empty: {stack.empty()}')
	print(f'stack count: {stack.count()}')
	print(f'stack items: {stack.stack()}')
	
	print('stack pop')
	stack.pop()

	print(f'stack empty: {stack.empty()}')
	print(f'stack count: {stack.count()}')
	print(f'stack items: {stack.stack()}')
	
	print(f'stack peek: {stack.peek()}')

	print('stack pop: 0')
	print(f'stack pop: {stack[0]}')
	
	print(f'stack empty: {stack.empty()}')
	print(f'stack count: {stack.count()}')
	print(f'stack items: {stack.stack()}')
	
	print(f'stack len: {len(stack)}')
	
	print('stack check: C')
	if 'C' in stack:
		print('item in stack')
	else:
		print('item not in stack')
		
	print('stack check: B')
	if 'B' in stack:
		print('item in stack')
	else:
		print('item not in stack')

	print('stack push: A')
	stack.push('A')
	print('stack push: B')
	stack.push('B')
	print('stack push: C')
	stack.push('C')

	print('stack last: D')
	stack[stack.count() - 1] = 'D'

	print('stack first: X')
	stack[0] = 'X'

	print(f'stack empty: {stack.empty()}')
	print(f'stack count: {stack.count()}')
	print(f'stack items: {stack.stack()}')

	print('stack dump')
	stack.dump()

	print(f'stack empty: {stack.empty()}')
	print(f'stack count: {stack.count()}')
	print(f'stack items: {stack.stack()}')

if __name__ == "__main__":
	main()
