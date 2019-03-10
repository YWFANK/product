# read file
products = []
with open('products', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'product, price' in f:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])

#for inputing
while True:
	name = input('Enter the food name: ')
	if name == 'q':
		break
	price = input ('Enter the food price: ')
	products.append([name, price])
print(products)

#input product and price
for p in products:
	print(p)
	print(p[0])

#write data to file
with open('products.csv', 'w', encoding ='utf-8') as f:
	f.write('product, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')