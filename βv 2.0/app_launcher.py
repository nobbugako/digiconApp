import os
import tkinter as tk
from tkinter import messagebox
from launch_apps import launch_apps_from_folder

def on_button_click(folder):
    script_dir = os.path.dirname(__file__)
    folder_path = os.path.join(script_dir, 'apps', folder)
    try:
        launch_apps_from_folder(folder_path)
    except Exception as e:
        messagebox.showerror("エラー", f"{folder} のアプリの起動に失敗しました: {e}")
        print(f"エラー: {e}")

# メインウィンドウの作成
root = tk.Tk()
root.title("アプリを起動するアプリ")
root.geometry("800x400")  # ウィンドウサイズを調整

# タイトルラベル
title_label = tk.Label(root, text="アプリを起動するアプリ", font=("Arial", 24))
title_label.pack(pady=20)

# 画像の読み込み
script_dir = os.path.dirname(__file__)
image_path_a = os.path.join(script_dir, 'sozai', 'A.png')  # 画像ファイルのパスを指定
image_path_b = os.path.join(script_dir, 'sozai', 'B.png')  # 画像ファイルのパスを指定
image_path_c = os.path.join(script_dir, 'sozai', 'ｼｨｨｨ.png')  # 画像ファイルのパスを指定
button_image_a = tk.PhotoImage(file=image_path_a)
button_image_b = tk.PhotoImage(file=image_path_b)
button_image_c = tk.PhotoImage(file=image_path_c)

# ボタンフレームの作成
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# ボタンA
button_a = tk.Button(button_frame, image=button_image_a, command=lambda: on_button_click('A'))
button_a.pack(side=tk.LEFT, padx=10)

# ボタンB
button_b = tk.Button(button_frame, image=button_image_b, command=lambda: on_button_click('B'))
button_b.pack(side=tk.LEFT, padx=10)

# ボタンC
button_c = tk.Button(button_frame, image=button_image_c, command=lambda: on_button_click('C'))
button_c.pack(side=tk.LEFT, padx=10)

# バージョンラベル
version_label = tk.Label(root, text="βv2.0", font=("Arial", 10))
version_label.pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=10)

# メインループの開始
root.mainloop()
