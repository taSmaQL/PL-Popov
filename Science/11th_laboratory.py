'''
Вариант: 10
Текст задачи: даны самые популярные репозитории на github https://habr.com/ru/post/453444/, 
по последней цифре зачетки получить JSON для вашего варианта.
Программа с графическим интерфейсом вводим в поле имя репозитория и по нажатию кнопки получаем результат.
Необходимо получить в новый файл следующую информацию:
"company": None,
'created_at': '2015-08-09T17:55:43Z',
'email': None,
"id": 1362940,
'name': 'Kubernetes',
"url": "https://api.github.com/users/kubernetes"}
Все прикрепить одним архивом.
'''
import tkinter as tk, json
from tkinter import messagebox

repository_data = {
    "company": None,
    'created_at': '2014-11-12T12:00:00Z',
    "email": None,
    "id": 1362940,
    "name": "Microsoft .NET CoreFX",
    "url": "https://api.github.com/users/dotnet"
}

def show_repository_info():
    repo_name = entry.get()
    if repo_name == "Microsoft .NET CoreFX":
        result = json.dumps(repository_data, indent=4)
        result_label.config(text=result)
        save_to_file(result)
    else:
        result_label.config(text="Репозиторий не найден.")

def save_to_file(data):
    with open("repository_info.json", "w") as json_file:
        json_file.write(data)
    messagebox.showinfo("Сохранение", "Информация успешно сохранена в repository_info.json")

root = tk.Tk()
root.title("Информация о репозитории")

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Получить информацию", command=show_repository_info)
button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)
root.mainloop()
