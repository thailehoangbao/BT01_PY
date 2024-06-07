class AVLTreeNode:
    def __init__(self, key, iphone):
        self.key = key  # Giá iPhone
        self.iphone = iphone  # Thông tin iPhone (tên, mô tả, hình ảnh)
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, node, key, iphone):
        if not node:
            return AVLTreeNode(key, iphone)
        
        if key < node.key:
            node.left = self.insert(node.left, key, iphone)
        else:
            node.right = self.insert(node.right, key, iphone)

        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1:
            if key < node.left.key:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        if balance < -1:
            if key > node.right.key:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def insert_iphone(self, key, iphone):
        self.root = self.insert(self.root, key, iphone)

    def search_in_range(self, node, min_price, max_price, result):
        if not node:
            return
        
        if min_price < node.key:
            self.search_in_range(node.left, min_price, max_price, result)
        
        if min_price <= node.key <= max_price:
            result.append(node.iphone)
        
        if max_price > node.key:
            self.search_in_range(node.right, min_price, max_price, result)

    def find_iphones_in_range(self, min_price, max_price):
        result = []
        self.search_in_range(self.root, min_price, max_price, result)
        return result
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class iPhoneSearchApp:
    def __init__(self, root, avl_tree):
        self.root = root
        self.avl_tree = avl_tree
        self.setup_ui()

    def setup_ui(self):
        self.root.title("iPhone Price Search")

        tk.Label(self.root, text="Min Price:").grid(row=0, column=0, padx=10, pady=10)
        self.min_price_entry = ttk.Entry(self.root)
        self.min_price_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Max Price:").grid(row=1, column=0, padx=10, pady=10)
        self.max_price_entry = ttk.Entry(self.root)
        self.max_price_entry.grid(row=1, column=1, padx=10, pady=10)

        self.search_button = ttk.Button(self.root, text="Search", command=self.search_iphones)
        self.search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.result_listbox = tk.Listbox(self.root, width=50, height=10)
        self.result_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.result_listbox.bind('<<ListboxSelect>>', self.show_details)

        self.details_frame = tk.Frame(self.root)
        self.details_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.details_label = tk.Label(self.details_frame, text="", justify=tk.LEFT)
        self.details_label.pack(side=tk.LEFT)

        self.image_label = tk.Label(self.details_frame)
        self.image_label.pack(side=tk.RIGHT)

    def search_iphones(self):
        min_price = int(self.min_price_entry.get())
        max_price = int(self.max_price_entry.get())
        results = self.avl_tree.find_iphones_in_range(min_price, max_price)

        self.result_listbox.delete(0, tk.END)
        self.result_data = results
        if results:
            for iphone in results:
                display_text = f"{iphone['name']} - ${iphone['price']}: {iphone['description']}"
                self.result_listbox.insert(tk.END, display_text)
        else:
            messagebox.showinfo("No Results", "No iPhones found in the specified price range.")

    def show_details(self, event):
        selected_index = self.result_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            iphone = self.result_data[index]
            details_text = f"Name: {iphone['name']}\nPrice: ${iphone['price']}\nDescription: {iphone['description']}"
            self.details_label.config(text=details_text)

            # Fetch and display image
            image_url = iphone['image']
            response = requests.get(image_url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

if __name__ == "__main__":
    iphones = [
        {"price": 999, "name": "iPhone 12", "description": "iPhone model", "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"},
        {"price": 699, "name": "iPhone 11", "description": "iPhone model", "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"},
        {"price": 799, "name": "iPhone SE", "description": "iPhone model", "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"},
        # Thêm các sản phẩm khác nếu cần
    ]

    avl_tree = AVLTree()

    for iphone in iphones:
        avl_tree.insert_iphone(iphone["price"], iphone)

    root = tk.Tk()
    app = iPhoneSearchApp(root, avl_tree)
    root.mainloop()
