'''
	Find the longest substring of unique
	letters in a given string of n letters.
'''

function(my_string)
	my_string.tolower()
	best_strings = []
	i = 0 // 1st index in string
	while i < length(my_string); i += 1
		if my_string@[i] = my_string@[i+j]
			best_strings -> append(my_string[i])
	find best string in my string
	return it
