
#----------------------------------------------------------------------------------------------------------------------------------------|
#----------------------------------------------------Joshua Fritts-----------------------------------------------------------------------|
#----------------------------------------------------M02-Lab.py--------------------------------------------------------------------------|
#----------------------------------------------------------------------------------------------------------------------------------------|
#This Python program serves as a student record management tool. It allows the user to input student information, including last name,---|
# first name, and GPA, and provides options to display qualifications, count entered students, and either quit or re-run the program. ---|
#----------------------------------------------------------------------------------------------------------------------------------------|



import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

# Welcome Prompt
print("To begin, follow prompts, Last Name then First Name, finally the GPA of the student. Enter 'zzz' to quit or 'rrr' to display results: ")

# Time-based Delay
print("Press Enter to start the program, or wait for 20 seconds for an automatic start...")
start_time = time.time()

while True:
    if input() == '' or time.time() - start_time >= 20:
        break

# Clear the screen for readability
os.system('cls' if os.name == 'nt' else 'clear')

# Initialize empty lists to store student names and GPAs
student_names = []
student_GPAs = []

# Function to check if a student qualifies for Dean's List or Honor Roll
def check_qualification(GPA):
    if GPA >= 3.5:
        return "Dean's List"
    elif GPA >= 3.25:
        return "Honor Roll"
    else:
        return "Not qualified"

# Initialize a counter for students entered
student_count = 0

# Input loop
while True:
    # Display the total number of students entered
    print(f"Total students entered: {student_count}")

    # Ask for the student's last name
    last_name = input("|zzz to quit|rrr to run program| Enter the student's last name: ")

    # Check if the user wants to quit or display results
    if last_name.lower() == 'zzz':
        break
    elif last_name.lower() == 'rrr':
        # Clear the screen for readability
        os.system('clear' if os.name == 'posix' else 'cls')
        # Display qualifications
        for i in range(len(student_names)):
            first_name, last_name = student_names[i]
            GPA = student_GPAs[i]
            qualification = check_qualification(GPA)
            
            print(f"{first_name} {last_name} has a GPA of {GPA} and is on the {qualification}.")

        # Display the total number of students entered
        print(f"Total students entered: {student_count}")

        # After displaying qualifications and the count, provide the option to quit or re-run
        while True:
            option = input("Enter 'q' to quit or 'r' to re-run the program: ")
            if option.lower() == 'q':
                exit()  # Quit the program
            elif option.lower() == 'r':
                student_names.clear()
                student_GPAs.clear()
                student_count = 0  # Reset the student count
                break  # Re-run the program
    else:
        # Ask for the student's first name
        first_name = input("Enter the student's first name: ")

        # Ask for the student's GPA as a float
        try:
            GPA = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid GPA input. Please enter a valid number.")
            continue

        # Increment the student count
        student_count += 1

        # Clear the screen for readability after entering GPA
        os.system('cls' if os.name == 'nt' else 'clear')

        # Append the student's name and GPA to the respective lists
        student_names.append((first_name, last_name))
        student_GPAs.append(GPA)
