"""
Author: Reilly Westrich
Date Written: 04/28/2025
Program: Module 06 Programming Assignment
Version: 1.3
Mark It Off to do list. Currently just the main window for viewing and creating lists.
Will be working on adding another window for specific lists and allow user to add
items to list along with delete and mark completed. Will also be adding priority indicators
along with color customization.
"""
import tkinter as tk
from tkinter import messagebox


#the main window for managing lists
class MarkItOff:

    def __init__(self, wRoot):
        self.wRoot = wRoot
        self.wRoot.title("Mark It Off - To Do Lists")
        self.wRoot.geometry("400x500")

        #Dictionary to store lists
        self.dictLists = {}

        #Main Window GUI Setup
        self.wLabel = tk.Label(wRoot, text="Mark It Off - My Lists", font=("Arial", 16))
        self.wLabel.pack(pady=10)

        #Entry for new list names
        self.wListEntry = tk.Entry(wRoot, width=30)
        self.wListEntry.pack(pady=5)

        #Button to add a new list
        self.wAddListButton = tk.Button(wRoot, text="Create New List", command=self.addList)
        self.wAddListButton.pack(pady=5)

        #Listbox to display all lists
        self.wListsListbox = tk.Listbox(wRoot, width=40, height=15)
        self.wListsListbox.pack(pady=10)

        #Button to delete a list
        self.wDeleteListButton = tk.Button(wRoot, text="Delete List", command=self.deleteList)
        self.wDeleteListButton.pack(pady=5)

    #List Management
    def addList(self):
        strListName = self.wListEntry.get().strip()
        if strListName:
            if strListName not in self.dictLists:
                self.dictLists[strListName] = []
                self.updateListsListbox()
                self.wListEntry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "List name already exists!")
        else:
            messagebox.showwarning("Warning", "Please enter a list name!")

    #delete a selected list
    def deleteList(self):
        try:
            iIndex = self.wListsListbox.curselection()[0]
            strListName = self.wListsListbox.get(iIndex)
            del self.dictLists[strListName]
            self.updateListsListbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a list!")

    #update the listbox with current lists
    def updateListsListbox(self):
        self.wListsListbox.delete(0, tk.END)
        for strListName in self.dictLists:
            self.wListsListbox.insert(tk.END, strListName)


if __name__ == "__main__":
    wRoot = tk.Tk()
    app = MarkItOff(wRoot)
    wRoot.mainloop()