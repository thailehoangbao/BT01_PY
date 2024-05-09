# py -m pip install customtkinter
import customtkinter
customtkinter.set_default_color_theme("green") # green, dark-blue, blue
customtkinter.set_appearance_mode("light") # system ,light, dark


# Khởi tạo giao diện
root = customtkinter.CTk()

root.title("cyberlearn")
#Chiều rộng , cao
root.geometry("400x400")

#frame (khung chứa dữ liệu chủ yếu để di chuyển trong giao diện) 
# cách xấp xếp dữ liệu trong frame
#1/pack
#2/place
#3/grid
#tham số 1: master => để quyết định thằng nào chứa nó
frameTop = customtkinter.CTkFrame(master=root,fg_color="white")
frameTop.pack(side="top", fill="both", expand=True)


#side = top, bottom, left, right (vị trí của frame)
#expand = True ( canh giửa )
# fill = both , x = chiều ngang , y= chiều cao, both = giãn ra cả 2 (điền hết không gian của frame)
frameblue = customtkinter.CTkFrame(master=frameTop, fg_color="blue")
frameblue.pack(side="left", fill="both", expand=True)

# Frame bottom
framered = customtkinter.CTkFrame(master=frameTop, fg_color="red")
framered.pack(side="right", fill="both", expand=True)


frameBottom = customtkinter.CTkFrame(master=root,fg_color="white")
frameBottom.pack(side="bottom", fill="both", expand=True)
# Frame left
frameblack = customtkinter.CTkFrame(master=frameBottom, fg_color="black")
frameblack.pack(side="right", fill="both", expand=True)

# Frame right
frameyellow = customtkinter.CTkFrame(master=frameBottom, fg_color="yellow")
frameyellow.pack(side="left", fill="both", expand=True)



#widget


#class


#vòng lập giao diện
root.mainloop()