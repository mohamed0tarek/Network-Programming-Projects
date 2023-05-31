from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from socket import *
from threading import *

top = Tk()
top.title("Rock Paper Scissors (server)")
top.geometry("630x500")
top.config(bg="#0fb1f7")
##############################################################################################################################
# add paper image
img = Image.open("paper.png")
img = img.resize((70, 70), Image.ANTIALIAS)
paperImg = ImageTk.PhotoImage(img)

# add rock image
img = Image.open("rock.png")
img = img.resize((70, 70), Image.ANTIALIAS)
rockImg = ImageTk.PhotoImage(img)

# add scissors image
img = Image.open("scissors.png")
img = img.resize((70, 70), Image.ANTIALIAS)
scissorsImg = ImageTk.PhotoImage(img)
##############################################################################################################################

label1 = Label(top, text="Your choice :", font=("Arial", 12))
label1.place(x=50, y=25)

myChoiceLabel = Label(top, width=30, height=17, bg="black")
myChoiceLabel.place(x=50, y=50)

label2 = Label(top, text="Opponent choice :", font=("bookman", 12))
label2.place(x=350, y=25)

opponentChoiceLabel = Label(top, width=19, height=11, bg="black", text="Still Choosing...", fg="white", font=(12))
opponentChoiceLabel.place(x=350, y=50)

vs = Label(top, text="VS", fg="black", font=("Arial", 18), bg="#0fb1f7")
vs.place(x=290, y=150)

#############################################################################################################################

myRespond = ''
opponentRespond = ''
imgIntended = paperImg
flage = False

def checkResult():
    if myRespond == opponentRespond:
        win(f"Both players selected {myRespond}. It's a tie!")
    elif myRespond == "rock":
        if opponentRespond == "scissors":
            win("Rock smashes scissors! server win!")
        else:
            win("Paper covers rock! server lose.")
    elif myRespond == "paper":
        if opponentRespond == "rock":
            win("Paper covers rock! server win!")
        else:
            win("Scissors cuts paper! server lose.")
    elif myRespond == "scissors":
        if opponentRespond == "paper":
            win("Scissors cuts paper! server win!")
        else:
            win("Rock smashes scissors! server lose.")

def win(message):
    messagebox.showinfo("Result", message)
    top.destroy()

def checkRespond():
    global opponentRespond
    global imgIntended
    if opponentRespond == "paper":
        imgIntended = paperImg
    elif opponentRespond == "rock":
        imgIntended = rockImg
    elif opponentRespond == "scissors":
        imgIntended = scissorsImg


def clickPaper():
    global flage, myRespond, opponentRespond, imgIntended
    flage = True
    myRespond = "paper"
    myChoiceLabel.config(image=paperImg, width=220, height=250,bg="#82f937", highlightbackground="black", highlightthickness=3)
    rockButton.config(bg="white")
    scissorsButton.config(bg="white")
    for child in frame.winfo_children():
        child.configure(state="disabled")
    if opponentRespond != '':
        checkRespond()
        opponentChoiceLabel.config(image=imgIntended, width=220, height=250,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
        checkResult()
    send("paper")

def clickRock():
    global flage, myRespond, opponentRespond, imgIntended
    flage = True
    myRespond = "rock"
    myChoiceLabel.config(image=rockImg, width=220, height=250,bg="#82f937", highlightbackground="black", highlightthickness=3)
    paperButton.config(bg="white")
    scissorsButton.config(bg="white")
    for child in frame.winfo_children():
        child.configure(state="disabled")
    if opponentRespond != '':
        checkRespond()
        opponentChoiceLabel.config(image=imgIntended, width=220, height=250,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
        checkResult()
    send("rock")

def clickScissors():
    global flage, myRespond, opponentRespond, imgIntended
    flage = True
    myRespond = "scissors"
    myChoiceLabel.config(image=scissorsImg, width=220, height=250,bg="#82f937", highlightbackground="black", highlightthickness=3)
    rockButton.config(bg="white")
    paperButton.config(bg="white")
    for child in frame.winfo_children():
        child.configure(state="disabled")
    if opponentRespond != '':
        checkRespond()
        opponentChoiceLabel.config(image=imgIntended, width=220, height=250,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
        checkResult()
    send("scissors")

###############################################################################################################################
label3 = Label(top, text="Choices :", font=("Arial", 12), bg="#dae0e8")
label3.place(x=50, y=330)

canvas = Canvas(top, width=520, height=5, bg="#0fb1f7", highlightbackground="#0fb1f7")
canvas.place(x=50,y=355)
canvas.create_line(0, 5, 520, 5)

frame = Frame(top, width=520, height=100, bg="#0fb1f7")
frame.place(x=50,y=370)

paperButton = Button(frame, image=paperImg,width=100, height=100,bg="#fdba3a", bd=3, command=clickPaper)
paperButton.place(x=0,y=0)

rockButton = Button(frame, image=rockImg,width=100, height=100, bd=3,bg="#fdba3a",command=clickRock)
rockButton.place(x=200,y=0)

scissorsButton = Button(frame, image=scissorsImg,width=100, height=100, bd=3,bg="#fdba3a",command=clickScissors)
scissorsButton.place(x=400,y=0)
##############################################################################################################

def handler():
    global opponentRespond
    while True:
        respond = conn.recv (2048)
        respond = respond.decode ('UTF-8')
        if respond == "paper":
            opponentChoiceLabel.config(text="he is ready",fg="black", width=19, height=11,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
            opponentRespond = "paper"
            if flage:
                opponentChoiceLabel.config(image=paperImg, width=220, height=250,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
                checkResult()

        elif respond == "rock":
            opponentChoiceLabel.config(text="he is ready",fg="black", width=19, height=11,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
            opponentRespond = "rock"
            if flage:
                opponentChoiceLabel.config(image=rockImg, width=220, height=250,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
                checkResult()

        elif respond == "scissors":
            opponentChoiceLabel.config(text="he is ready",fg="black", width=19, height=11,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
            opponentRespond = "scissors"
            if flage:
                opponentChoiceLabel.config(image=scissorsImg, width=220, height=250,bg="#f1fc30", highlightbackground="black", highlightthickness=3)
                checkResult()
        


s = socket (AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 6000
s.setsockopt (SOL_SOCKET, SO_REUSEADDR, 1)
s.bind ((host, port))
s.listen (5)
conn, add = s.accept ()
thread = Thread (target=handler)
thread.start()

def send(val):
    conn.send(val.encode('UTF-8'))

top.mainloop()