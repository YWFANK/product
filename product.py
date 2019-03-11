import os # operating system

#read file
#內部讀取的檔建議設為傳入參數，不要放在fuction裡面
#每個function只寫一個功能，不要混用
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'product, price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#for inputing
def user_input(products):
	while True:
		name = input('Enter the food name: ')
		if name == 'q':
			break
		price = input ('Enter the food price: ')
		products.append([name, price])
	print(products)
	return products

#input product and price
def print_products(products):
	for p in products:
		print(p)
		print(p[0])

#write data to file
def write_file(filename, products):
	with open(filename, 'w', encoding ='utf-8') as f:
		f.write('product, price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('the file is here')
		products = read_file(filename)
	else:
		print('the file is not here')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()