
def unique_sub(string)
	'''
		Find the longest substring of unique
		letters in a given string of n letters.
	'''
	i = 0 # primary string index
	while i < length(my_string); i += 1
		j = i+1 # secondary string index
		while j < length(my_string); j += 1
		if my_string@[i] = my_string@[i+j+1]
			best_strings -> append(my_string[i])
	find best string in my string
	return it
