import customtkinter as ctk
from tkinter import Canvas, Scrollbar, Frame
from PIL import Image, ImageTk

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Tên Của Bạn")
root.geometry("650x500")  # Kích thước cửa sổ lớn hơn để chứa danh sách sản phẩm

# Khung chính
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill=ctk.BOTH, expand=1)

# Canvas để chứa các sản phẩm
canvas = Canvas(main_frame)
canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=1)

# Thanh cuộn dọc
scrollbar = ctk.CTkScrollbar(main_frame, orientation=ctk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

# Cấu hình Canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Khung chứa các sản phẩm
product_frame = ctk.CTkFrame(canvas)

# Thêm khung chứa vào Canvas
canvas.create_window((0, 1), window=product_frame, anchor="center")

# Tạo hình ảnh sản phẩm
def load_image(path, size):
    img = Image.open(path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Đường dẫn hình ảnh sản phẩm
image_path = "img/iphone.jpg"
product_image = load_image(image_path, (150, 150))

# Số lượng sản phẩm (giả sử có 20 sản phẩm)
num_products = 20
products_per_row = 4

# Tạo các sản phẩm
for i in range(num_products):
    row = i // products_per_row
    column = i % products_per_row
    
    # Khung con cho mỗi sản phẩm
    product_sub_frame = ctk.CTkFrame(product_frame)
    product_sub_frame.grid(row=row, column=column, padx=10, pady=10)
    
    # Hình ảnh sản phẩm
    product_label = ctk.CTkLabel(product_sub_frame, image=product_image, text="")
    product_label.pack()
    
    # Tiêu đề sản phẩm
    title_label = ctk.CTkLabel(product_sub_frame, text=f"iphone{i}")
    title_label.pack()

    # Mô Tả sản phẩm
    desc_product = ctk.CTkLabel(product_sub_frame, text="Hàng chính hãng")
    desc_product.pack()
    
    # Nút bấm "Mua Hàng"
    buy_button = ctk.CTkButton(product_sub_frame, text="Mua Hàng")
    buy_button.pack()

# Bắt đầu vòng lặp chính của ứng dụng
root.mainloop()
