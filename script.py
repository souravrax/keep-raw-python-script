import os
from collections import defaultdict

cwd = os.getcwd()
print(cwd)

raw_files = set()

extension_to_keep = ".cr3"
extension_to_remove = ".cr3"

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.lower().endswith(extension_to_keep):
            filePath = os.path.join(root, file)
            raw_files.add(file[:-len(extension_to_keep)])

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.lower().endswith(extension_to_remove) and file[:-len(extension_to_remove)] in raw_files:
            filePath = os.path.join(root, file)
            os.remove(filePath)

print(raw_files)