# Учёт товаров

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):  # получить список продуктов
        products = ''
        file = open(self.__file_name, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            products += line
        file.close()
        return products

    def add(self, *products):
        products_in_shop = self.get_products()
        for product in products:
            if product.name not in products_in_shop:
                file = open(self.__file_name, 'a')
                file.write(product.name + ', ' + str(product.weight) + ', ' + product.category + '\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
