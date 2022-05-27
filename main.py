from tkinter import (
    Tk,
    # fill
    X,
    # side
    TOP,
    # widget
    Entry,
    OptionMenu,
    Label,
    Button,
    Frame,
    Radiobutton,
    # variable
    IntVar,
    StringVar,
)

# returns border options as a dictionary
def border(color, width):
    return {"highlightbackground": color, "highlightthickness": width}


root = Tk()
root.configure(background="#fff")
root.title("Quadratic Equation Solver | BMI Calculator")

# ================================= Quadradic Equation Solver ===============================

# top frame label
Label(root, text="Quadratic Equation Solver", pady=10, font=("Arial", 20, "bold"), bg="white").pack()

border_frame = Frame(root, **border("green", 3))
border_frame.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)

# quadradic equation solver
def quadratic_eq_solver(a, b, c):
    d = b ** 2 - 4 * a * c
    if a != 0:
        if d < 0:
            return -1, "Delta < 0 : No real roots"
        elif d == 0:
            b = 0 if b == 0.0 else b
            return 0, f"x1 = x2 = {-b / (2 * a)}"
        else:
            return 1, f"x1 = {(-b + d ** 0.5) / (2 * a)}  x2 = {(-b - d ** 0.5) / (2 * a)}"
    else:
        return 0, "'a' cannot be zero"


# solve button command
def eq_solve_eq():
    a = float(eq_a.get())
    b = float(eq_b.get())
    c = float(eq_c.get())
    ans = quadratic_eq_solver(a, b, c)
    eq_answer.set(ans[1])


# clear button command
def eq_clear():
    eq_a.set("0")
    eq_b.set("0")
    eq_c.set("0")
    eq_answer.set("-")


# top frame
frame_eq = Frame(border_frame, padx=5, pady=5)

# "a x^2" entry
eq_a = IntVar(root)
Entry(frame_eq, width=10, textvariable=eq_a, **border("red", 2)).grid(row=1, column=0)
Label(frame_eq, width=10, text="x^2 + ").grid(row=1, column=1)

# "b x" entry
eq_b = IntVar(root)
Entry(frame_eq, width=10, textvariable=eq_b, **border("red", 2)).grid(row=1, column=2)
Label(frame_eq, width=10, text="x + ").grid(row=1, column=3)

# "c" entry
eq_c = IntVar(root)
Entry(frame_eq, width=10, textvariable=eq_c, **border("red", 2)).grid(row=1, column=4)
Label(frame_eq, width=10, text=" = 0").grid(row=1, column=5)

# answer label
eq_answer = StringVar(root)
Label(frame_eq, text="", textvariable=eq_answer, font=("Arial", 14, "bold")).grid(row=2, column=1, columnspan=4, pady=10)
eq_answer.set("-")

# clear and solve button
Button(frame_eq, text="Clear", width=10, command=eq_clear, **border("orange", 2), fg="orange", bg="white").grid(row=3, column=1, columnspan=2)
Button(frame_eq, text="Solve", width=10, command=eq_solve_eq, **border("blue", 2), fg="blue", bg="white").grid(row=3, column=3, columnspan=2)

frame_eq.pack()

root.mainloop()
