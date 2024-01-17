#!/usr/bin/env python
# coding: utf-8

# In[1]:


def welcome_bot(): 
    #Welcome bot
    print('Welcome To NetTech')
    user_name=input('Enter Your good Name')
    print('Hellow',user_name)
    mobile_number=input('Enter Your Mobile Number')
    print('Mobile Number:',mobile_number)


# In[2]:


def chai_recommandation():
    #mumbai based chai recommandation bot
    #welcome use to mumbai
    print('Welcome to mumbai city')
    #ask user to name
    user_name=input("What's your good name? ")
    #greaing user# ask user to its bugedet
    print('hello',user_name.title())
    # ask user to its budget
    budget=int(input('Please enter your budget:'))
    #500--- go to taj hotel
    if budget>=500:
        print('Go to taj hotel')
    #100-500---starbucks
    elif budget>=100 and budget<500:
        print('Please go to starbucks')
    #50-100----udipi
    elif budget>=50 and budget<100:
        print('Please go to udipi')
    #10-50------tapari
    elif budget>=100 and budget<500:
        print('Please go to tapari')
    #<10 n hotes available
    else:
        print('No hotes available')


# In[3]:


def make_my_trip():   
    #make my trip recommandation hotels
    #welcome user in 
    print('welcome to make my trip')
    #Ask user its details
    user_name=input('please enter your good name:')
    mobile_no=input('please enter your Mobile number: ')
    age=input('please enter your age:  ')
    members=input('please enter how many members: ')
    print('hello',user_name.title(),mobile_no,age,members)
    #please enter city
    city=input('please enter city are you interested:  ')
    #please ask user budget plan
    budget=int(input('please enter your budget'))
    if budget>=5000:
        print('please go to 5 star hotels')
    elif budget>=4000 and budget<5000:
        print('please go to 3 star hotels')
    elif budget>=2000 and budget<4000:
        print('please go to 2 star hotels')
    elif budget>=1000 and budget<2000:
        print('please go to normal hotels')    
    else:
        print('no hotels available')


# In[4]:


def head_and_tails():   
    #head and tails
    #welcome
    print('welcome to the heads and tails game')
    user_input=input('please enter Head  Or Tails')
    print('you choose :',user_input.title())
    #coint toss
    import random
    if random.choice('ht')==('h'):
        coin_toss='Heads'
    else:
        coin_toss='Tails'
        print('coin result:',coin_toss.title())
    if user_input.lower()==coin_toss.lower():
        print('you win')
    else:
        print('you loss')


# In[5]:


def ludo_game():  
    #Welcome to Lud Game
    print('Welcome to the Ludo Game')
    user_input=input('Please Select Dice Number')
    print('You Choose:', user_input.title())
    #dice Toss
    import random
    dice_toss=random.choice('123456')
    print('Dice Result:',dice_toss)
    #use condition statement
    if user_input==dice_toss:
        print('You Win')
    else:
        print('you loss')


# In[6]:


def Quiz_game():
    #Welcome to Quizgame
    print('Welcome To The Quiz competion Game')
    que1=input('How Many Days DoWe Have In A week:?')
    score=0
    if que1=="7":
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')
    print('*'*30)

    que2=input('How Many Days DoWe Are There In A Normal Year:?')
    #score=0
    if que2=="365":
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')
    print('*'*30)

    que3=input('How Many Colors Are In A Rainbow:?')
    #score=0
    if que3=="7":
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')
    print('*'*30)

    que4=input('How Many Letters Are In The English alphabet :?')
    #score=0
    if que4=="26":
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')
    print('*'*30)
    print('Your Tatal Score Is:',score)
    


# In[7]:


def multiplication_table():
    #multification table
    num=int(input('please enter number here'))
    for i in range(1,10+1):
        print(i,'X',num,'=',i*num)


# In[8]:


def cube_table():
    print('Welcome To Cube Table')
        #multification table
    num=int(input('please enter number here'))
    for i in range(1,num+1):
        print('cube of',i,'=',i**num)


# In[9]:


def factorial():   
    #factorial Number
    print('Welcome to factorial')

    num=int(input('please enter number:-'))
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print('the factorial of',num,'is',factorial)


# In[10]:


def fibonaci():
    #Welcome To Fibonahi Number
    print('Wel Come to Fibonacci Numbers')
    #ask user to one inpu
    num=int(input('please enter one number:-'))
    #addition of first to numbers
    n1,n2=0,1
    count=0
    for i in range(1,num+1):
        print(n1)
        num=n1+n2
        n1=n2
        n2=num


# In[11]:


def password():   
    #Welcome to Passord Generate matchine
    print('Welcome to password generate matchine')
    #Ask user to how many digit password required
    user_input=int(input('please enter how many digit password required: '))
    #use random library
    import random
    import string
    import secrets
    letters=string.ascii_letters
    digit=string.digits
    special_char=string.punctuation
    #use if else
    if user_input>=8:
    #use for loop
        password=''
        special_list=letters+digit+special_char
        for i in range(user_input):
            password=password+random.choice(special_list)
        print('Your Password is:',password)
    else:
        print('please enter strong pasword')


# In[12]:


def Countdown_Timer():
    #Countdown Timer
    from countdown import countdown
    user_input_minutes=int(input("Please Enter Minutes:"))
    user_input_seconds=int(input("please enter seconds:"))
    # Create a countdown of 1 minute and 10 seconds
    countdown(mins=user_input_minutes,secs=user_input_seconds)


# In[13]:


def mind_game():
    #Welcome to the mind game
    import time
    import random
    num=0
    print('Welcome to the guess game:')
    print('*'*30)
    time.sleep(5)
    #Please guesss the number from 1 to 500
    print('Please guesss the number from 1 to 500')
    print('*'*30)
    time.sleep(0.8)
    #Please double your guess number
    print('Please double your guess number:')
    print('*'*30)
    time.sleep(5)
    #Please add my 50 in your double number
    for i in range(4):
        my_number=random.randint(1, 500)
        num=num+my_number
        print('Then add my',my_number,'in your double number:')
        print('*'*30)
        time.sleep(5)
    #Please divide by your last ans
    print('Then divide by 2  your last ans:')
    print('*'*30)
    time.sleep(1)
    #Please divide by your last ans
    print('Then minus guess number by devided an ans:')
    print('*'*30)
    time.sleep(5)
    #thank you
    last_ans=my_number/2
    print('thank you, your ans is',last_ans)


# In[14]:


#pip install tk


# In[15]:


#importin Tkinterlibrary
import tkinter as tk
#creating a main window
window=tk.Tk()
#chnge title
window.title('Deepak Murdekar')
#decide indows size
window.geometry('600x500')
#add lable
tk.Label(window,text='PYTHON PROJECT',font=('helvetica',21,'bold')).place(x=150,y=30)
tk.Label(window,text='Made By : Deepak M',font=('helvetica',16,)).place(x=180,y=80)

#add button
tk.Button(window,text='Welcome Bot',command=welcome_bot).place(x=30,y=150,width=150,height=35)
tk.Button(window,text='Chai Recommandation',command=chai_recommandation).place(x=210,y=150,width=150,height=35)
tk.Button(window,text='Make my Trip',command=make_my_trip).place(x=400,y=150,width=150,height=35)
tk.Button(window,text='Heads and Tails',command=head_and_tails).place(x=30,y=210,width=150,height=35)
tk.Button(window,text='ludo Game',command=ludo_game).place(x=210,y=210,width=150,height=35)
tk.Button(window,text='Quiz Game',command=Quiz_game).place(x=400,y=210,width=150,height=35)
tk.Button(window,text='Multiplication Table',command=multiplication_table).place(x=30,y=270,width=150,height=35)
tk.Button(window,text='Cube Table',command=welcome_bot).place(x=210,y=270,width=150,height=35)
tk.Button(window,text='Factorial',command=factorial).place(x=400,y=270,width=150,height=35)
tk.Button(window,text='Fibonaci',command=fibonaci).place(x=30,y=330,width=150,height=35)
tk.Button(window,text='Password',command=password).place(x=210,y=330,width=150,height=35)
tk.Button(window,text='Countdown Timer',command=Countdown_Timer).place(x=400,y=330,width=150,height=35)
tk.Button(window,text='Mind Game',command=mind_game).place(x=210,y=390,width=150,height=35)



#main loop (ye agr nhi likhoge toh UI nahi dikhega)
window.mainloop()


# In[ ]:


ludo_game()
Quiz_game()
multiplication_table()
cube_table()
factorial()
fibonaci()
password()
Countdown_Timer()
mind_game()

