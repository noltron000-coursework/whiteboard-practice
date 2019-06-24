def unique_sub(string):
	'''
		Find the longest substring of unique
		letters in a given string of n letters.
	'''
	# keep track of longest substring here
	best_sub = ''
	# iterate through each character in the string
	i = 0  # primary string index / iterator
	while i < len(string):
		# create character-storage unit; a set
		char_set = {}
		# again - iterate through each character in the string
		# that is located after the primary index, i
		j = 0  # secondary string index / iterator
		while i+j < len(string):
			# check if the char_set contains given character...
			if string[i+j] in char_set:
				# ...if it does, we will have to break this loop
				# but first, we can see if the substring is long
				if len(string[i:i+j]) > len(best_sub):
					# it is a long substring :D
					best_sub = string[i:i+j]
				# let's get out of this nested loop
				break
			else:
				# add indexed location to character-storage unit
				char_set[string[i+j]] = None # value is None
			j += 1  # iterate secondary index
		i += 1  # iterate primary index
		# unfortunately, there is no good way to break out
		# of this main loop early that I could find
	return 'LONGEST STRING:\n' + best_sub


mega_string = 'abcdefgghijklmnopqr yesss'


print(unique_sub(mega_string))
