#!/Users/jeff/.pyenv/shims/python

import re

def re_logtolist(data):
	"""logtolist function that returns a list of dicts"""

	data_list = []
	temp_dict = {}

	temp_list = data.split('\n')
	regex = '(^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}) .*? \\[(.*?)\\] "(.*?)"'
	for line in temp_list:
		fields = re.match(regex, line)
		if fields:
			ip = fields.group(1)
			ts = fields.group(2)
			r = fields.group(3)

			temp_dict['ip_address'] = ip
			temp_dict.update({'timestamp':ts})
			temp_dict.update({'request':r})
			data_list.append(temp_dict)
		else:
			pass

	print(data_list)
	return(data_list)

def main():
	""" Main function"""

	file = 'mini-access-log.txt'
	with open(file, 'r') as fh:
		data = fh.read()
	re_logtolist(data)

if __name__ == '__main__':
    main()