class Node:
    def __init__(self, phone):
        self.key = phone["price"]
        self.info = phone
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert_node(self, phone):
        self.root = self.insert(self.root, phone)

    def insert(self, root, phone):
        # Thêm nút gốc
        if root is None:
            return Node(phone)

        # Chèn vào cây con trái hoặc phải
        if phone["price"] < root.key:
            root.left = self.insert(root.left, phone)
        elif phone["price"] > root.key:
            root.right = self.insert(root.right, phone)

        return root

    def in_order(self, root):
        # Duyệt cây theo thứ tự in-order
        if root is None:
            return ''
        return f"{self.in_order(root.left)} {root.key} - {root.info['name']} {self.in_order(root.right)}"

    def pre_order(self, root):
        # Duyệt cây theo thứ tự pre-order
        if root is None:
            return ''
        return f"{root.key} - {root.info['name']} {self.pre_order(root.left)} {self.pre_order(root.right)}"

    def post_order(self, root):
        # Duyệt cây theo thứ tự post-order
        if root is None:
            return ''
        return f"{self.post_order(root.left)} {self.post_order(root.right)} {root.key} - {root.info['name']}"

    def get_tree_in_order(self):
        # Lấy biểu diễn cây theo thứ tự in-order
        return self.in_order(self.root)

    def get_tree_pre_order(self):
        # Lấy biểu diễn cây theo thứ tự pre-order
        return self.pre_order(self.root)

    def get_tree_post_order(self):
        # Lấy biểu diễn cây theo thứ tự post-order
        return self.post_order(self.root)

    def find_price(self, min_price, max_price):
        # Tìm các điện thoại trong khoảng giá
        result = []
        self._find_price(self.root, min_price, max_price, result)
        return result

    def _find_price(self, root, min_price, max_price, result):
        if root is None:
            return

        # Kiểm tra và thêm giá trị nếu nằm trong khoảng
        if min_price <= root.key <= max_price:
            result.append(root.info["name"])

        # Duyệt cây con trái và phải
        if root.left is not None:
            self._find_price(root.left, min_price, max_price, result)
        if root.right is not None:
            self._find_price(root.right, min_price, max_price, result)

    def search(self, price):
        # Tìm kiếm giá trị trong cây
        return self._search(self.root, price)

    def _search(self, root, price):
        if root is None:
            return f"Giá trị {price} không tồn tại trong cây."
        if root.key == price:
            return f"Đã tìm thấy: {root.info}"
        elif price < root.key:
            return self._search(root.left, price)
        else:
            return self._search(root.right, price)

# Tạo danh sách điện thoại
lstPhone = [
    {"price": 3000, "name": "phone A"},
    {"price": 2000, "name": "phone B"},
    {"price": 1000, "name": "phone C"},
    {"price": 5000, "name": "phone D"},
    {"price": 6000, "name": "phone E"},
    {"price": 7000, "name": "phone F"},
    {"price": 4000, "name": "phone G"}
]

# Tạo cây BST và chèn các phần tử
tree = BSTree()
for phone in lstPhone:
    tree.insert_node(phone)

# In cây theo thứ tự in-order
print("Cây BST theo thứ tự in-order:")
print(tree.get_tree_in_order())

# In cây theo thứ tự pre-order
print("\nCây BST theo thứ tự pre-order:")
print(tree.get_tree_pre_order())

# In cây theo thứ tự post-order
print("\nCây BST theo thứ tự post-order:")
print(tree.get_tree_post_order())

