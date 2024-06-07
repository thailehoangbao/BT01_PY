class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.meaning = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, meaning):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.meaning = meaning

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_end_of_word:
            return node.meaning
        return None

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_with_prefix(node, prefix)

    def _find_words_with_prefix(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._find_words_with_prefix(child_node, prefix + char))
        return words

    def update(self, word, new_meaning):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.is_end_of_word:
            node.meaning = new_meaning
            return True
        return False
    
import tkinter as tk

from tkinter import ttk, messagebox

class DictionaryApp:
    def __init__(self, root, trie):
        self.root = root
        self.trie = trie
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Dictionary App")

        # Entry for word input
        self.word_entry = ttk.Entry(self.root, width=50)
        self.word_entry.grid(row=0, column=0, padx=10, pady=10)
        self.word_entry.bind('<KeyRelease>', self.on_key_release)

        # Button to search
        self.search_button = ttk.Button(self.root, text="Search", command=self.search_word)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display suggestions
        self.suggestions_listbox = tk.Listbox(self.root, height=10, width=50)
        self.suggestions_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        self.suggestions_listbox.bind('<<ListboxSelect>>', self.on_suggestion_select)

        # Text widget to display meaning
        self.meaning_text = tk.Text(self.root, height=10, width=50)
        self.meaning_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        # Entry for adding new word
        self.new_word_entry = ttk.Entry(self.root, width=50)
        self.new_word_entry.grid(row=3, column=0, padx=10, pady=10)

        # Entry for new word meaning
        self.new_meaning_entry = ttk.Entry(self.root, width=50)
        self.new_meaning_entry.grid(row=4, column=0, padx=10, pady=10)

        # Button to add new word
        self.add_button = ttk.Button(self.root, text="Add/Update Word", command=self.add_update_word)
        self.add_button.grid(row=5, column=0, padx=10, pady=10)

    def on_key_release(self, event):
        prefix = self.word_entry.get()
        suggestions = self.trie.starts_with(prefix)
        self.suggestions_listbox.delete(0, tk.END)
        for word in suggestions:
            self.suggestions_listbox.insert(tk.END, word)

    def on_suggestion_select(self, event):
        selected_word = self.suggestions_listbox.get(self.suggestions_listbox.curselection())
        meaning = self.trie.search(selected_word)
        self.meaning_text.delete(1.0, tk.END)
        self.meaning_text.insert(tk.END, meaning)

    def search_word(self):
        word = self.word_entry.get()
        meaning = self.trie.search(word)
        if meaning:
            self.meaning_text.delete(1.0, tk.END)
            self.meaning_text.insert(tk.END, meaning)
        else:
            messagebox.showinfo("Not Found", f"The word '{word}' is not in the dictionary.")

    def add_update_word(self):
        word = self.new_word_entry.get()
        meaning = self.new_meaning_entry.get()
        if word and meaning:
            self.trie.insert(word, meaning)
            messagebox.showinfo("Success", f"The word '{word}' has been added/updated.")
        else:
            messagebox.showerror("Error", "Both word and meaning are required.")

if __name__ == "__main__":
    trie = Trie()
    root = tk.Tk()
    app = DictionaryApp(root, trie)
    root.mainloop()
