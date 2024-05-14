import customtkinter
customtkinter.set_default_color_theme("green") # green, dark-blue, blue
customtkinter.set_appearance_mode("light") # system ,light, dark


# Khởi tạo giao diện
root = customtkinter.CTk()

root.title("cyberlearn")
#Chiều rộng , cao
root.geometry("400x400")
entry = customtkinter.CTkEntry(root, placeholder_text="Hãy nhập dữ liệu",bg_color='black',fg_color="blue",text_color='white')
entry.pack()

def button_event(title):
    print(entry.get()) # lấy dữ liệu từ input

button = customtkinter.CTkButton(root, text="Bấm Nút", command=lambda: button_event("pressd"),text_color='white',bg_color='black',fg_color="blue")
button.pack()

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(root, text="CTkCheckBox", command=checkbox_event,
                                        variable=check_var, onvalue="on", offvalue="off")


progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal")
progressbar.pack()

checkbox.pack()


def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(root, from_=0, to=100, command=slider_event)
slider.pack()
#py -m pip install Pillow
from PIL import Image

my_image = customtkinter.CTkImage(light_image=Image.open("./img/cach-do-la-ban.jpg"),
                                    dark_image=Image.open("./img/cach-do-la-ban.jpg"),
                                    size=(100 , 100))

image_label = customtkinter.CTkLabel(root, image=my_image, text="")  # display image with a CTkLabel
image_label.pack()
root.mainloop()