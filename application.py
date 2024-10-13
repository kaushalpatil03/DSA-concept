import tkinter as tk
from bst import BinarySearchTree

class BSTApp:
    def __init__(self, root):
        self.bst = BinarySearchTree()
        self.root = root
        self.root.title("Binary Search Tree Application")

        # Label for input
        self.label = tk.Label(root, text="Enter a number:")
        self.label.pack()

        # Entry field for input
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Button to insert into BST
        self.insert_button = tk.Button(root, text="Insert", command=self.insert_value)
        self.insert_button.pack()

        # Button to display inorder traversal
        self.display_button = tk.Button(root, text="Display Inorder Traversal", command=self.display_inorder)
        self.display_button.pack()

        # Text area to display the output
        self.output = tk.Text(root, height=10, width=40)
        self.output.pack()

    def insert_value(self):
        try:
            value = int(self.entry.get())  # Get the value from the input
            self.bst.insert(value)
            self.output.insert(tk.END, f"Inserted {value} into BST\n")
            self.entry.delete(0, tk.END)  # Clear the input field
        except ValueError:
            self.output.insert(tk.END, "Please enter a valid integer\n")

    def display_inorder(self):
        inorder_result = self.bst.inorder()  # Get inorder traversal
        self.output.insert(tk.END, f"Inorder Traversal: {inorder_result}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
