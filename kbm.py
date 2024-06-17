from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0])

mixer.init()

mixer.music.load('C:\\Users\\Hp\\OneDrive\\Desktop\\kbc.mp3')
mixer.music.play(-1)

def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressLabelA.place_forget()
    progressLabelB.place_forget()
    progressLabelC.place_forget()
    progressLabelD.place_forget()
    b=event.widget
    value=b['text']

    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    win2.destroy()
                    win.destroy()

                def playagain():
                    mixer.music.stop()
                    win2.destroy()
                    questionArea.delete(1.0,END)
                    questionArea.insert(END,questions[0])

                    option1.config(text=first_option[0])
                    option2.config(text=second_option[0])
                    option3.config(text=third_option[0])
                    option4.config(text=fourth_option[0])

                    amtlabel.config(image=amtimg)
                    
                mixer.music.stop()
                mixer.music.load('C:\\Users\\Hp\\OneDrive\\Desktop\\kbcwon.mp3')
                mixer.music.play()
                win2=Toplevel()
                win2.overrideredirect(True)
                win2.config(background="black")
                win2.geometry("500x400+140+30")
                win2.title("You won 1M pounds...")
                imgLabel=Label(win2,image=centerimg,bd=0)
                imgLabel.pack(pady=30)
                wonLabel=Label(win2,text="You Won..!",font=("arial",40,"bold"),bg="black",fg="white")
                wonLabel.pack()

                playagainButton=Button(win2,text="Play Again",font=("arial",20,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=playagain)
                playagainButton.pack()
                closeButton=Button(win2,text="Close",font=("arial",20,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=close)
                closeButton.pack()

                happyimg=PhotoImage(file="C:\\Users\\Hp\\OneDrive\\Desktop\\happy.png")
                happyLabel=Label(win2,image=happyimg,bg="black")
                happyLabel.place(x=30,y=280)

                happyLabel1=Label(win2,image=happyimg,bg="black")
                happyLabel1.place(x=400,y=280)
                
                win2.mainloop()
                break
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            option1.config(text=first_option[i+1])
            option2.config(text=second_option[i+1])
            option3.config(text=third_option[i+1])
            option4.config(text=fourth_option[i+1])
            amtlabel.config(image=amtimages[i])

        if value not in correct_answers:
            def close():
                win1.destroy()
                win.destroy()

            def tryagain():
                win1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])

                option1.config(text=first_option[0])
                option2.config(text=second_option[0])
                option3.config(text=third_option[0])
                option4.config(text=fourth_option[0])

                amtlabel.config(image=amtimg)
            
            win1=Toplevel()
            win1.overrideredirect(True)
            win1.config(background="black")
            win1.geometry("500x400+140+30")
            win1.title("You won 0 pounds...")
            imgLabel=Label(win1,image=centerimg,bd=0)
            imgLabel.pack(pady=30)
            loseLabel=Label(win1,text="You Lose..!",font=("arial",40,"bold"),bg="black",fg="white")
            loseLabel.pack()

            tryagainButton=Button(win1,text="Try Again",font=("arial",20,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=tryagain)
            tryagainButton.pack()
            closeButton=Button(win1,text="Close",font=("arial",20,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=close)
            closeButton.pack()

            sadimg=PhotoImage(file="C:\\Users\\Hp\\OneDrive\\Desktop\\sad.png")
            sadLabel=Label(win1,image=sadimg,bg="black")
            sadLabel.place(x=30,y=280)

            sadLabel1=Label(win1,image=sadimg,bg="black")
            sadLabel1.place(x=400,y=280)
            
            win1.mainloop()
            break

def lifeline50():
    lifeline50button.config(image=image50x,state="disabled")
    if questionArea.get(1.0,'end-1c')==questions[0]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[1]:
        option1.config(text='')
        option4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[2]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[3]:
        option2.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[4]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[5]:
        option2.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[6]:
        option2.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[7]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[8]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[9]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[10]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[11]:
        option2.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[12]:
        option1.config(text='')
        option3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[13]:
        option1.config(text='')
        option4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[14]:
        option3.config(text='')
        option4.config(text='')

    
def audiencepolelifeline():
    audiencePolebutton.config(image=audiencepolex,state="disabled")
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620,y=190)
    progressbarC.place(x=660,y=190)
    progressbarD.place(x=700,y=190)

    progressLabelA.place(x=580,y=320)
    progressLabelB.place(x=620,y=320)
    progressLabelC.place(x=660,y=320)
    progressLabelD.place(x=700,y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=35)
        progressbarB.config(value=60)
        progressbarC.config(value=80)
        progressbarD.config(value=20)

    if questionArea.get(1.0,'end-1c')==questions[2]:
        progressbarA.config(value=40)
        progressbarB.config(value=75)
        progressbarC.config(value=60)
        progressbarD.config(value=30)
        
    if questionArea.get(1.0,'end-1c')==questions[3]:
        progressbarA.config(value=85)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=30)
        
    if questionArea.get(1.0,'end-1c')==questions[4]:
        progressbarA.config(value=40)
        progressbarB.config(value=95)
        progressbarC.config(value=40)
        progressbarD.config(value=60)
        
    if questionArea.get(1.0,'end-1c')==questions[5]:
        progressbarA.config(value=80)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0,'end-1c')==questions[6]:
        progressbarA.config(value=80)
        progressbarB.config(value=35)
        progressbarC.config(value=50)
        progressbarD.config(value=70)
        
    if questionArea.get(1.0,'end-1c')==questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=95)
        progressbarC.config(value=60)
        progressbarD.config(value=70)
        
    if questionArea.get(1.0,'end-1c')==questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=80)
        
    if questionArea.get(1.0,'end-1c')==questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=85)
        progressbarC.config(value=60)
        progressbarD.config(value=50)
        
    if questionArea.get(1.0,'end-1c')==questions[10]:
        progressbarA.config(value=50)
        progressbarB.config(value=85)
        progressbarC.config(value=20)
        progressbarD.config(value=60)
        
    if questionArea.get(1.0,'end-1c')==questions[11]:
        progressbarA.config(value=80)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=40)
        
    if questionArea.get(1.0,'end-1c')==questions[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=95)
        progressbarC.config(value=60)
        progressbarD.config(value=70)
        
    if questionArea.get(1.0,'end-1c')==questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=45)
        progressbarC.config(value=90)
        progressbarD.config(value=70)
        
    if questionArea.get(1.0,'end-1c')==questions[14]:
        progressbarA.config(value=80)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=10)

def phonelifeline():
    mixer.music.load("C:\\Users\\Hp\\OneDrive\\Desktop\\calling.mp3")
    mixer.music.play()
    callButton.place(x=70,y=260)
    phonebutton.config(image=phoneimgx,state="disabled")


def phoneclick():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()
    
    mixer.music.load('C:\\Users\\Hp\\OneDrive\\Desktop\\kbc.mp3')
    mixer.music.play(-1)
    
    
  
        
    
correct_answers=["Ganesha","Jaipur","New Delhi","6","14 Sep",
                 "28","Vrindachal","Mumbai","Bangalore","Marble","1969",
                 "8 Sep","14 Oct","Malayalam","Yen"]

questions=["Which God is also known as 'Gauri Nandan'?",
           "Which city is also known as Pink City in India?",
           "What is the Capital of India?",
           "How many major religions are there in India?",
           "When is the Hindi Diwas celebrated?",
           "How many states are there in India?",
           "Which of the following is not a state of India?",
           "Which Indian city hosts Indian movie Industry?",
           "Which city is known as the 'Silicon Valley of India'?",
           "Taj Mahal was made of ....",
           "In which year did the first moon landing occur?",
           "The International Literacy Day is observed on..",
           "Which Day is observed as the World Standards Day?",
           "The language of Lakshadweep. a Union Territory of India, is?",
           "What is the currency of Japan?"]

first_option=["Agni","Banglore","Mumbai","6",
              "13 Sep","28","Vrindachal","Goa","Delhi","Brick","1966",
              "8 Sep","26 June","Tamil","Yen"]

second_option=["Indra","Maysore","New Delhi","7","14 Sep",
               "29","Goa","Mumbai","Mumbai","Marble","1969",
               "28 Nov","14 Oct","Hindi","Won"]

third_option=["Hanuman","Jaipur","Kolkata","8","14 July","30","Jharkhand",
              "Chennai","Chennai","Granite","1968","2 May","15 Nov",
              "Malayalam","Euro"]

fourth_option=["Ganesha","Kochi","Chennai","9","15 Aug","31","Chattisgarh",
               "Kolkata","Bangalore","Sandstone","1970","22 Sep","2 Dec",
               "Telugu","Dollar"]


win=Tk()
win.geometry("1270x652+0+0")
win.title("Who wants to be a Millionaire")
win.config(background="black")

leftframe=Frame(win,bg="black",padx=90)
leftframe.grid(row=0,column=0)

rightframe=Frame(win,bg="black",pady=25,padx=15)
rightframe.grid(row=0,column=1)

topframe=Frame(leftframe,bg="black",pady=15)
topframe.grid(row=0,column=0)

centerframe=Frame(leftframe,bg="black",pady=15)
centerframe.grid(row=1,column=0)

bottomframe=Frame(leftframe,bg="black",pady=15)
bottomframe.grid(row=2,column=0)

image50=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\50-50.png')
image50x=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\50-50-x.png')
lifeline50button=Button(topframe,image=image50,bg="black",activebackground="black",bd=0,width=180,height=80,command=lifeline50)
lifeline50button.grid(row=0,column=0)

audiencepole=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\audiencePole.png')
audiencepolex=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\audiencePolex.png')

audiencePolebutton=Button(topframe,image=audiencepole,bg="black",activebackground="black",bd=0,width=180,height=80,command=audiencepolelifeline)
audiencePolebutton.grid(row=0,column=1)

phoneimg=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\phoneAFriend.png')
phoneimgx=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\phoneAFriendx.png')
phonebutton=Button(topframe,image=phoneimg,bg="black",activebackground="black",bd=0,width=180,height=80,command=phonelifeline)
phonebutton.grid(row=0,column=2)

callimage=PhotoImage(file="C:\\Users\\Hp\\OneDrive\\Desktop\\phone.png")

callButton=Button(win,image=callimage,bd=0,bg="black",activebackground="black",cursor="hand2",command=phoneclick)


centerimg=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\center.png')
centerlabel=Label(centerframe,image=centerimg,bg="black",height=200,width=300)
centerlabel.grid(row=0,column=0)

layimg=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\lay.png')
laylabel=Label(bottomframe,image=layimg,bg="black")
laylabel.grid(row=0,column=0)

amtimg=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture0.png')
amtimg1=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture1.png')
amtimg2=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture2.png')
amtimg3=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture3.png')
amtimg4=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture4.png')
amtimg5=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture5.png')
amtimg6=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture6.png')
amtimg7=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture7.png')
amtimg8=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture8.png')
amtimg9=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture9.png')
amtimg10=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture10.png')
amtimg11=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture11.png')
amtimg12=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture12.png')
amtimg13=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture13.png')
amtimg14=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture14.png')
amtimg15=PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Desktop\\picture15.png')

amtimages=[amtimg1,amtimg2,amtimg3,amtimg4,amtimg5,amtimg6,amtimg7,
           amtimg8,amtimg9,amtimg10,amtimg11,amtimg12,amtimg13,amtimg14,
           amtimg15]


amtlabel=Label(rightframe,image=amtimg,bg="black")
amtlabel.grid(row=0,column=0)

questionArea=Text(bottomframe,font=("arial",18,"bold"),width=34,height=2,wrap="word",bg="black",fg="white",bd=0)
questionArea.place(x=70,y=10)
questionArea.insert(END,questions[0])

labelA=Label(bottomframe,text="A:",font=("arial",16,"bold"),bg="black",fg="white")
labelA.place(x=60,y=110)

labelB=Label(bottomframe,text="B:",font=("arial",16,"bold"),bg="black",fg="white")
labelB.place(x=340,y=110)

labelC=Label(bottomframe,text="C:",font=("arial",16,"bold"),bg="black",fg="white")
labelC.place(x=60,y=190)

labelD=Label(bottomframe,text="D:",font=("arial",16,"bold"),bg="black",fg="white")
labelD.place(x=340,y=190)

option1=Button(bottomframe,text=first_option[0],font=("arial",18,"bold"),bg="black",fg="white",activebackground="black",bd=0,activeforeground="white",cursor="hand2")
option1.place(x=110,y=100)

option2=Button(bottomframe,text=second_option[0],font=("arial",18,"bold"),bg="black",fg="white",activebackground="black",bd=0,activeforeground="white",cursor="hand2")
option2.place(x=400,y=100)

option3=Button(bottomframe,text=third_option[0],font=("arial",18,"bold"),bg="black",fg="white",activebackground="black",bd=0,activeforeground="white",cursor="hand2")
option3.place(x=110,y=180)

option4=Button(bottomframe,text=fourth_option[0],font=("arial",18,"bold"),bg="black",fg="white",activebackground="black",bd=0,activeforeground="white",cursor="hand2")
option4.place(x=400,y=180)

option1.bind('<Button-1>',select)
option2.bind('<Button-1>',select)
option3.bind('<Button-1>',select)
option4.bind('<Button-1>',select)

progressbarA=Progressbar(win,orient=VERTICAL,length=120)
progressbarB=Progressbar(win,orient=VERTICAL,length=120)
progressbarC=Progressbar(win,orient=VERTICAL,length=120)
progressbarD=Progressbar(win,orient=VERTICAL,length=120)

progressLabelA=Label(win,text="A",font=("arial",20,"bold"),bg="black",fg="white")
progressLabelB=Label(win,text="B",font=("arial",20,"bold"),bg="black",fg="white")
progressLabelC=Label(win,text="C",font=("arial",20,"bold"),bg="black",fg="white")
progressLabelD=Label(win,text="D",font=("arial",20,"bold"),bg="black",fg="white")








win.mainloop()
