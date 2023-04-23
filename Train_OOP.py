class Furniture:
    '''It's all about Furniture'''

    def __init__(self, name: object, material: object, color: object, price: object) -> object:
        self.name = name
        self.material = material
        self.color = color
        self.price = price


    def display_function(self):
        print("Я - предмет мебели")


    def display_furniture(self):
        print(f'Название: {self.name}. Цена: {self.price}')


class Table(Furniture):
    '''Class: table, subclass for Furniture'''

    name = "table"
    material = "wood"
    color = "braun"
    price = 100

    def __init__(self, ttype):
        self.ttype = ttype


furn1 = Furniture("table", "wood", "braun", 1000)
furn2 = Furniture("wardrobe", "wood", "braun", 2000)
furn3 = Furniture("chear", "metal", "silver", 300)
table1 = Table("kitchen")
table2 = Table("student")
table3 = Table("office")
print(f"Furniture: {Furniture.__doc__}")
print(f"Table: {Table.__doc__}")

# print(*Furniture.__dict__, sep="\n")
print(furn1.display_function())
print(furn1.display_furniture())
print(table1.name, table1.ttype)
print(*Table.__dict__, sep="\n")