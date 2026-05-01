class Student: #Class Student

    #__init__ constructor is used to do initializing
    def __init__(self, name, age, roll_number, phone_number):
        self.name = name #assigning value to the data-member name
        self.age = age
        self.roll = roll_number  #
        self.phone = phone_number

    def display_details(self):
        print("\nName : ", self.name)
        #the object name is now intsantiated (created) ~ the __init__ runs for self.name
        print("Age : ", self.age)
        print("Roll Number : ", self.roll)
        print("Phone Number : ", self.phone)

# Creating an instance of the Student class
student1 = Student("Chandana Raghunath", 20, "B18", "9481247719")
student2 = Student("Kaveri Bairisetti", 19, "B16", "8073324684")

# Calling the display_details method to display the student's details
student1.display_details()
student2.display_details()
