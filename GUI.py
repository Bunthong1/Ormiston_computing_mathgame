# The Ormiston Computing Program : 24 / 06 / 20 , Thong
# This Program is created to help the junior student with their math on ( addition and multiplication )
# User V18 : Fix the answer error handling 


# These command import other class that require for GUI like User class and Everythig from tkinter
# * means everything in Tkinter
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from User import User

class window_one:

    # This is the initial function which is just start of the the info frame and set notvalid to false 
    def __init__(self):
        self.notvalid = False
        self.info()
    
    #This function include all the widgets that display in the GUI for info page
    def info(self):

        #Create the frame named frame1 in the main window
        self.frame1 = Frame(main_window)

        #Set the background colour of this frame to #00ffff
        self.frame1.config(bg ="#00ffff")
        self.frame1.grid()

        #Display the name of the program and command for the user to follow
        Label(self.frame1, text="Ormiston Computing",bg ="#00ffff", font= ('arial', 17, 'bold')).grid(row=0, columnspan= 2, pady=10)
        Label(self.frame1,bg ="#00ffff", text="Please enter your name and year level :", font= ('arial', 13)).grid(row=1, column=0, pady = 5, columnspan= 2)

        #Create a input box for teh user to enter their name
        Label(self.frame1, text="Name :",bg ="#00ffff",font= ('arial', 13, 'bold')).grid(row=2, column=0, padx = 60, pady = 5)
        self.user = Entry(self.frame1, bd = 1,bg ="white", width = 15, borderwidth = 0)
        self.user.grid(row=2, column=1, pady = 5, padx= 15)

        #Create a input box for the user to enter their year level
        Label(self.frame1, text="Year :",bg ="#00ffff",font= ('arial', 13, 'bold')).grid(row=3, column=0, padx = 60, pady = 5)
        self.year = Entry(self.frame1, bd = 1,bg ="white", width = 15, borderwidth = 0)
        self.year.grid(row=3, column=1, pady = 5, padx= 15)

        #Create quit button which allow the user to get out from the program
        Button(self.frame1,text="Quit", bg='red',fg='black',font= ('arial', 13, 'bold'), command = self.quit).grid(row=4, column=0, pady = 15)

        #Create Begin button which allow the user to go to the next page or continue the program
        Button(self.frame1,text="Begin",bg = "#abab0a",fg='black',font= ('arial', 13, 'bold'), command = self.home ).grid(row=4, column=1, pady = 15)

    #This function is create to destroy or delete the whole window
    def quit(self):
        #remove the entire window
        main_window.destroy()

    def home(self):

        #Checke the user input whether it in between the boundary or not
        if self.year.get() not in  ["8","9","10"]:
            self.notvalid = True
            #show a error message to let user know the boundary of teh year input
            messagebox.showerror("Error", "Please only input 8, 9 ,10 in student year level")
            
        else:
            
            #Remove the previous frame 
            self.frame1.grid_remove()
        
            #Create the frame named frame2 in the main window
            self.frame2 = Frame(main_window)

            #Set the background colour of this frame to #00ffff
            self.frame2.config(bg ="#00ffff")
            self.frame2.grid()

            #Display the name of the program
            Label(self.frame2, text="Ormiston Computing",bg ="#00ffff", font= ('arial', 17, 'bold')).grid(row=0, column= 0, pady=10, padx=80)

            #Create a button that allow the user to start the game or quit it
            Button(self.frame2,text="Start", bg='yellow',fg='black', width = 100 ,height = 40,font= ('arial', 13, 'bold'), command = self.topic).grid(row=1, column=0, pady = 10)
            Button(self.frame2,text="Quit", bg='Red',fg='black',font= ('arial', 13, 'bold'), command = self.quit).grid(row=2, column=0)

            #Create the button which help the user to understand the functionality of the program
            Button(self.frame2,text="help?", bg='#00ffff',fg='blue',underline = True, font= ('arial', 13, 'underline'), command = self.help).grid(row=3, column=0, pady = 15, sticky=W)

            #Display the name of the the developer that develop the program
            Label(self.frame2, text="Creator: Thong & Lia",bg ="#00ffff", font= ('arial', 13)).grid(row=3, column =0, sticky=E)


    def help(self):
        #Remove the previous frame 
        self.frame2.grid_remove()
        
        #Create the frame named frame3 in the main window
        self.frame3 = Frame(main_window)

        #Set the background colour of this frame to #00ffff
        self.frame3.config(bg ="#00ffff")
        self.frame3.grid()

        #Display the title of the page
        Label(self.frame3, text="  Instruction :",bg ="#00ffff", font= ('arial', 17, 'bold')).grid(row=0, column= 0, pady=10, sticky=W)

        #Create a button the allow the user go back to home page
        Button(self.frame3,text="Home", bg="#abab0a",fg='black', font= ('arial', 13, 'bold'), command = self.backhome).grid(row=0, column=1, pady = 10)

        #Display the instruction of the program
        Label(self.frame3, text="  By simply select the right answer to \nthe question. Then, it will lead you \nanother question. Example Below :",bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=1, column= 0, pady=10, sticky=W)
        Label(self.frame3, text=" \t\t   2 + 4 = ?",bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=2, column= 0, pady=10, sticky=W)
        Label(self.frame3, text="              Answer : ",bg="#00ffff", font= ('arial', 13, 'bold')).grid(row=3, column= 0, sticky=W)
        Label(self.frame3, text="      6     ",bg="white", font= ('arial', 13, 'bold')).grid(row=3, columnspan = 2, pady = 5)

    
    def topic(self):

        #Remove the previous frame 
        self.frame2.grid_remove()
        
        #Create the frame named frame4 in the main window
        self.frame4 = Frame(main_window)

        #Set the background colour of this frame to #00ffff
        self.frame4.config(bg ="#00ffff")
        self.frame4.grid()
        
        #Display a hello statement with user name
        display = Label(self.frame4, bg ="#00ffff", text="Hello, " + self.user.get(), font= ('arial', 17, 'bold')).grid(row=0, column=0, pady = 5)

        #Asks user to choose a topic to practise on 
        Label(self.frame4, text="     Which topic would you like to practice ?     ",bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=1, column= 0, pady=10)
        
        #Create 2 different buttons for the user to choose on fro practise
        Button(self.frame4,text="Addition [+]", bg='yellow',width = 150, height = 30,fg='black',font= ('arial', 13, 'bold'), command = lambda:self.level("Addition")).grid(row=2, column=0, pady=10)
        Button(self.frame4,text="Multiplication [x]", bg='yellow',width =150, height = 30,fg='black',font= ('arial', 13, 'bold'), command = lambda:self.level("Multiplication")).grid(row=3, column=0, pady=10)

    def level(self, text):

        #Remove the previous frame 
        self.frame4.grid_remove()

        #Create the frame named frame7 in the main window ( in Advance )
        self.frame7 = Frame(main_window)
        #Set the background colour of this frame to #00ffff
        self.frame7.config(bg ="#abab0a")
        
        #Create the frame named frame5 in the main window
        self.frame5 = Frame(main_window)

        #Set the background colour of this frame to #00ffff
        self.frame5.config(bg ="#00ffff")
        self.frame5.grid()

        #Set point to 0 and question to 1
        #For calculate the point and total question
        self.point = 0
        self.question = 1

        #check which button the user click on
        if text == "Addition":
            #define the topic name to "addition"
            self.topic1= "Addition"
        else :
            #define the topic name to "multiplication"
            self.topic1= "Multiplication"

        #Display the topic according to the button the user click
        Label(self.frame5, bg ="#00ffff", text="{}".format(text), font= ('arial', 17, 'bold')).grid(row=0, column=0, pady = 5, padx = 150)

        #Ask teh user to choose how hard they want the question be
        Label(self.frame5, text="Choose a level :",bg ="#00ffff", font= ('arial', 13)).grid(row=1, column= 0, pady=10)

        #create 3 differnt button for 3 different level
        Button(self.frame5,text="Easy", bg='yellow',width = 150, height = 30,fg='black',font= ('arial', 13, 'bold'), command = lambda:self.levelquestion("Easy")).grid(row=2, column=0, pady=5)
        Button(self.frame5,text="Medium", bg='yellow',width =150, height = 30,fg='black',font= ('arial', 13, 'bold'), command = lambda:self.levelquestion("Medium")).grid(row=3, column=0, pady=5)
        Button(self.frame5,text="Hard", bg='yellow',width = 150, height = 30,fg='black',font= ('arial', 13, 'bold'), command = lambda:self.levelquestion("Hard")).grid(row=4, column=0, pady=5)

    def levelquestion(self, text):

        #Remove the previous frame
        self.frame5.grid_remove()

        #Remove the previous frame
        self.frame7.grid_remove()
        
        #Create the frame named frame6  in the main window
        self.frame6 = Frame(main_window)

        #Set the background colour of this frame to #00ffff
        self.frame6.config(bg ="#00ffff")
        self.frame6.grid()

        # Transfer the 4 values ( user, year, level, topic) to the User class
        self.user1 = User(self.user.get(), self.year.get(), text, self.topic1)

        #Fetch the 2 number which generate from user class according to the level that the user choose
        self.int1, self.int2 = self.user1.question()

        #defien level teh user choose to self.level1
        self.level1 = text
        
        #Display the level of the question and point the user get
        Label(self.frame6, text="Level : " + text,bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=0, column= 0, pady=5, sticky = W)
        Label(self.frame6, text="{}{}".format("Point : ", self.point),bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=1, column= 0, sticky = W)

        #Create the button that allow the user to go back to home frame
        Button(self.frame6,text="Home", bg="#abab0a",fg='black', font= ('arial', 13, 'bold'), command = self.backhome1).grid(row=0, column=2, pady = 10)

        #Display the question number that user answering
        Label(self.frame6, text="{}{}".format("Question : ", self.question),bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=3, column= 1)

        #display the question according to the topic 
        if self.topic1 =="Addition" :
            Label(self.frame6, text = "{}{}{}".format(self.int1, "  +  " ,self.int2), bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=4, column= 1, pady=5)

        else :
            Label(self.frame6, text = "{}{}{}".format(self.int1, "  x  " ,self.int2), bg ="#00ffff", font= ('arial', 13, 'bold')).grid(row=4, column= 1, pady=5)

        #Create the Input box which allow the user to input the answer 
        self.answerentry = Entry(self.frame6, bd = 1,bg ="white", width = 15, borderwidth = 0)
        self.answerentry.grid(row=5, column=1, pady = 5, padx= 15)

        #Create a button which allow the user to submit the answer
        Button(self.frame6,text="Submit", bg="yellow",fg='black', font= ('arial', 13, 'bold'), command = self.Submit).grid(row=6, column=1, pady = 10)


    def Submit(self):

        #senf teh user answernetry to User class for checking 
        self.user1.canswer(self.answerentry.get())

        # Fetch the result back from User class
        result = self.user1.canswer(self.answerentry.get())

        #check when the result is correct 
        if result == "correct":

            # check when the question is below 10
            if self.question <= 9 :

                # add 1 to the point and question
                self.point = self.point + 1
                self.question = self.question + 1
                
                #Remove the previous frame 
                self.frame6.grid_remove()
                self.frame7.grid()

                #Display the question number that user answering
                Label(self.frame7, text="Correct",bg ="#abab0a", font= ('arial', 15, 'bold')).grid(row=0, column= 0, pady =10)
                if self.topic1 == "Addition":
                    Label(self.frame7, text = "{}{}{}{}{}".format(self.int1, "  +  " ,self.int2, "  =  ",self.answerentry.get()), bg ="#abab0a", font= ('arial', 13, 'bold')).grid(row=1, column= 0, pady=5, padx = 150)
                else :
                    Label(self.frame7, text = "{}{}{}{}{}".format(self.int1, "  x  " ,self.int2, "  =  ",self.answerentry.get()), bg ="#abab0a", font= ('arial', 13, 'bold')).grid(row=1, column= 0, pady=5, padx = 150)

                #Display the point user got
                Label(self.frame7, text = "{}{}".format(" Points  =  ", self.point), bg ="#abab0a", font= ('arial', 13, 'bold')).grid(row=2, column= 0, pady=5)

                #Create a button which allow the user to submit the answer
                Button(self.frame7,text="Next", bg="yellow",fg='black', font= ('arial', 13, 'bold'), command = lambda: self.levelquestion(self.level1)).grid(row=3, column=0, pady = 10)



            # check when the question reach 10
            elif self.question == 10 :

                        self.point = self.point + 1
                        
                        #Remove the previous frame 
                        self.frame6.grid_remove()

                        #Create the frame named frame8 in the main window
                        self.frame8 = Frame(main_window)

                        #Set the background colour of this frame to #00ffff
                        self.frame8.config(bg ="#00ffff")
                        self.frame8.grid()

                        #Display the title of the page
                        Label(self.frame8, text="  Congratulation  ",bg ="#00ffff", fg = "red", font= ('arial', 15, 'bold')).grid(row=1, column= 0, padx =10)
                        #Display the title of the page
                        Label(self.frame8, text="Total question :10 \n Correct : 10", bg="#abab0a",width = 30,height = 4, font= ('arial', 13, 'bold')).grid(row=2, column= 0, pady=15, padx =40)

                        #Create a button the allow the user go back to home page
                        Button(self.frame8,text="Home", bg="#abab0a",fg='black', font= ('arial', 13, 'bold'), command = self.backhome3).grid(row=0, column=0, pady=5, columnspan = 2,sticky = E)

                        #Create a button the allow the user to quit the program
                        Button(self.frame8,text="Quit", bg="red",fg='black', font= ('arial', 13, 'bold'), command = self.quit).grid(row=3, column=0,columnspan =2, pady=5, sticky = W, padx =30)

                        #Create a button the allow the user to practise more
                        Button(self.frame8,text="Next", bg="yellow",fg='black', font= ('arial', 13, 'bold'), command = self.backtopic2).grid(row=3, column=0,sticky = E, pady=5, padx =30)
                        self.user1.transfer_detail(self.point,self.topic1)

                #cehck when the user's answer is wrong 
        if result == "wrong":

            #Remove the previous frame 
            self.frame6.grid_remove()
        
            #Create the frame named frame9 in the main window
            self.frame9 = Frame(main_window)

            #Set the background colour of this frame to #00ffff
            self.frame9.config(bg ="#00ffff")
            self.frame9.grid()

            #Display the result
            Label(self.frame9, text="  Game Over  ",bg ="#00ffff", fg = "red", font= ('arial', 15, 'bold')).grid(row=1, column= 0, padx =10)

            #Display the total point and question answered
            Label(self.frame9, text="Total question :{} \n Correct : {}".format(self.question, self.point), bg="#abab0a",width = 30,height = 4, font= ('arial', 13, 'bold')).grid(row=2, column= 0, pady=15, padx =40)

            #Create a button the allow the user go back to home page
            Button(self.frame9,text="Home", bg="#abab0a",fg='black', font= ('arial', 13, 'bold'), command = self.backhome2).grid(row=0, column=0, pady=5, columnspan = 2,sticky = E)

            #Create a button the allow the user to quit the program
            Button(self.frame9,text="Quit", bg="red",fg='black', font= ('arial', 13, 'bold'), command = self.quit).grid(row=3, column=0,columnspan =2, pady=5, sticky = W, padx =30)

            #Create a button the allow the user to start practise again
            Button(self.frame9,text="Restart", bg="yellow",fg='black', font= ('arial', 13, 'bold'), command = self.backtopic).grid(row=3, column=0,sticky = E, pady=5, padx =30)

            # send the result of the user to User class
            self.user1.transfer_detail(self.point)

        if result == "error":
            # display a error message when the user enter invalid input
            messagebox.showerror("Error", "Please enter the WHOLE NUMBER only (NO LETTER).")
        
    def backhome(self):
        #Remove the previous frame ( frame 3 )
        self.frame3.grid_remove()

        #Call the frame 2 to display
        self.frame2.grid()

    def backhome1(self):
        #Remove the previous frame ( frame 6 )
        self.frame6.grid_remove()

        #Call the frame 2 to display
        self.frame2.grid()

    def backhome2(self):
        #Remove the previous frame ( frame 9 )
        self.frame9.grid_remove()

        #Call the frame 2 to display
        self.frame2.grid()

    def backhome3(self):
        #Remove the previous frame ( frame 8 )
        self.frame8.grid_remove()

        #Call the frame 2 to display
        self.frame2.grid()

    def backtopic(self):
        #Remove the previous frame ( frame 9 )
        self.frame9.grid_remove()

        #Call the frame 4 to display
        self.frame4.grid()

    def backtopic2(self):
        #Remove the previous frame ( frame 8 )
        self.frame8.grid_remove()

        #Call the frame 4 to display
        self.frame4.grid()
        
        
# Define main main_window to the tkinter
main_window = Tk()

# Title the main window 
main_window.title("Ormiston Computing")

# Colour the background colour of the main window 
main_window.config(bg = '#00ffff' )

# Arrange the main the main_windw through .grid() method 
main_window.grid()

# Run the window_one class
window_one()

