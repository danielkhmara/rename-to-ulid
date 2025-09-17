import os
import ulid

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, "folder-for-rename")

for filename in os.listdir(folder_path):
   file_path = os.path.join(folder_path, filename)
   if os.path.isfile(file_path):
      ext = os.path.splitext(filename)[1]
      new_name = f"{ulid.new()}{ext}"
      new_path = os.path.join(folder_path, new_name)
      os.rename(file_path, new_path)