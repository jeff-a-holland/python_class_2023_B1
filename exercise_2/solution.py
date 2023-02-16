#!/Users/jeff/.pyenv/shims/python

def myrange2(start, *args):
	'''myrange2 function'''

	print(f'Args are: {start} and {list(args)}')

	range_list = []
	if len(args) not in range(0,3):
		print('  ERROR!! Must only enter 1, 2 or 3 integer args')
		return(range_list)
	if len(args) in [1,2] and args[0] != None and args[0] <= start:
		print("  ERROR!! End can't be greater than or equal to start")
		return(range_list)

	range_start = start # Default when 2 or 3 args, will clobber if 0.
	range_step = 1  # Default value when only 1 or 2 args. Will clobber if 3.
	range_end = 0   # Default value when only 1 arg, will clobber if 2 or 3.
	if len(args) == 0:
		range_start = 0
		range_end = start
	elif len(args) == 1:
		if args[0] != None:
			range_end = args[0]
		else:
			range_start = 0
			range_end = start
	elif len(args) == 2:
		if args[0] != None:
			range_end = args[0]
		else:
			range_start = 0
			range_end = start
		if args[1] != None:
			range_step = args[1]
		else:
			range_step = 1

	range_list = [range_start]
	while range_start < (range_end - range_step):
		range_list.append(range_start + range_step)
		range_start = range_start + range_step
	return(range_list)

def myrange3(start, *args):
	'''myrange3 function'''

	iterator = iter(myrange2(start, *args))
	return iterator

def main():
	"""Main function"""

	# Module testing for myrange2 function
	print('----------------------------------------'
		  '\nModule testing for myrange2 function:\n'
		  '----------------------------------------')
	for x in myrange2(10):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange2(10,20,None):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange2(20,10,None):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange2(10, 30, 3):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange2(1,2,3,4):
		print(f'  Value in range: {x}')
	print('\n')

	# Module testing for myrange3 function
	print('---------------------------------------'
		  '\nModule testing for myrange3 function:\n'
		  '---------------------------------------')
	for x in myrange3(10):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange3(10, 20, None):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange3(20, 10, None):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange3(10, 30, 3):
		print(f'  Value in range: {x}')
	print('\n')
	for x in myrange3(1, 2, 3, 4):
		print(f'  Value in range: {x}')
	print('\n')

if __name__ == '__main__':
    main()