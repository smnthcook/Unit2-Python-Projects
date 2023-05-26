'''
Quiz bowl
Samantha Cook
4/5/2023
Python II
'''


questions = ['What is the longest river in the US? ',
             'What is the clinical name for the thigh bone?',
             'What is the prefix in the word \"unnecessary\"',
             'Between 1 and 100, how many multiples of 7 are odd numbers? ',
             'Who painted the Mona Lisa? ',
             'Who was the first American in space? ',
             'Maine borders which US state? ',
             'How many inches are in two yards? ',
             'What is the smallest fish in the world? ',
             'Whose picture is on the five-dollar bill? ',]

answers = ['mississippi', 'femur', 'un', '7', 'DaVinci', 'alan shepard',
          'new hamshire', '72', 'paedocypris', 'abraham lincoln']

answers_correct = 0
for i in range(0, len(questions)):
    answer = input(questions[i])
    if answer == answers[i]:
        answers_correct += 1
        
print("You got", answers_correct, "answer(s) correct.")