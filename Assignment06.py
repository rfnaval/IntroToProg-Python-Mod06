# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using classes and functions
# with structured error handling and SoC
# Change Log: (Who, When, What)
#   Renato Felicio,11/16/2024,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #

# Import section
import json
from typing import TextIO

# Global Data Layer

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants

FILE_NAME: str = "Enrollments.json" # Constant holds the name of the file with students data

# Define the Data Variables and constants
students: list=[] # This variable holds the information of all registered students.
menu_choice: str=''  # It holds the user choice.

# Class definition

# Processing Data Layer
class FileProcessor:
    """
        A collection of processing layer functions that work with json files

        ChangeLog: (Who, When, What)
        Renato Felicio,11/16/2024,Created Class
        """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

            Notes:
            - Data sent to the student_data parameter will be overwritten.

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :param file_name: string with the name of the file we are reading
            :param student_data: list of dictionary rows we are adding data to
            :return: list of dictionary rows filled with data
        """
        try:
            file: TextIO = open(file_name, "r")  # Open the JSON file for reading
            student_data: list = json.load(file) # File data is loaded into a table
            # Now 'student_data' contains the parsed JSON data as a Python list of dictionaries
            file.close()
        except FileNotFoundError as e:  # Handles error in case there is no initial file
            IO.output_error_messages("Data file must exist before running this script!")
            file = open(FILE_NAME, "w")  # Creates an empty initial file, in case of file not found
            IO.output_error_messages("Empty file was created!\n")
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file from a list of dictionary rows

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :param file_name: string with the name of the file we are writing to
            :param student_data: list of dictionary rows containing our data
            :return: None
        """
        try:
            file: TextIO = open(file_name, "w")
            json.dump(student_data, file)  # It writes the list of dictionaries into a json file
            file.close()
        except Exception as e: # It handles any exception that could happen when writing the file
            if file.closed == False:
                file.close()
                IO.output_error_messages("There was a problem with writing to the file.", e)
                IO.output_error_messages("Please check that the file is not open by another program.", e)
                print()
# End of Processing Data Layer

# Presentation Data Layer

class IO:
    """A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        Renato Felicio,11/16/2024,Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :return: string with the users choice
        """
        choice="0"
        try:
            choice: str = input("What would you like to do: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
               raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the current data to the user

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets data from the user and adds it to a list of dictionary rows

            ChangeLog: (Who, When, What)
            Renato Felicio,11/16/2024,Created function

            :param student_data: list of dictionary rows containing our current data
            :return: list of dictionary rows filled with a new row of data
        """
        try:
            student_first_name: str = input("Enter the student's first name: ") # Holds student first name input
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.") # Custom error
            student_last_name: str = input("Enter the student's last name: ") # Holds student last name input
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.") # Custom error
            course_name: str = input("Please enter the name of the course: ") # Holds course name input
            student: dict = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.",e)
        return student_data

# End of Presentation Data Layer

# End of class definition

# Start of the main body of the script

# Read data from a file
students:list = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while (True): # Loops through the menu of options
    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice=IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students=IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        IO.output_student_courses(students)
        continue

    # Save the data to a file and present to user
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,students)
        IO.output_student_courses(students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

