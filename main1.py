#!/usr/bin/env python3

from stack import Stack

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

if __name__ == "__main__":
	main()
