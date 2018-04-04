from tkinter import *
 
root = Tk()
root.title("test canvas")
 
can = Canvas(root,bg="gold")
can.pack()
can.create_oval(10,10,125,125)
 
def move(*args):
    print (args)
    if args[0] == "scroll":
        can.yview_scroll(args[1],"unit")
    #else:
        #can.yview_moveto(args[1])
 
scl = Scrollbar(root,command=move)
scl.pack()
root.mainloop()
