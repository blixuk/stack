# stack
Simple Python Stack & more advanced stack

### Stack

- init
- push ( item ) - add item to top of the stack
- pop - remove last item off the stack
- peek - return last item on the stack
- empty - return True or False
- count - return number of items in the stack
- stack - return the stack object
- dump - clear the stack

sample code
```
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
```
output
```
stack empty: True
stack count: 0
stack items: []
stack push: A
stack push: B
stack push: C
stack empty: False
stack count: 3
stack items: ['A', 'B', 'C']
stack pop
stack empty: False
stack count: 2
stack items: ['A', 'B']
stack peek: B
```

### Stack 2

- init
- push ( item ) - add item to top of the stack
- _ _ setitem _ _ - add item at any point
- pop - remove last item off the stack
- _ _ getitem _ _ - remove any item
- peek - return last item on the stack
- _ _ contains _ _ - check if any item is on the stack
- empty - return True or False
- count - return number of items in the stack
- _ _ len _ _ - return the amount of items on the stack
- stack - return the stack object
- dump - clear the stack
- _ _ iter _ _ - iterate over the stack

sample code
```
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
```
output
```
stack empty: True
stack count: 0
stack items: []
stack push: A
stack push: B
stack push: C
stack empty: False
stack count: 3
stack items: ['A', 'B', 'C']
stack pop
stack empty: False
stack count: 2
stack items: ['A', 'B']
stack peek: B
stack pop: 0
stack pop: A
stack empty: False
stack count: 1
stack items: ['B']
stack len: 1
stack check: C
item not in stack
stack check: B
item in stack
stack push: A
stack push: B
stack push: C
stack last: D
stack first: X
stack empty: False
stack count: 4
stack items: ['X', 'A', 'B', 'D']
stack dump
stack empty: True
stack count: 0
stack items: []
```