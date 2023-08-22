from tkinter import *
import pyshorteners
root = Tk()
root.title('Link Shortener')
root.iconbitmap(None)
root.geometry("400x300")
root.configure(bg='deep sky blue')
#bg = PhotoImage(file="download.png")
#label1 = Label( root, image = bg)
#label1.place(x = 100, y = 10)

def shorten():
    if shorty.get():
        shorty.delete(0,END)

    if my_entry.get():
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        shorty.insert(END,url)



my_label = Label(root,text="Enter url to shorten",font=("Helvetica",16),bg="deep sky blue")
my_label.pack(pady=10)

my_entry = Entry(root,font=("Helvetica",15))
my_entry.pack(pady=10)

my_button = Button(root, text="shortern link",command=shorten,font=("Helvetica",15),bg='indian red2')
my_button.pack(pady=10)

short_lable = Label(root, text="shoterned link",font=("Helvetica",12),bg='deep sky blue')
short_lable.pack(pady=10)

shorty = Entry(root,font=("Helvetica",17),justify=CENTER,width= 20,bd=0,background="deep sky blue",foreground="gray1")
shorty.pack(pady=10)


root.mainloop()
