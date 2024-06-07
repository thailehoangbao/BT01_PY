class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete_child = _delete(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0
            return False
        _delete(self.root, word, 0)

def filter_text(trie, text):
    words = text.split()
    filtered_words = []
    for word in words:
        if trie.search(word):
            filtered_words.append('*' * len(word))
        else:
            filtered_words.append(word)
    return ' '.join(filtered_words)

import tkinter as tk
from tkinter import ttk, messagebox

class SensitiveWordFilterApp:
    def __init__(self, root, trie):
        self.root = root
        self.trie = trie
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Sensitive Word Filter")

        # Entry for input text
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Button to filter text
        self.filter_button = ttk.Button(self.root, text="Filter Text", command=self.filter_text)
        self.filter_button.grid(row=1, column=0, padx=10, pady=10)

        # Text widget to display filtered text
        self.filtered_text = tk.Text(self.root, height=10, width=50)
        self.filtered_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        # Entry for adding new sensitive word
        self.new_word_entry = ttk.Entry(self.root, width=50)
        self.new_word_entry.grid(row=3, column=0, padx=10, pady=10)

        # Button to add new sensitive word
        self.add_button = ttk.Button(self.root, text="Add Sensitive Word", command=self.add_sensitive_word)
        self.add_button.grid(row=3, column=1, padx=10, pady=10)

        # Entry for deleting a sensitive word
        self.delete_word_entry = ttk.Entry(self.root, width=50)
        self.delete_word_entry.grid(row=4, column=0, padx=10, pady=10)

        # Button to delete a sensitive word
        self.delete_button = ttk.Button(self.root, text="Delete Sensitive Word", command=self.delete_sensitive_word)
        self.delete_button.grid(row=4, column=1, padx=10, pady=10)

    def filter_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        filtered = filter_text(self.trie, text)
        self.filtered_text.delete("1.0", tk.END)
        self.filtered_text.insert(tk.END, filtered)

    def add_sensitive_word(self):
        word = self.new_word_entry.get().strip()
        if word:
            self.trie.insert(word)
            messagebox.showinfo("Success", f"The word '{word}' has been added to the sensitive words list.")
            self.new_word_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a word.")

    def delete_sensitive_word(self):
        word = self.delete_word_entry.get().strip()
        if word:
            self.trie.delete(word)
            messagebox.showinfo("Success", f"The word '{word}' has been deleted from the sensitive words list.")
            self.delete_word_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a word.")

if __name__ == "__main__":
    trie = Trie()
    root = tk.Tk()
    app = SensitiveWordFilterApp(root, trie)
    root.mainloop()
