from tkinter import*
root = Tk()

def send():
  send = "You : "+e.get()
  txt.insert(END,"\n"+send)
  if (e.get()=="hello"):
    txt.insert(END,"\n"+"Bot : Hi")
  elif (e.get()=="hi"):
    txt.insert(END,"\n"+"Bot : Hello")
  elif (e.get()=="how are you"):
    txt.insert(END,"\n"+"Bot : fine!!,What about you.")
  elif (e.get()=="fine"):
    txt.insert(END,"\n"+"Bot : Nice")
  elif (e.get()=="good"):
    txt.insert(END,"\n"+"Bot : Nice!!")
  elif (e.get()=="very good"):
    txt.insert(END,"\n"+"Bot : Nice!")
  elif (e.get()=="nice"):
    txt.insert(END,"\n"+"Bot : Yeee!")
  elif (e.get()=="very nice"):
    txt.insert(END,"\n"+"Bot : Yeee Man,so glad to listen that")
  elif (e.get()=="intersting"):
    txt.insert(END,"\n"+"Bot : Very good!!")
  elif (e.get()=="what u doing today"):
    txt.insert(END,"\n"+"Bot : Actually, Im Watching Youtube.")
  elif (e.get()=="Wsp"):
    txt.insert(END,"\n"+"Bot : Ayeee Hello")
  elif (e.get()=="wsp"):
    txt.insert(END,"\n"+"Bot : hEllooo mann. ")
  elif (e.get()=="a"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="b"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="c"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="e"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="d"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="f"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="g"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="h"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="y"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="r"):
    txt.insert(END,"\n"+"Bot : ._. What ")
  elif (e.get()=="fuck you"):
    txt.insert(END,"\n"+"Bot : :/ Why. ")
  elif (e.get()=="ur dog"):
    txt.insert(END,"\n"+"Bot : Not Funny :/ ")
  elif (e.get()=="you are dog"):
    txt.insert(END,"\n"+"Bot : You are UnNormal Person. ")
  elif (e.get()=="can u calculate"):
    txt.insert(END,"\n"+"Bot : Yes. ")
  elif (e.get()=="1+1"):
    txt.insert(END,"\n"+"Bot : 2. ")
  elif (e.get()==""):
    txt.insert(END,"\n"+"Bot : Speak   ")
  elif (e.get()=="riad"):
    txt.insert(END,"\n"+"Bot : riad = baghl ")
  elif (e.get()=="what u doing"):
    txt.insert(END,"\n"+"Bot : Actually, Im Watching Youtube.")
  
  elif (e.get()=="who are you"):
    txt.insert(END,"\n"+"Bot : Maland. Profesional AI Made By Riad ")
  else:
    txt.insert(END,"\n"+"Bot : I Cant Read this")                  
  e.delete(0,END)
txt=Text(root)
txt.pack()
txt.grid(row = 4,column=0,columnspan=2)
e = Entry(root,width = 100)
send = Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("ChatBot")
root.resizable(False,False)





root.mainloop()