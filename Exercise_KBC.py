# Create a program capable of displaying questions to the user like kbc
# Use List data type to store the questions and their correct answers
# Display the final amount person is taking home after playing the game

def func1(AnsList):
    for ans in range(len(AnsList)):
        print(AnsList[ans])


#print("Kaun banega Winner")
#choice = input("If you want to play, press \'y' else 'n' : \n")
# if choice == 'y':
#     print("Lets Play")
# money = 0

Ans1 = [
    "A.	Tamil",

    "B.	Hindi",

    "C.	Malayalam",

    "D.	Telugu"]

Ans3 = ["A. Karnataka",

        "B. Kerala",

        "C.Tamil Nadu",

        "D.Andhra Pradesh"]

Ans2 = [
    "A.	Ujjain. Purl; Prayag. Haridwar",

    "B.	Prayag. Haridwar, Ujjain, Nasik",

    "C.  Rameshwaram. Purl, Badrinath. Dwarika",

    "D.	Chittakoot, Ujjain, Prayag,Haridwar"]
Questions = ["The language of Lakshadweep. a Union Territory of India, is ",
             "In which group of places the Kumbha Mela is held every twelve years? ", "Pongal is a popular festival of which state?"]

print("Kaun banega Winner")
choice = input("If you want to play, press \'y' else 'n' : \n")
if choice == 'y':
    print("Lets Play")
    money = 0
    for x in range(len(Questions)):

    # for ques in len(Questions):
    #     if(ques==0):
        if (x == 0):
            print("Question for Rs1000")
            print(Questions[x])

            func1(Ans1)
            x = input("Choose your option: ")
            if (x == "C"):
                print("You win : Rs1000")
                money = money+1000
            else:
                print("Wrong Answer")
                print(
                    "Sorry no lifeline, \n You need to start again!!! \n Thanks For playing")

                break

        if x == 1:
            print("Question for Rs5000")
            print(Questions[x])
            func1(Ans2)
            x = input("Choose your option: ")
            if (x == "B"):
                print("You win : Rs5000")
                money = money+5000
            else:
                print("Wrong Answer")
                print("Sorry no lifeline, \n You need to start again!!! \n Thanks For playing")

                break
        if x == 2:
            print("Question for Rs 10000")
            print(Questions[x])
            func1(Ans3)
            x = input("Choose your option: ")
            if (x == "C"):
                print("You win : Rs10000")
                money = money+10000
            else:
                print("Wrong Answer")
                print("Sorry no lifeline, \n You need to start again!!! \n Thanks For playing")

                break

        print(" Congratulations !!! You won")
        print("The total money you won is Rs", money)

else:
    print("Oops sorry to hear that, come back whenever you want to play.")
