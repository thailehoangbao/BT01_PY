import customtkinter
customtkinter.set_default_color_theme("green") # green, dark-blue, blue
customtkinter.set_appearance_mode("light") # system ,light, dark


# Khởi tạo giao diện
root = customtkinter.CTk()

root.title("cyberlearn")
#Chiều rộng , cao
root.geometry("400x400")

#place

# relx cách lề trái
# rely cách lề trên
# relwidth chiều rộng
# relheight chiều cao
# frame.place(relwidth=0.5,relheight=0.5,relx=0.25,rely=0.25)
framered = customtkinter.CTkFrame(master=root,fg_color="red")
framered.place(relwidth=0.5,relheight=0.5,relx=0,rely=0)


frameblue = customtkinter.CTkFrame(master=root,fg_color="blue")
frameblue.place(relwidth=0.5,relheight=0.5,relx=0.5,rely=0)

frameyellow = customtkinter.CTkFrame(master=root,fg_color="yellow")
frameyellow.place(relwidth=0.5,relheight=0.5,relx=0.5,rely=0.5)


frameblack = customtkinter.CTkFrame(master=root,fg_color="black")
frameblack.place(relwidth=0.5,relheight=0.5,relx=0,rely=0.5)

root.mainloop()