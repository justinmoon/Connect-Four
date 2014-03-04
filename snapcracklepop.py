i = 1
while i < 101:
    print_value = ''
    if (i%3 == 0):
    	print_value += "Crackle"
    if (i%5 == 0):
    	print_value += "Pop"
    if print_value:
    	print print_value
    else:
    	print i
    i += 1
