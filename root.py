from tkinter import*
import random

root=Tk()
root.title("Random words")
root.geometry("500x500")

label1=Label(root)

def generate_random():
    list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    random_L1=random.randint(53, 63)
    random_L2=random.randint(27, 52)
    random_L3=random.randint(1, 26)
    random_L4=random.randint(64, 94)
    random_L5=random.randint(64, 94)
    
    random_alpha1=list1[random_L1]
    random_alpha2=list1[random_L2]
    random_alpha3=list1[random_L3]
    random_alpha4=list1[random_L4]
    random_alpha5=list1[random_L5]
    
    label1["text"]=random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5
    
btn=Button(root, text="Generate random word", command=generate_random, bg="Blue", fg="White")
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()