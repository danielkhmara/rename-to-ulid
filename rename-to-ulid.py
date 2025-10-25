import os
import ulid

base_dir = os.path.join(os.path.dirname(__file__), 'folder-for-rename')
for root, _, files in os.walk(base_dir):
   for f in sorted(files):
      path = os.path.join(root, f)
      ext = os.path.splitext(f)[1]
      new_name = str(ulid.new()) + ext
      new_path = os.path.join(root, new_name)
      os.rename(path, new_path)
