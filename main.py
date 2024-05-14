import customtkinter as ctk

# Tạo một cửa sổ chính (main window)
root = ctk.CTk()

# Đặt kích thước của cửa sổ
root.geometry("500x300")

# Đặt tiêu đề của cửa sổ
root.title("Thái Lê Hoàng Bảo")

# Không cho phép thay đổi kích thước của cửa sổ
root.resizable(False, False)

# Khởi động vòng lặp chính của ứng dụng
root.mainloop()