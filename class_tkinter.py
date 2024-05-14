# Xây dựng một giao diện người dùng (GUI) sử dụng thư viện customtkinter trong Python, trong đó giao diện chứa 100 nút (button) và có khả năng cuộn (scroll). Mục tiêu là tạo ra một cửa sổ GUI mà người dùng có thể dễ dàng cuộn qua 100 nút.
import customtkinter
class FrameGrid(customtkinter.CTkScrollableFrame):
    def __init__(self,master,fg_color,bg_color):
        super().__init__(master=master,fg_color=fg_color,bg_color=bg_color)
        self.grid(row=0, column=0,sticky="nsew")

        for index in range(0, 101):
            button = customtkinter.CTkButton(
                self,
                text=f"Nút số: {index}",
                text_color='white',
                bg_color='black',
                fg_color="blue",
                command=lambda index=index: self.button_click(index)
            )
            button.pack(pady=10, padx=5)

    def button_click(self, index):
        print(f"Button {index} clicked")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cybersoft")
        self.geometry("800x600")
        for item in range(3):
            self.columnconfigure(item,weight=1)
            self.rowconfigure(item,weight=1)

        FrameGrid(self,"red","blue")

app = App()
for i in range(0,1):
    app.columnconfigure(i, weight=1)
    app.rowconfigure(i, weight=1)
app.mainloop()