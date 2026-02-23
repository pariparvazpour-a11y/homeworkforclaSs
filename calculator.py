import tkinter as tk
#تابع
def press(key):
    if key == "=":
        try:
            result = eval(display.get())
            display.set(result)
        except:
            display.set("خطا")
    elif key == "C":
        display.set("")
    else:
        display.set(display.get() + str(key))


root = tk.Tk()
root.title("ماشین حساب")
root.geometry("300x400")
root.resizable(False, False)

display = tk.StringVar()

#صفحه نمایش
entry = tk.Entry(
    root,
    textvariable=display,
    font=("Tahoma", 20),
    bd=10,
    relief="sunken",
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# ---------- دکمه ----------
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
]

#دکمه
#buttons = [
 #   ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
  #  ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
   # ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    #("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    #("C",5,0), ("⌫",5,1)
#]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        tk.Button(
            row_frame,
            text=btn,
            font=("Tahoma", 16),
            height=2,
            width=5,
            command=lambda b=btn: press(b)
        ).pack(side="left", expand=True, fill="both")

# دکمه پاک کردن
tk.Button(
    root,
    text="C",
    font=("Tahoma", 16),
    height=2,
    command=lambda: press("C")
).pack(fill="both", padx=10, pady=5)

root.mainloop()
