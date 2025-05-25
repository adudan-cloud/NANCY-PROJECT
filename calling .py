from functions import countdown, clear_list, print_square, update_dict
if __name__ == "__main__":


    # Call the countdown function
    countdown(5)
    
    # Create a list and clear it
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    clear_list(my_list)
    print("Cleared list:", my_list)
    
    # Print the square of a number
    print_square(4)
    
    # Update a dictionary
    my_dict = {'a': 1, 'b': 2}
    print("Original dictionary:", my_dict)
    update_dict(my_dict, 'c', 3)
    print("Updated dictionary:", my_dict)

from classes import Car, Dog, Student

# create instances of each class
car = Car("Toyota", "Corolla")
print(car.display_info())
car.change_wheels_count(6)

dog = Dog("Buddy", 3, "golden retriever")
print(dog.bark())
print(Dog.get_species())

student = Student("NANCY", 10)
print(student.get_info())
print(student.change_school("kiti high school"))
print(student.get_info())