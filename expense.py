products = []
while True:
	name = input('enter the product name')
	if name == 'q':
		break
	price = input('enter the price')
	products.append([name,price])

print(products)
