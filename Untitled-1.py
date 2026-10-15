import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Main window")
window.geometry("600x600")

canvas = tkinter.Canvas(width=600, height=600, bg="white")

# font_style = ("Times New Roman", 20)
# label = tkinter.Label(text="Логин", font=font_style)

# поле логина
label = tkinter.Label(text="Логин")
label.place(x=20, y=20)

login_var = tkinter.StringVar()
entry_login = tkinter.Entry(textvariable=login_var)
entry_login.place(x=20, y=50)
# поле пароля
label_password = tkinter.Label(text="Пароль")
label_password.place(x=20, y=80)

password_var = tkinter.StringVar()
entry_password = tkinter.Entry(textvariable=password_var)
entry_password.place(x=20, y=110)
# кнопки


# кнопка входа
def func_success():
    l = len(login_var.get())
    # login_var.set(login_var.get().replace(" ", "")) 
    
    if l == 0:
        messagebox.showerror("Неккоретный логин", "Логин пустой")
    elif " " in login_var.get():
        messagebox.showerror("Неккоретный логин", "Логин содержит пробел")
    else:
        messagebox.showinfo("Вход", "Вы успешно вошли в систему")
    
btn_success = tkinter.Button(text="Вход", command=func_success)
btn_success.place(x=20, y=140)
# кнопка отмена
def func_error():
    messagebox.showinfo("Отмена", "Вы отменили вход в систему")

btn_error = tkinter.Button(text="Отмена", command=func_error)
btn_error.place(x=120, y=140)

canvas.pack()
window.mainloop()