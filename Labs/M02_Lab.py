'''
M02_Lab.py
Created by: Julian Payne
This program will initialize a Students object and allow the user to 
input name's and GPA's of students until they enter a sentinel value in the 
form of ZZZ. Upon entering the sentinel value, the program will then check 
each student's GPA to determine which have made the Dean's list and which have 
made Honor Roll. It will then output the names of these students. 

self.students = dictionary that stores student information in the form of key-value pairs
quit = string variable that stores the sentinel value ZZZ
data = string representation of the data stored in the class object
last = string variable that prompts user for last name 
first = string variable that prompts user for first name
gpa = float variable that prompts user for GPA
SEE HERE
'''


class Students:
    quit = "ZZZ"

    def __init__(self):
        '''
        Initializes the Student object with an empty dictionary of students and
        calls instance methods
        '''

        self.students = {}
        self.add_students()
        self.get_deans_list()
        self.get_honor_roll()

    def __str__(self):
        '''
        Returns a string representation of the Students object
        '''

        data = ""
        for student in self.students:
            data += f"Name: {student}\nGPA: {self.students[student]}\n"
        return data

    def add_students(self):
        '''
        Accepts user input and updates the class dictionary with the new
        values
        '''

        last = input("Enter a student's last name: ").strip()
        while last != "ZZZ":
            first = input("Enter a student's first name: ").strip()
            name = first + " " + last
            gpa = float(input("Enter the student's GPA: "))
            self.students.update({name : gpa})
            last = input("Enter a student's last name or ZZZ to quit: ").strip()

    def get_deans_list(self):
        '''
        Checks each value in the students dictionary to see if the GPA value is
        greater than or equal to 3.5
        '''

        for student in self.students:
            if self.students[student] >= 3.5:
                print(f"{student} made the Dean's list")

    def get_honor_roll(self):
        '''
        Checks each value in the students dictionary to see if the GPA value is
        greater than or equal to 3.25
        '''

        for student in self.students:
            if self.students[student] >= 3.25:
                print(f"{student} made Honor Roll")

    

def main():
    Students()

if __name__ == "__main__":
    main()