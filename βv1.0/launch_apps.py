import os
import subprocess

def launch_apps_from_folder(folder_path):
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                try:
                    subprocess.Popen(item_path, shell=True)
                    print(f"{item_path} を起動しました。")
                except Exception as e:
                    try:
                        os.startfile(item_path)
                        print(f"{item_path} を起動しました。")
                    except Exception as e:
                        print(f"{item_path} の起動に失敗しました: {e}")
            else:
                print(f"{item_path} はファイルではありません。")
    except Exception as e:
        print(f"フォルダの読み込みに失敗しました: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    folder_path = os.path.join(script_dir, 'apps')
    launch_apps_from_folder(folder_path)

