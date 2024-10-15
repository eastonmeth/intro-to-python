temperature = float(input('What is the current temperature?: '))

if temperature > 30:
	print("It's a hot day.")
	print('Drink plenty of water!')
elif temperature > 20:
	print("It's a nice day.")
elif temperature > 10:
	print("It's a bit chilly.")
else:
	print("It's a cold day.")