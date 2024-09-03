import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

def get_external_folder_path(relative_path):
    """外部のフォルダを参照する"""
    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def launch_apps_from_folder(folder_path):
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                try:
                    subprocess.Popen(item_path, shell=True)
                    print(f"{item_path} を起動しました。")
                except Exception as e:
                    print(f"{item_path} の起動に失敗しました: {e}")
                    messagebox.showerror("エラー", f"{item_path} の起動に失敗しました: {e}")
            else:
                print(f"{item_path} はファイルではありません。")
    except Exception as e:
        print(f"フォルダの読み込みに失敗しました: {e}")
        messagebox.showerror("エラー", f"フォルダの読み込みに失敗しました: {e}")

def on_button_click(folder):
    folder_path = get_external_folder_path(os.path.join('起動したいものを入れてね', folder))
    print(f"Trying to access folder: {folder_path}")
    if not os.path.exists(folder_path):
        error_message = f"{folder} フォルダが見つかりません。"
        print(error_message)
        messagebox.showerror("エラー", error_message)
        return
    launch_apps_from_folder(folder_path)

def open_help_pdf():
    pdf_path = get_external_folder_path('使い方マニュアルアプリのみ.pdf')
    try:
        os.startfile(pdf_path)
    except Exception as e:
        messagebox.showerror("エラー", f"PDFファイルを開くことができませんでした: {e}")

root = tk.Tk()
root.title("アプリを起動するアプリ")
root.geometry("800x400")

background_image_path = get_external_folder_path('sozai/のっぶの力作(修正版).png')
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(root, width=background_photo.width(), height=background_photo.height())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

button_a_image_path = get_external_folder_path('sozai/Aボタン.png')
button_image_a = ImageTk.PhotoImage(Image.open(button_a_image_path))

button_b_image_path = get_external_folder_path('sozai/Bボタン.png')
button_image_b = ImageTk.PhotoImage(Image.open(button_b_image_path))

button_c_image_path = get_external_folder_path('sozai/Cボタン.png')
button_image_c = ImageTk.PhotoImage(Image.open(button_c_image_path))

help_icon_path = get_external_folder_path('sozai/ヘルプA.png')
help_icon_img = Image.open(help_icon_path)
help_icon_img = help_icon_img.resize((100, 50), Image.Resampling.LANCZOS)
help_icon_image = ImageTk.PhotoImage(help_icon_img)

button_a = tk.Button(root, image=button_image_a, command=lambda: on_button_click('A'))
canvas.create_window(200, 200, window=button_a)

button_b = tk.Button(root, image=button_image_b, command=lambda: on_button_click('B'))
canvas.create_window(400, 200, window=button_b)

button_c = tk.Button(root, image=button_image_c, command=lambda: on_button_click('C'))
canvas.create_window(600, 200, window=button_c)

help_button = tk.Button(root, image=help_icon_image, command=open_help_pdf)
canvas.create_window(50, 350, window=help_button)

version_label = tk.Label(root, text="ver. 1.1", font=("Arial", 10), bg="white")
canvas.create_window(750, 370, window=version_label)

root.mainloop()
