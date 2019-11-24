text = open("brain", 'r')

file = open("fixed_brain", 'w')

file.write(text.read().replace('а', 'о'))