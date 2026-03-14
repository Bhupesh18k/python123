# # 1. Write a Python function to create a table named employees with columns id (integer), name (text), age (integer), and department (text) in the test.db database.
import sqlite3
def create():
    connection= sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees
            (id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT)
            """)
    connection.commit()
    connection.close()
create()

# # 2. Insert at least 5 different employees into the employees table using a Python function “insert_employee()” and then calling it from outside.
# # Insert 5 different employees
# insert_employee(1, 'Alice', 30, 'HR')
# insert_employee(2, 'Bob', 25, 'Engineering')
# insert_employee(3, 'Charlie', 28, 'Sales')
# insert_employee(4, 'David', 35, 'Marketing')
# insert_employee(5, 'Eve', 22, 'HR')
def insert_employee(empid, name, age, department):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO employees (id, name, age, department) VALUES (?, ?, ?, ?)
    """, (empid, name, age, department))
    connection.commit()
    connection.close()
insert_employee(1, 'Alice', 30, 'HR')
insert_employee(2, 'Bob', 25, 'Engineering')
insert_employee(3, 'Charlie', 28, 'Sales')
insert_employee(4, 'David', 35, 'Marketing')
insert_employee(5, 'Eve', 22, 'HR')


# # 3. Write a Python function to update the department of employees with id ‘2’and ‘4’ into “Data Science”.
def update():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE employees
        SET department = 'Data Science'
        WHERE id IN (2, 4)
    """)
    connection.commit()
    connection.close()
update()

# # 4. Write a Python function to delete an employee from the employees table whose ID is ‘4’.
def delete(emp_id):
    connection= sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    connection.commit()
    connection.close()
delete(4)

# # 5. Write a Python function to fetch and display employees older than 25 years.
def fetch():
    connection=sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE age > 25")
    records = cursor.fetchall()
    for row in records:
        print(row)
    connection.close()
fetch()


# 6. Create an abstract base class Shape with encapsulated area attributes and an abstract area() method.
# a. Use inheritance for specific shapes like Circle (only need to pass radius) and Rectangle (need to pass both length and breadth).
# b. Extend Shape with a Triangle class using inheritance.
# Implement calculate_area() with base and height (0.5 * base * height).
# Create a triangle (base=10, height=5) and print its area. [Expected: 25.0]
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self):
        self._area = 0
    @abstractmethod
    def calculate_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def calculate_area(self):
        self._area = 3.14 * self.radius * self.radius
        return self._area
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        self._area = self.length * self.breadth
        return self._area
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    def calculate_area(self):
        self._area = 0.5 * self.base * self.height
        return self._area
triangle = Triangle(10, 5)
print(triangle.calculate_area())



# 7. Build a Vehicle abstract class with private fuel_capacity and fuel_consumption attributes. Subclasses Car and ElectricCar inherit and implement two functions:
# a) travel(self, distance)
# b) update_remaining_fuel(self).
# c) For Car, used_fuel = distance * self.consumption and self.fuel_capacity = max(0, self. fuel_capacity - used_fuel)
# d) For Electric_Car, used_fuel = distance * 0.2 and self.fuel_capacity = max(0, self. fuel_capacity - used_fuel)
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, fuel_capacity, fuel_consumption):
        self.__fuel_capacity = fuel_capacity      
        self.__fuel_consumption = fuel_consumption
    @abstractmethod
    def travel(self, distance):
        pass
    @abstractmethod
    def update_remaining_fuel(self):
        pass
    def get_fuel_capacity(self):
        return self.__fuel_capacity
    def set_fuel_capacity(self, value):
        self.__fuel_capacity = value
    def get_consumption(self):
        return self.__fuel_consumption
class Car(Vehicle):
    def travel(self, distance):
        used_fuel = distance * self.get_consumption()
        remaining = self.get_fuel_capacity() - used_fuel
        self.set_fuel_capacity(max(0, remaining))
    def update_remaining_fuel(self):
        return self.get_fuel_capacity()
class ElectricCar(Vehicle):
    def travel(self, distance):
        used_fuel = distance * 0.2
        remaining = self.get_fuel_capacity() - used_fuel
        self.set_fuel_capacity(max(0, remaining))
    def update_remaining_fuel(self):
        return self.get_fuel_capacity()
