#--------------------------
def new_game():
    
    guesses = [] #empty list
    correct_guesses = 0 #the score
    question_num = 1 #counter
    
    for key in questions: #print out everything in the "questions" libaray
        print("----------------------") #line break
        print(key)
        for i in options[question_num-1]: #display all the options for each question - nested for loop
            print(i)    #                - giving options a index of "question_num-1"  ------  #prints the first index of the "options list" which shows all the options for question 1
        guess = input("Enter (A, B, C, or D): ")  
        guess = guess.upper()   #cacpitalizes the user input   
        guesses.append(guess)   #adds a number to our empty "guesses list"                   
        
        #               this will return either 0 or 1 and that will add onto "correct_guesses"
        correct_guesses += check_answer(questions.get(key),guess) #get the correct answer(argument) from the "questions" dictionary, takes another argument which is the "guess" value
        question_num += 1                #this adds onto the index by 1 so during the next loop it will print the second index in "options"
        
    display_score(correct_guesses, guesses)  #print out the value of correct_guesses and # of guesses at the end
        
#--------------------------
def check_answer(answer, guess): 
    
    if answer == guess:  #if the value of the "answer" and guess is the same
        print("CORRECT!")   #print out correct
        return 1 #return one point
    else:
        print("WRONG!")
        return 0 #return 0 points
#--------------------------
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS")
    print("----------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ") #print the answer in the questions libaray
    print()
    
    print("Guesses: ", end="") #print all the values you guessed
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100) #display final score - int cast
    print("Your score is: "+str(score)+"%") 
    
    
#--------------------------
def play_again():
    
    response = input("Do you want to play agian? (yes or no) ")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False
#----------------------------------------------------------------------

questions = {                              #dictionary 
    "Who created Python?: ": "A",                #question,correct answer
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

#2D list
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game() #call new game fucntion

while play_again(): #will return true or false depending on user response
    new_game() #a new game will be run
    
print("Byeeee!") #will print after while loop ends
    







