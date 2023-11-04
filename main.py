from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

miles_label = Label(text="Miles", font=("DM Sans", 10, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("DM Sans", 10, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to", font=("DM Sans", 10, "normal"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

output_label = Label(text= "0", font=("DM Sans", 10, "normal"))
output_label.grid(column=1, row=1)
equal_label.config(padx=10, pady=10)

input = Entry()
input.focus()
input.grid(column=1, row=0)


def button_clicked():
    miles = input.get()
    KM = float(miles)*1.6
    output_label["text"] = round(KM)
    print("I got clicked")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()

