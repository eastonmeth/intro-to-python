weight = float(input('Weight: '))
units = input('(K)g or (L)bs: ')

if units.lower() == 'l':
	converted_weight = weight / 2.205
	converted_units = 'kg'
else:
	converted_weight = weight * 2.205
	converted_units = 'lbs'

print(f'Weight in {converted_units}: {converted_weight}')