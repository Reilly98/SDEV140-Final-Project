"""
Author: Reilly Westrich
Date Written: 05/10/2025
Program: Module 08 Final Project
Version: 1.5
Mark It Off to do list.
"""
import tkinter as tk
from tkinter import messagebox, colorchooser


#The main window for managing lists
class MarkItOff:
    def __init__(self, wRoot):
        self.wRoot = wRoot
        self.wRoot.title("Mark It Off - To Do Lists")
        self.wRoot.geometry("600x800")

        #Dictionary to store lists
        self.dictLists = {}

        #Default colors
        self.strBgColor = "white"
        self.strFgColor = "black"

        #Main Window GUI Setup
        self.wLabel = tk.Label(wRoot, text="Mark It Off - My Lists", font=("Arial", 16), bg=self.strBgColor, fg=self.strFgColor)
        self.wLabel.pack(pady=10)

        #Entry for new list names
        self.wListEntry = tk.Entry(wRoot, width=30, bg=self.strBgColor, fg=self.strFgColor)
        self.wListEntry.pack(pady=5)

        #Button to add a new list
        self.wAddListButton = tk.Button(wRoot, text="Create New List", command=self.addList, bg=self.strBgColor, fg=self.strFgColor)
        self.wAddListButton.pack(pady=5)

        #Listbox to display all lists
        self.wListsListbox = tk.Listbox(wRoot, width=40, height=15, bg=self.strBgColor, fg=self.strFgColor)
        self.wListsListbox.pack(pady=10)

        #Button to manage a selected list's items
        self.wManageListButton = tk.Button(wRoot, text="Manage List", command=self.openListItemsWindow, bg=self.strBgColor, fg=self.strFgColor)
        self.wManageListButton.pack(pady=5)

        #Button to delete a list
        self.wDeleteListButton = tk.Button(wRoot, text="Delete List", command=self.deleteList, bg=self.strBgColor, fg=self.strFgColor)
        self.wDeleteListButton.pack(pady=5)

        #Buttons for color customization
        self.wChangeBgButton = tk.Button(wRoot, text="Change Background Color", command=self.changeBackgroundColor, bg=self.strBgColor, fg=self.strFgColor)
        self.wChangeBgButton.pack(pady=5)

        self.wChangeFgButton = tk.Button(wRoot, text="Change Text Color", command=self.changeTextColor, bg=self.strBgColor, fg=self.strFgColor)
        self.wChangeFgButton.pack(pady=5)

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

    #Delete a selected list
    def deleteList(self):
        try:
            iIndex = self.wListsListbox.curselection()[0]
            strListName = self.wListsListbox.get(iIndex)
            del self.dictLists[strListName]
            self.updateListsListbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a list!")

    #Update the listbox with current lists
    def updateListsListbox(self):
        self.wListsListbox.delete(0, tk.END)
        for strListName in self.dictLists:
            self.wListsListbox.insert(tk.END, strListName)

    #Open a new window to manage the selected list's items
    def openListItemsWindow(self):
        try:
            iIndex = self.wListsListbox.curselection()[0]
            strListName = self.wListsListbox.get(iIndex)
            wItemsWindow = tk.Toplevel(self.wRoot)
            ListItemsWindow(wItemsWindow, strListName, self.dictLists)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a list!")

    #Change background color
    def changeBackgroundColor(self):
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.strBgColor = color
            self.wRoot.configure(bg=self.strBgColor)
            for widget in [self.wLabel, self.wListEntry, self.wAddListButton, self.wListsListbox,
                           self.wManageListButton, self.wDeleteListButton, self.wChangeBgButton, self.wChangeFgButton]:
                widget.configure(bg=self.strBgColor)

    #Change text color
    def changeTextColor(self):
        color = colorchooser.askcolor(title="Choose Text Color")[1]
        if color:
            self.strFgColor = color
            for widget in [self.wLabel, self.wListEntry, self.wAddListButton, self.wListsListbox,
                           self.wManageListButton, self.wDeleteListButton, self.wChangeBgButton, self.wChangeFgButton]:
                widget.configure(fg=self.strFgColor)


#Window for managing items in a specific list
class ListItemsWindow:
    def __init__(self, wParent, strListName, dictLists):
        self.wParent = wParent
        self.strListName = strListName
        self.dictLists = dictLists
        self.wParent.title(f"Items in {strListName}")
        self.wParent.geometry("400x500")

        #Default colors
        self.strBgColor = "white"
        self.strFgColor = "black"

        #Load the image for the Mark Completed button using PhotoImage
        self.photoMarkCompleted = None
        try:
            self.photoMarkCompleted = tk.PhotoImage(file="mark_completed.png")
            print("Successfully loaded mark_completed.png")
        except tk.TclError as e:
            print(f"Error loading mark_completed.png: {e}. Trying mark_completed.gif...")
            try:
                self.photoMarkCompleted = tk.PhotoImage(file="mark_completed.gif")
                print("Successfully loaded mark_completed.gif")
            except tk.TclError as e2:
                print(f"Error loading mark_completed.gif: {e2}. Using text button instead.")
                self.photoMarkCompleted = None

        #GUI Setup for Items Window
        self.wLabel = tk.Label(self.wParent, text=f"Items in {strListName}", font=("Arial", 16), bg=self.strBgColor, fg=self.strFgColor)
        self.wLabel.pack(pady=10)

        #Entry for new item
        self.wItemEntry = tk.Entry(self.wParent, width=30, bg=self.strBgColor, fg=self.strFgColor)
        self.wItemEntry.pack(pady=5)

        #Button to add a new item
        self.wAddItemButton = tk.Button(self.wParent, text="Add Item", command=self.addItem, bg=self.strBgColor, fg=self.strFgColor)
        self.wAddItemButton.pack(pady=5)

        #Listbox to display items
        self.wItemsListbox = tk.Listbox(self.wParent, width=40, height=15, bg=self.strBgColor, fg=self.strFgColor)
        self.wItemsListbox.pack(pady=10)

        #Button to mark an item as completed
        if self.photoMarkCompleted:
            self.wMarkCompletedButton = tk.Button(self.wParent, image=self.photoMarkCompleted, command=self.markCompleted,)
        else:
            self.wMarkCompletedButton = tk.Button(self.wParent, text="Mark Completed", command=self.markCompleted, bg=self.strBgColor, fg=self.strFgColor,)
        self.wMarkCompletedButton.pack(pady=5)

        #Button to delete an item
        self.wDeleteItemButton = tk.Button(self.wParent, text="Delete Item", command=self.deleteItem, bg=self.strBgColor, fg=self.strFgColor)
        self.wDeleteItemButton.pack(pady=5)

        #Buttons for color customization
        self.wChangeBgButton = tk.Button(self.wParent, text="Change Background Color", command=self.changeBackgroundColor, bg=self.strBgColor, fg=self.strFgColor)
        self.wChangeBgButton.pack(pady=5)

        self.wChangeFgButton = tk.Button(self.wParent, text="Change Text Color", command=self.changeTextColor, bg=self.strBgColor, fg=self.strFgColor)
        self.wChangeFgButton.pack(pady=5)

        #Update listbox with current items
        self.updateItemsListbox()

    #Add a new item to the list
    def addItem(self):
        strItem = self.wItemEntry.get().strip()
        if strItem:
            #Check if item text already exists
            if not any(item['text'] == strItem for item in self.dictLists[self.strListName]):
                self.dictLists[self.strListName].append({'text': strItem, 'completed': False})
                self.updateItemsListbox()
                self.wItemEntry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Item already exists in the list!")
        else:
            messagebox.showwarning("Warning", "Please enter an item!")

    #Mark a selected item as completed or uncompleted
    def markCompleted(self):
        try:
            iIndex = self.wItemsListbox.curselection()[0]
            # Toggle completion status
            self.dictLists[self.strListName][iIndex]['completed'] = not self.dictLists[self.strListName][iIndex]['completed']
            self.updateItemsListbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item!")

    #Delete a selected item
    def deleteItem(self):
        try:
            iIndex = self.wItemsListbox.curselection()[0]
            del self.dictLists[self.strListName][iIndex]
            self.updateItemsListbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item!")

    #Update the listbox with current items
    def updateItemsListbox(self):
        self.wItemsListbox.delete(0, tk.END)
        for item in self.dictLists[self.strListName]:
            strDisplay = f"{item['text']} [Completed]" if item['completed'] else item['text']
            self.wItemsListbox.insert(tk.END, strDisplay)

    #Change background color
    def changeBackgroundColor(self):
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.strBgColor = color
            self.wParent.configure(bg=self.strBgColor)
            for widget in [self.wLabel, self.wItemEntry, self.wAddItemButton, self.wItemsListbox,
                           self.wMarkCompletedButton, self.wDeleteItemButton, self.wChangeBgButton, self.wChangeFgButton]:
                widget.configure(bg=self.strBgColor)

    #Change text color
    def changeTextColor(self):
        color = colorchooser.askcolor(title="Choose Text Color")[1]
        if color:
            self.strFgColor = color
            for widget in [self.wLabel, self.wItemEntry, self.wAddItemButton, self.wItemsListbox,
                           self.wMarkCompletedButton, self.wDeleteItemButton, self.wChangeBgButton, self.wChangeFgButton]:
                widget.configure(fg=self.strFgColor)


if __name__ == "__main__":
    wRoot = tk.Tk()
    app = MarkItOff(wRoot)
    wRoot.mainloop()