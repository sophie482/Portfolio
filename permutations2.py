import tkinter as tk
from itertools import permutations

# finds all permuations of a given word
def getPerms(wordToSolve):
    perms = [''.join(p) for p in permutations(wordToSolve)]
    number = 0
    permsOutput = ''
    for i in range(len(set(perms))):
        number +=1 
        permsOutput += (str(perms[i]) + "\n")
    return("There are " + str(number) + " possible combinations: \n" + str(permsOutput))

# evaluates user input (entry.get collects data from user) and calls get perms,
# then puts the result onto screen
def evaluate(event):
    res.configure(text = str(getPerms(entry.get())))
    
window = tk.Tk()
# tkinter window
tk.Label(window, text="Your Word:").pack()
# label is text box widget, .pack organizes/adds widgets to window
entry = tk.Entry(window)
# user input widget
entry.bind("<Return>", evaluate)
# when user hits return, evaluate runs with user input (entry)
entry.pack()
# adds entry widget to window
res = tk.Label(window)
# empty label for result
res.pack()
# adds result widget to window
window.mainloop()
# calls all window widgets
