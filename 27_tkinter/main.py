import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am cony! ", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")
window.mainloop()
