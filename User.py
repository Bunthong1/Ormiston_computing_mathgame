# The Ormiston Computing Program : 24 / 06 / 20 , Thong
# This Program is created to help the junior student with their math on  ( addition and multiplication )
# User V9 : Fix the answer error handling 

#this code import the random module
import random

#create a class named user
class User :

    # create an initial function which store user name, year ,level and topic
    def __init__(self, user, year, level, topic):

        #set all teh variable as global
        self.user = user
        self.year = year
        self.level = level
        self.topic = topic

    # create a question generate function
    def question(self):

        #when the user choose "easy"
        if self.level == "Easy":
            #set the number list from 1 to 5
            num = [1,2,3,4,5]

        #when the user choose "medium"
        elif self.level == "Medium":
            #set the number list from 6 to 10
            num = [6,7,8,9,10]

        #when the user choose "hard"
        elif self.level == "Hard":
            #set the number list from 11 to 15
            num = [11,12,13,14,15]

        #generate 2 random nuber from the number list
        number_choice1 = random.choice(num)
        number_choice2 = random.choice(num)

        #generate the answer according to the topic ( addition or multiplication )
        if self.topic == "Addition" :
            self.answer = number_choice1 + number_choice2

        else :
            self.answer = number_choice1 * number_choice2

        #return the 2 random number to the GUI class
        return(number_choice1, number_choice2)

    #create an answer checking function
    def canswer(self,answerentry):

        #set valid to false
        valid = False
        
        while not valid:
            try :
                #check the answerinput with the actual answer from the computer
                #return the result back to GUI class
                if self.answer == int(answerentry):
                    return "correct"
                else:
                    return "wrong"
            except ValueError:
                return "error"
                break

    #create a function which write teh final data to a txt file
    def transfer_detail(self,Point):
       try:
            #open the file
            with open('quizdata.txt', 'a') as data:

                #write all teh data to that file
                data.write("\n\nUsername : {}".format(self.user))
                data.write("\nYear : {}".format(self.year))
                data.write("\nTopic : {}".format(self.topic))
                data.write("\nLevel: {}".format(self.level))
                data.write("\nPoint : {}".format(Point))
                return True

       except:
            return False
        
