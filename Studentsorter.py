# Author: [Ryan Burger]
# File Name: studentsorter.py
# Description: This app accepts student names and GPAs, then checks if they qualify for the Dean's List or Honor Roll based on their GPA.

def main():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            print("Exiting the program.")
            break

        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))

        # Check for Dean's List qualification
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        
        # Check for Honor Roll qualification
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for Dean's List or Honor Roll.")

# Call the main function
if __name__ == "__main__":
    main()