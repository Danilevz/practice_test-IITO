products = {'soap': 120, 'crisps': 160, 'soda': 80, 'bread': 75, 'butter': 200}
print('products in database: ')
print(products.keys())
choice=input('enter name of needed product to calculate price: ')
n=int(input('enter quantity of a needed product: '))
price_fone = products.get(choice, '__Error: entered product is not in a list__')
def productquan_counter(n, price_fone):
    if n==1:
        result=price_fone
        return result
    else:
        result=n*price_fone
        return result
print('price of a product in a relation to your quantity: ', productquan_counter(n, price_fone))