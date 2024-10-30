# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать
# следующими свойствами:
# 1. Атрибут name - название продукта (строка).
# 2. Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# 3. Атрибут category - категория товара (строка).
# 4. Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены
# запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# 1. Инкапсулированный атрибут __file_name = 'products.txt'.
# 2. Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
# строку со всеми товарами из файла __file_name.
# 3. Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

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


    def get_products(self):
        file = open(self.__file_name, 'r+')
        file_product = file.read()
        file.close()
        return file_product

    def add(self, *products):
        num = self.get_products()
        file = open(self.__file_name, 'a+')
        for i in products:
            if str(i) not in num:
                file.write(str(i) + '\n')
                num += str(i) + '\n'
            else:
                print(f'Продукт {i} уже имеется')
        file.close()



s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
