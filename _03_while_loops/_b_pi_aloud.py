"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi = "31415926535897932384"
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi
    name = 0
    messagebox.showinfo(None, message="tell me the digits of pi in order")
    while name < 20:
        answer = simpledialog.askinteger(None, prompt="Another")
        if pi[name] == str(answer):
            messagebox.showinfo(None, message="Correct")
        else:
            messagebox.showinfo(None, message="Wrong")
            messagebox.showinfo(None, message="L")
            break
        name+=1
        print(name)
    if name == 20:
        messagebox.showinfo(None, message="Go touch grass nerd")
        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
