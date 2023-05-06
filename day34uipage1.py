from tkinter import *
from day34quizquestions1 import quizstarter

THEME_COLOR="#375362"

class QuizInterface:
    def __init__(self,quizer: quizstarter):#this is one way in which data-type can be set as well using variablename: datatype
        self.quizbrain=quizer
        self.windows=Tk()
        self.windows.title("Quizzer")
        self.windows.config(padx=20,pady=20,bg=THEME_COLOR)#padx and pady 20 means there will be a distance of atleast 20 between the nearest object and windows across x and y axis
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)#bg is set to theme color to make the text "Score:0" visible as the fg is white and the bg is white too,so the text is not visible
        #the background becomes visible too if the bg is not set to THEME_COLOR
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,
        width=280,
        text="Some Questions?: ",
        fill=THEME_COLOR,
        font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)#padx or pady means the minmum space b
        true_image=PhotoImage(file="D://udemyflashrighttick.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_image=PhotoImage(file="D://udemyflashwrongtick.png")
        self.false_button=Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)
        self.next_ques()


        self.windows.mainloop()

    def next_ques(self):
        self.canvas.config(bg="white")#when the next_ques function is called,firstly the bg of the canvas is
        #configured to white
        if self.quizbrain.questions_left():#this function is called to ensure that the current questionno is lesser than length of the given list
          kmn=self.quizbrain.start_questions()#in this current question object is selected from the list,the text is derieved from it,question_no is incremented and then 
          #returned along with question number
          self.score_label.config(text=f"Score:{self.quizbrain.score}")#now the text attribute od score_label widget is configured with current score attribute of quizbrain class which is updated
          #everytime checkans function is called
          self.canvas.itemconfig(self.question_text,text=kmn)#lastly the text attribute of question_text widget is updated
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")#else if the no more questions are left then buttons are disabled
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):#when true button is pressed then this function is called and the response returned by checkans in thsi case 
        #is True and this True is passed as parameter to give_feedback function
        is_right=self.quizbrain.checkans("True")
        self.give_feedback(is_right)

    def false_pressed(self):#when false button is pressed then False is passed as parameter to checkans function and the False response that 
        #is returned back is sent as parameter to give_feedback function
        is_right=self.quizbrain.checkans("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")#if is_right is True then canvas's background is configured to green
        else:
            self.canvas.config(bg="red")#else canvas background is configured to red
        self.windows.after(1000,self.next_ques)#after 1000 miliseconds the function self.next_ques is called

#canvas object is a widget in tkinter that is used to draw graphics and display images,also canvas widget
#offers customization like here you can customize the size of your canvas widget(height and width) and place the 
#text or image at a given position as per your own convenience like we have done here.The tkinter window only offers the 
#padding over here not te kind of customization mentioned above.We can also assign event handling functions to specific part of the canvas
#This will make your graphics and images responsive to mouse clicks like in this case by using this part of the code
#self.canvas.itemconfig(self.question_text,text=kmn) we are replacing a given attribute of of canvas
#item question_text(text item of question_text) with kmn,also canvas widget is highly scalable meaning that it can easily be
#resized, apparently it is also well suited for applications that need to display large amount of information,such as data visualization

#self.windows is a reference to the tkinter Tk object that represents the main window of your application
#mainloop is a method of the 'Tk' class that starts the main event loop. Once this application is called, the application will run until
#the user closes the window or the quit method is called
#the line self.windows.mainloop() starts the main event of the loop of tkinter application.It should be placed at the end
#of your tkinter code after all the widgets have been added to the window and their behaviour has been defined.
#In tkinter, the mainloop method is event driven loop that runs the GUI application until it is closed by the user progamatically.
#It listens to events, such as user inputs, and triggers the appropriate functions to handle such events 
#time.sleep blocks the execution of program for a specified number of seconds which means that it will make the GUI unresponsive,
#on the other hand self.windows.after schedules the execution of a programme after a specified amount of time without making the GUI unresponsive

