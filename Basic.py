# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade  
     
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def get_average_grade(self):
#         total = 0
#         for student in self.students:
#             total += student.get_grade()
#         return total / len(self.students)

    

# student1 = Student("Tim", 19, 95)
# student2 = Student("Bill", 19, 75)
# student3 = Student("Jill", 19, 65)
# student4 = Student("Jack", 19, 85)
# course1 = Course("Big Data", 3)

# course1.add_student([student1, student2, student3, student4])


# print(course1.get_average_grade())

        


class Product:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name
    def get_product(self):
        return self.quantity
    
    def get_price(self):
        return self.price
class Store:
    def __init__(self, name, max_products):
        self.name = name
        self.max_products = max_products
        self.products = []

    def add_products(self, product):
        if len(self.products) < self.max_products:
            self.products.append(product)
            return True
        return False
    
    
    def calculate_total_value(self):
        total = 0
        for value in self.products:
            total += value.get_price() * value.get_product()
        return total

    def get_avg_price(self):
        total_price = 0
        for price in self.products:
            total_price += price.get_product()
        return total_price/len(self.products)
    
    # def get_products(self):
    #     product = []
    #     for i in self.products:
    #         print("Product Name" + product[i].name)
    #         product[i] +=1

            
print("Cricket Inventory")
p1 = Product("Bat",300,10)
p2 = Product("Bowl",100, 30)
p3 = Product("Stumps",500,15)
store = Store("Champions",3)
store.add_products(p1)
store.add_products(p2)
print(store.add_products(p3))
print(store.get_avg_price())

print(store.calculate_total_value())

# print(store.get_products())

        

        