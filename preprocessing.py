import os

data_folder = 'openwebtext-master'
output_file = 'openwebtext.txt'

all_text = ''
num_files = 0

for subdir, _, files in os.walk(data_folder):
    for file in files:
        with open(os.path.join(subdir, file), 'r', encoding='utf-8', errors='ignore') as f:
            all_text += f.read()
            num_files += 1

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(all_text)

print(f"Combined {num_files} files into {output_file}")
