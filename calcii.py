from tkinter import *

def click(event):
    global scvalue
    text= event.widget.cget("text")
    print(text)
    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
        
    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()


root = Tk()
root.geometry("400x600")  # Adjusted size to fit buttons better
root.title("Khushboo's Calculator...")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Define button properties
button_properties = {
    'padx': 8,  # Reduced padding for a smaller button size
    'pady': 8,
    'font': "lucida 18 bold",  # Slightly smaller font for better fit
    'bg': "lightgrey",
    'fg': "black"
}

# Define button labels and their corresponding rows
button_labels = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", "-", "*"],
    ["/","%", "=",],
    ["C","÷", "."]
]

# Create frames and add buttons using loops
frames = []
for i in range(len(button_labels)):
    f = Frame(root, bg="grey")
    f.pack(pady=5)  # Added padding between frames
    frames.append(f)

for row_index, labels in enumerate(button_labels):
    frame = frames[row_index]
    for text in labels:
        b = Button(frame, text=text, padx=button_properties['padx'], pady=button_properties['pady'],
                   font=button_properties['font'], bg=button_properties['bg'], fg=button_properties['fg'])
        b.pack(side=LEFT, padx=3, pady=3)  # Reduced button padding for better fit
        b.bind("<Button-1>", click)

root.mainloop()
