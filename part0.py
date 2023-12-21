#input1 = int(input("Enter a course ID(i.e. CS0002, CS0004"))
# file = open('class_data.txt', 'r')
# if not input1 in file.read():
#     print("Cannot find this course")
# else:
#         data = file.readlines()
#         for line in data:
#             word = line.split()
#             for i in range(1):
#                 if str(input1)== word[i]:
#                     title = word[i+1]
#                     print("The title of this course is: " + title)
#         #class_data.close()  
                  
#         data_of_names = []
#         enrollement_file = open('enrollment_data.txt', 'r')
#         splitting_data = enrollement_file.split()
#         for line in splitting_data:
#             result = line.split()
#             for i in range(1):
#                 if result[i]==str(input1):
#                     data_of_names.append(len(result))  #mistake append from i+1 to len.
def get_course_data(course):
    course_data = []
    course_found = False
    course_title = ""

    # Open the file for reading
    with open('class_data.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Iterate through each line
        for line in lines:
            # Split the line into course number and course description
            line_parts = line.strip().split(',')

            # Extract course number and course description
            current_course_number = line_parts[0]
            current_course_description = line_parts[1]

            # Check if the course number matches the user input
            if current_course_number == course:
                course_data.append((current_course_number, current_course_description))
                course_found = True
                course_title = current_course_description  # Store the title for later access

    return course_data, course_found, course_title

# Ask the user for a course
user_course = input("Enter a course ID: ")

# Get data, course found status, and title for the specified course
course_data, course_found, course_title = get_course_data(user_course)

if course_found:
    #print(f"\nData for Course '{user_course}':")
    # for course_number, course_description in course_data:
    #     print(f"Course Number: {course_number}, Description: {course_description}")

    print(f"The Title of this course is: {course_title}")
else:
    print(f"Cannot find this course '{user_course}'.")
           
            
        
# def get_enrollment_data(course):
#     enrollment_data = ""

#     # Open the enrollment_data.txt file for reading
#     with open('enrollment_data.txt', 'r') as file:
#         enrollment_data = file.read()

#     return enrollment_data

# # Ask the user for a course
# user_course = input("Enter the course number: ")

# # Get enrollment data for the specified course
# enrollment_data = get_enrollment_data(user_course)

# if enrollment_data:
#     print(f"\nEnrollment data for Course '{user_course}':")
#     print(enrollment_data)
# else:
#     print(f"No enrollment data found for Course '{user_course}'.")
                
  
def get_enrolled_students(course):
    enrolled_students = []

    # Open the enrollment_data.txt file for reading
    with open('enrollment_data.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Iterate through each line
        for line in lines:
            # Split the line into course number, last name, and first name
            line_parts = line.strip().split(',')

            # Extract course number and student names
            current_course_number = line_parts[0]
            last_name = line_parts[1]
            first_name = line_parts[2]

            # Check if the course number matches the desired course
            if current_course_number == course:
                enrolled_students.append((last_name, first_name))

    return enrolled_students

# Ask the user for a course
#user_course = input("Enter the course number: ")

# Get enrolled students for the specified course
enrolled_students = get_enrolled_students(user_course)

if enrolled_students:
    print(f"Total number of students enrolled: {len(enrolled_students)}")
    #print(f"\nEnrolled Students for Course '{user_course}':")
    for last_name, first_name in enrolled_students:
        print(f"{last_name}, {first_name}")
    
else:
    print(f"No enrolled students found for Course '{user_course}'.")
    
