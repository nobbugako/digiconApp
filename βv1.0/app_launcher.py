import os
import tkinter as tk
from tkinter import messagebox
from launch_apps import launch_apps_from_folder

def on_button_click():
    script_dir = os.path.dirname(__file__)
    folder_path = os.path.join(script_dir, 'apps')
    try:
        launch_apps_from_folder(folder_path)
    except Exception as e:
        messagebox.showerror("エラー", f"アプリの起動に失敗しました: {e}")
        print(f"エラー: {e}")

# メインウィンドウの作成
root = tk.Tk()
root.title("アプリを起動するアプリ")
root.geometry("600x400")

# タイトルラベル
title_label = tk.Label(root, text="アプリを起動するアプリ", font=("Arial", 24))
title_label.pack(pady=20)

# 画像の読み込み
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'sozai', '起動ボタン - コピー.png')  # 画像ファイルのパスを指定
button_image = tk.PhotoImage(file=image_path)


# ボタン
button = tk.Button(root, image=button_image, command=on_button_click)
button.pack(pady=20)

# バージョンラベル
version_label = tk.Label(root, text="v1.0", font=("Arial", 10))
version_label.pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=10)

# メインループの開始
root.mainloop()
