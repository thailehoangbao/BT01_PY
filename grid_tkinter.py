import customtkinter
customtkinter.set_default_color_theme("green") # green, dark-blue, blue
customtkinter.set_appearance_mode("light") # system ,light, dark


# Khởi tạo giao diện
root = customtkinter.CTk()

root.title("cyberlearn")
#Chiều rộng , cao
root.geometry("400x400")
for column in range(0,2):
    # ảnh hưởng theo cột
    root.columnconfigure(column,weight=1)
    root.rowconfigure(column,weight=1)


frame = customtkinter.CTkFrame(master=root,fg_color="red")
frame.grid(row=0,column=0,sticky="nesw")

frame2 = customtkinter.CTkFrame(master=root,fg_color="blue")
frame2.grid(row=1,column=1,sticky="nesw")

frame3 = customtkinter.CTkFrame(master=root,fg_color="green")
frame3.grid(row=1,column=0,sticky="nesw")

frame4 = customtkinter.CTkFrame(master=root,fg_color="yellow")
frame4.grid(row=0,column=1,sticky="nesw")
root.mainloop()