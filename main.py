#Amore' Daniels

import random

#creating capitals dictionary
state_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
                  'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                  'California': 'Sacramento', 'Colorado': 'Denver',
                  'Connecticut': 'Hartford', 'Delaware': 'Dover',
                  'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
                  'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                  'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
                  'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                  'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
                  'Maine': 'Augusta', 'Maryland': 'Annapolis',
                  'Massachusetts': 'Boston', 'Michigan': 'Lansing',
                  'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
                  'Missouri': 'Jefferson City', 'Montana': 'Helena',
                  'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
                  'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                  'New Mexico': 'Santa Fe', 'New York': 'Albany',
                  'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
                  'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                  'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                  'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                  'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
                  'Texas': 'Austin', 'Utah': 'Salt Lake City',
                  'Vermont': 'Montpelier', 'Virginia': 'Richmond',
                  'Washington': 'Olympia', 'West Virginia': 'Charleston',
                  'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#initialize variables
answer = ''
attempts = 0
accuracy = 100.00
#keep a count of correct answers
correctAnswers = 0

#quiz the user with a random state
while answer != 'Quit':
    #count the number of tries
    attempts += 1
    #print('attempts:',attempts)
    state = random.choice(list(state_capitals))
    question = 'What is the capital of '+state+'? '
    #title function to capitalize first letter of every word
    #this will prevent errors for certain capitals that are 
    #more than one word
    answer = input(question).title()
    #print('answer:',answer)
    #get the value/capital of given state
    capital = state_capitals.get(state,'Wrong')
    #print('capital:',capital)

    #if the answer and the capital are the same
    if answer ==  capital:
        print('Correct response')
        #add one to counter
        correctAnswers += 1
        #print('# of correct answers:',correctAnswers)
        #calculate accuracy
        accuracy = (correctAnswers/attempts) * 100
        #accuracy should be printed each time
        #format specifier for 2 decimal places
        print('Your accuracy is %0.2f%%' % (accuracy))

    #if answer is not equal to the value/capital of state 
    if (answer != capital) and (answer != 'Quit'):
        print('Incorrect response')
        #calculate accuracy
        accuracy = (correctAnswers/attempts) * 100
        #accuracy should be printed each time
        #format specifier for 2 decimal places
        print('Your accuracy is %0.2f%%' % (accuracy))
    
#stop when the user says quit and print results
if answer == 'Quit':
    #accuracy should be printed each time
    #format specifier for 2 decimal places
    print('Your accuracy is %0.2f%%' % (accuracy))