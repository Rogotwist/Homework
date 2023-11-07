import tkinter as tk

def get_data():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()

    print(f"Имя: {name}")
    print(f"Адрес: {address}")
    print(f"Телефон: {phone}")

app = tk.Tk()
app.title("Ввод данных")

name_label = tk.Label(app, text="Имя:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

address_label = tk.Label(app, text="Адрес:")
address_label.pack()
address_entry = tk.Entry(app)
address_entry.pack()

phone_label = tk.Label(app, text="Телефон:")
phone_label.pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

submit_button = tk.Button(app, text="Отправить", command=get_data)
submit_button.pack()

app.mainloop()
