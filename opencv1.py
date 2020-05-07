import cv2
import datetime
from tkinter import *
from tkinter import messagebox

global str

frame=None
def save1(framr,st):
    st1='.jpg'
    st2=st+st1
    print(st2)
    cv2.imwrite(st2,framr)
    m1=messagebox.showinfo("notification",'image is saved')
    exit(0)

def save():
    str=e.get()
    save1(frame,str)

def capture(fram):
    root = Tk()
    root.geometry("200x200")
    cv2.imshow("image",fram)
    m=Label(root,text='The image is captured').grid()
    l=Label(root,text='Name your pic').grid()
    global e
    e=Entry(root)
    e.grid()
    str=e.get()
    b = Button(root, text='save', command=save).grid()
    root.mainloop()
    cv2.imshow('pic',fram)
    cv2.waitKey(0)

v1 = cv2.VideoCapture(0)

while(True):
    ret,frame=v1.read()
    font=cv2.FONT_HERSHEY_COMPLEX
    text=str(datetime.datetime.now())
    frame=cv2.putText(frame,text,(10,50),font,1,(0,0,250),1)
    cv2.imshow('Press q to capture the image',frame)

    if cv2.waitKey(1)& 0xFF==ord('q'):
        fr=frame
        cv2.destroyWindow('Press q to capture the image')
        break

capture(fr)

v1.release()
cv2.destroyAllWindows()