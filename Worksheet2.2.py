#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:51:07 2024

@author: lamaalabdulwahab
"""

#Q1

# Define the users dictionary
users = {'Alice': '1234','Bob': 'pa55word','Charlie': 'Bananas','David': 'hacker123'}

# Define the list of not allowed passwords
not_allowed = ['1234', 'password', 'hello', 'let me in']

# Check each user's password against the not allowed list
for key in users:
    for i in range(0,3):
        if users.get(key) == not_allowed[i]:
            print(key, "your password is not allowed. Please change it.")


#Q2

# Initial list of subjects
subjects = ['maths', 'engineering', 'physics', 'computer science']

# Select the 2nd and 3rd elements from the list
print("The 2nd subject is:", subjects[1])
print("The 3rd subject is:", subjects[2])

# Prompt user to enter a new subject
newsubject = input("Enter a new subject: ")

# Insert the new subject just before the last element in the list
subjects.insert(-1, newsubject)
print("Updated subjects list:", subjects)

# Check if 'History' is in the list
if 'History' in subjects:
    print("History is in the list.")
else:
    print("History is not in the list.")
    

#Q3

# The list of numbers
num_list = [3, 9, 7, 2, 25, 50]

target = 486

used_nums = []

result = 50 * 9
used_nums.append(50)
used_nums.append(9)
print(f"Step 1: 50 * 9 = {result}")

result += 25
used_nums.append(25)
print(f"Step 2: + 25 = {result}")

result += 7*2
used_nums.append(7)
used_nums.append(2)
print(f"Step 3: + 7 * 2 = {result}")

result -= 3
used_nums.append(3)
print(f"Step 4: - 3 = {result}")

# Check if we have reached the target
if result == target:
    print("Congratulations! You've reached the target:", result)
else:
    print("Oops! You didn't reach the target. Final result:", result)

# Display the used numbers
print("Numbers used in the operations:", used_nums)



#EXAM STYLE

#Q1

# List of people names
people_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  

# List of pets corresponding to the people in people_names
pets = ['Dog', 'Lizard', 'Fish', 'Bird', 'Cat']  

# pair each person with their pet and converting the pairs into a dictionary
pet_dict = dict(zip(people_names, pets))  

# Asking the user to input a name
user_input = input("Please enter a name: ")  

# Checking if the entered name exists in the people_names list
if user_input in people_names:
    # If the name exists, create a response with the person's name and their corresponding pet from the dictionary
    response = user_input + " has a pet " + pet_dict[user_input]  
else:
    # If the name doesn't exist in the list, show an error message
    response = "Sorry, information on that person’s pets is not available."  

# Print the final response to the user
print(response)  



#Q3


# Initial data structure
students = {
    'Alice': {
        'Subjects': {
            'Maths': 60,
            'Computer Science': 70,
            'English': 65,
        }
    }
}

# Name of the new person
new_person_name = 'Bob'

# Copying the structure and data of Alice for the new person
new_person_data = {
    'Subjects': {
        'Maths': 60,
        'Computer Science': 70,
        'English': 65,
    }
}

# Adding the new person to the dictionary
students[new_person_name] = new_person_data

# Printing the updated data structure
print(students)



