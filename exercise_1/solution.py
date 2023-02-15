#!/Users/jeff/.pyenv/shims/python
import re

# Global var, a dict of lists. Keys are countries, values are cities
visits = {}

def collect_places():
	"""Collect Places Function"""

	while True:
		city_country = input('Tell me where you went: ')

		# Account for spaces before/after cities and countries
		if re.match('\\s{0,}[^ ].*\\s{0,},\\s{0,}[^ ].*\\s{0}', city_country):
			city_country_list = city_country.split(',')
			# Remove any spaces
			city = (city_country_list[0].lstrip()).rstrip()
			country = (city_country_list[1].lstrip()).rstrip()

			if country in visits:
				visits[country].append(city)
			else:
				visits[country] = [city]

		elif ',' not in city_country and len(city_country.split()) > 0:
			print("That's not a legal city, country combination")

		else:
			# Call display_places function and break out of while loop
			display_places()
			break

def display_places():
	"""Display Places Function"""
	sorted_keys = sorted(visits.keys())
	sorted_dict = {key: visits[key] for key in sorted_keys}
	print('\nYou Visited:')
	for k, l in sorted_dict.items():
		l_unique = list(dict.fromkeys(l))
		l_unique.sort()
		print(k)
		for v in l_unique:
			if l.count(v) > 1:
				print(f'  {v} (' + str(l.count(v)) + ')')
			else:
				print(f'  {v}')
	print('\n')

def main():
	"""Main Function"""
	print('\n')
	collect_places()

if __name__ == '__main__':
    main()