import tkinter as tk


def add():
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(int(number1_entry.get()) + int(number2_entry.get())))


def sub():
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(int(number1_entry.get()) - int(number2_entry.get())))


def mul():
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(int(number1_entry.get()) * int(number2_entry.get())))


def div():
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(int(number1_entry.get()) / int(number2_entry.get())))

window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x500')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=10, height=4, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=10, height=4, command=sub)
button_sub.place(x=180, y=200)
button_mul = tk.Button(window, text='x', width=10, height=4, command=mul)
button_mul.place(x=100, y=272)
button_div = tk.Button(window, text='/', width=10, height=4, command=div)
button_div.place(x=180, y=272)

number1_entry = tk.Entry(window, width=26)
number1_entry.place(x=100, y=20)
number2_entry = tk.Entry(window, width=26)
number2_entry.place(x=100, y=40)
answer_entry = tk.Entry(window, width=26)
answer_entry.place(x=100, y=100)

number1 = tk.Label(window, text='Первое')
number1.place(x=50, y=20)
number2 = tk.Label(window, text='Второе')
number2.place(x=50, y=40)
answer = tk.Label(window, text='Результат:')
answer.place(x=40, y=100)
window.mainloop()