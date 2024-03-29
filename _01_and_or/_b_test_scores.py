"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    q=simpledialog.askinteger(None, prompt="what score did you get on your test?")
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    d=simpledialog.askinteger(None, prompt="what score did you get on your second test?")
    # TODO) Take the average score of both tests (total score / 2)
    if (q+d)/2>89.5 and (q+d)/2<100:
        messagebox.showinfo(message="Yuo Gett A")
    if (q+d)/2>79.5 and (q+d)/2<89.5:
        messagebox.showinfo(message="Yuo Gett B")
    if (q+d)/2>69.5 and (q+d)/2<79.5:
        messagebox.showinfo(message="Yuo Gett C")
    if (q+d)/2>59.5 and (q+d)/2<69.5:
        messagebox.showinfo(message="Yuo Gett D")
    if (q+d)/2<59.5:
        messagebox.showinfo(message="Yuo Gett F(s0 traach)")
    if (q+d)/2>100:
        messagebox.showinfo(message="Yuo Gett A+(s0 gud")
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    pass
