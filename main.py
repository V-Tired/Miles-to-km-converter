from tkinter import *


def to_miles():
    miles = "{:.2f}".format(float(input.get()) * .621371)
    result.config(text=f"{miles} miles", fg="darkslateblue")
    label3.config(text=f"{float(input.get())} km is equal to")


def to_km():
    km = "{:.2f}".format(float(input.get()) * 1.609344)
    result.config(text=f"{km} km", fg="darkslateblue")
    label3.config(text=f"{float(input.get())} miles is equal to")


FONT = ("sans", 12, "bold")
window = Tk()
window.title("Conversion")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

result = Label(text="", fg="DeepPink4", font=FONT)
result.grid(column=2, row=3)
result.config(padx=5, pady=5)

header = Label(text="Enter Units to be Converted", fg="DeepPink4", font=FONT)
header.grid(column=2, row=0, padx=5, pady=5)

label3 = Label(text="is equal to", fg="DeepPink4", font=FONT)
label3.grid(column=2, row=2, padx=5, pady=5)


km_to_miles = Button(text="Convert km to miles", command=to_miles, bg="lightpink", fg="DeepPink4", font=FONT)
km_to_miles.grid(column=2, row=4, padx=5, pady=5)

miles_to_km = Button(text="Convert miles to km", command=to_km, bg="lightpink", fg="DeepPink4", font=FONT)
miles_to_km.grid(column=2, row=5, padx=5, pady=5)
# ----------------------------Entry-------------------
input = Entry(width=20, fg="darkslateblue", font=FONT)
input.grid(column=2, row=1, padx=5, pady=5)












window.mainloop()