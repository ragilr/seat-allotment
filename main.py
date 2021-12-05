
from enum import Enum
from typing import List

# Enum order should be same as CSV column order
class Values(Enum):
	TIMESTAMP = 0
	NAME = 1
	ROLLNUMBER = 2
	CGPA = 3
	PREFERENCE = 4    # Preference starting index


seats = [1,1,1,1]                       # Number of seats in each project
total_preferences = 5                   # Number of preferences read from each student

# Function to read all lines from the CSV
def read_input_CSV(filename:str) -> List[List[str]]:
    student_response = []
    with open(filename) as file:
        next(file)                                          # skip first line of CSV
        for line in file:
            stripped_line = line.strip()
            if not stripped_line == None:
                student_response.append(stripped_line.split(','))
    return student_response

# Function to sort the student list based on their CGPA
def sort_student_on_CGPA(students:List[List[str]]) -> List[List[str]]:
    return sorted(students, key=lambda x: -float(x[Values.CGPA.value]))

# Function to validate inputs
def validate_inputs(students:List[List[str]])-> None:
    # TODO : Add more validations
    # add validation for T 1 T2 format
    num_of_students = len(students)
    if sum(seats) < num_of_students:
        raise Exception("Number of seats are less than the number of students")

# Function to allocate students to each project
def allocate_seats(students:List[List[str]]):
    seat_allocation = []
    for student in students:
        is_student_allocated_seat = False
        preference_index = Values.PREFERENCE.value
        # Allocating seat for each student
        while not is_student_allocated_seat:
            # Following line will break if the preference is not in the format T 1,T 2..,T 10etc.
            student_preference = int(student[preference_index].split(' ')[1])
            if(seats[student_preference-1] > 0):    # seat available
                seats[student_preference-1] -= 1
                allocated_seat = [student[Values.ROLLNUMBER.value],student[Values.NAME.value],student[preference_index]]
                seat_allocation.append(allocated_seat)
                is_student_allocated_seat = True            
            preference_index += 1
    return seat_allocation

# Main
def main():
    student_response = read_input_CSV("Pref_Topic.csv")    # TODO : read file name from args
    validate_inputs(student_response)
    students = sort_student_on_CGPA(student_response)
    seat_allocation = allocate_seats(students)
    print(seat_allocation)
    # TODO : Publish results into a CSV
    


if __name__ == "__main__":
    main()