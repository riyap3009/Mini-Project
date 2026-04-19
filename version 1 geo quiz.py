#version1  of geography quiz
import sys
AGE=13
#questions
quiz= {'What is the name of the longest river: ' :"Nile",
       'What is the largest ocean: ' :"Pacific Ocean ",
       'Who solved the 1854 cholera outbreak in London: ': "John Snow",
       'What is the capital of Croatia: ':"Zagreb ",
       'What country has the lowest population: ':"Vatican City",
       'Which country has the most time zones: ': "France",
       'Which country is opposite of New Zealand: ': "Spain",
       'What is the largest inland body of water: ' : "Caspian Sea",
       'What is the world’s largest island: ': "Greenland",
       
       }
#user details
name= input('Enter your name: ')
if name is None or name.strip ()== " ":
    sys.exit("No name entered. Exit Quiz")
age= int(input('Enter your age: '))

while True:
    if age < AGE:
        print("Your not eligible to take the quiz")
        sys.exit()
        break
    else:
        print('Start Quiz')
        break
for k,v in quiz.items():
    user_answer=input(f'{k}')
    if user_answer.strip().lower() == v.strip().lower():
        print('Correct')
    else:
        print("Incorrect")
