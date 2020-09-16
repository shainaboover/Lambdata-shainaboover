
from random import randint, sample, uniform
from acme import Product, BoxingGlove

adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun_list = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Dynamite']

def generate_products(num_products=30):
    product_list = []
    for x in range(num_products):
        adj = sample(adj_list, 1)[0]
        noun = sample(noun_list, 1)[0]
        name = adj + ' ' + noun
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products = Product(name, price, weight, flammability)
        product_list.append(products)
    return product_list


def inventory_report(product_list):
    name_list = []
    price_list = []
    weight_list = []
    flam_list = []
    for x in product_list:
        name_list.append(x.name)
        price_list.append(x.price)
        weight_list.append(x.weight)
        flam_list.append(x.flammability)
    prod_names = len(set(name_list))
    avg_price = sum(price_list) / len(price_list)
    avg_weight = sum(weight_list) / len(weight_list)
    avg_flam = sum(flam_list) / len(flam_list)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT', '\n',
    'Unique product names:', prod_names, '\n',
    'Average price:', avg_price, '\n',
    'Average weight:', avg_weight, '\n',
    'Average flammability:', avg_flam)


if __name__ == '__main__':
    inventory_report(generate_products())
