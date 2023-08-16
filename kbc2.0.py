print("\n \n **************** Welcome to KAUN BANEGA CROREPATI **************")
print("\n")
print("Rules of the GAME-> \n There are 3 levels of the game. Rs 1000, Rs. 320000, Rs. 10000000 \n If you give wrong answer to a question you will take home the amount which you won in the previous level. \n If you want to take home the money you have earned then you can quit the game. \n")


       
count = 0
questions = [
    ["When is the yoga day?", "21 June", "14 Nov", "3 Oct", "31 Dec", 1],
    ["When was Chandrayan 3 launched?", "14 July 2023", "2 July 2023", "28 June 2023", "12 May 2022", 1 ],
    ["इनमें से किस बीमारी को 'दिमागी बुखार' के नाम से भी जाना जाता है ?","टेटनस", "जापानी इन्सेफेलाइटिस", "डेंगू","रेबीज़", 2]
]

levels = [1000,2000,3000,5000,10000,20000]
money =0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f" \n -> Question for Rs. {levels[i]} \n {question[0]}")
    print(f"\na. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")

    reply = int(input("Enter your answer 1-4 or press 0 to quit \n"))
    
    if reply==0:
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}") 
        
        if(i==0):
            money =1000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000

    else:
        print("Wrong answer")       
print("Need to add more questions")
print(f"\nThanks For playing this game ! \n Total money you take home is {money}")