def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
   
    for key in question :
        print("----------------")
        print(key)        
        for i in options[question_num-1] :
            print(i)
        guess = input ("ENTER A, B, C OR D :" ).upper()  
        guesses.append(guess)
         
        correct_guesses += check_answer(question.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)
#---------------------------
def check_answer(answers,guess) :
    
   if answers == guess:
        print("CORRECT")
        return 1
   elif answers != guess:
        print("WRONG")  
        return 0  
#---------------------------
def display_score(correct_guesses, guesses) :
    print("---------------------------")
    print("RESULT")
    print("---------------------------")
    
    print("ANSWERS :" , end="")
    for i in question :
        print(question.get(i), end=" ")
    print()   
    
    print("guesses : ", end = "")
    for i in guesses :
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(question))*100)
    print("Your Score Is: " + str(score)+"%")
    
#---------------------------
def play_again() :
    
    r = input("Do You Want To Play Again? (Yes or No): ")
    r = r.upper()
    if r == "YES":
        return True
    else :
        return False 

#---------------------------    

                               
question = {
"ARE YOU GAY ?": "A",    
"IS IT REALLY IMPORTANT TO BE HAPPY ?": "C", 
"IS LIFE MEANINGLESS ?": "D",
"IF YOU HAVE ONE CHANCE , ONE OPPORTUNITY TO SEES EVERYTHING YOU WANTED IN LIFE WOULD YOU TAKE IT ?": "D"
}


options = [["A. NO","B. -YES-","C. MAYBE","D. ASK YOUR MOM"],                                       ["A. NO","B. THERE IS NO SUCH THING AS HAPPINESS","C. YES","D. MAYBE"],      
                 ["A. MAYBE","B. LIFE HAS NO MEANING","C. SKIP","D. NO, BECAUSE WE LIVE TO SEE WHAT  LIFE HAS INSTORE FOR US "],
                 ["A. NO","B. WHAT OPPORTUNITY","C. SKIP","D. YES, I WOULD"]]           



new_game() 

while play_again() :
    new_game()
    
print ("Have A Nice Day")