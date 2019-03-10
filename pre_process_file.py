#! /usr/bin/env python3
'''
    author: timothy c. siwula
    date: sun march 10th 2019
    file: ~/code/emoji/pre_process_file.py
    purpose: clean and extract all emoji keys from emoji.md
             for later use in a emoji dictionary module.
    run: chmod +x pre_process_file.py && ./pre_process_file.py
'''

# 1. for each unique string in emoji.md
# 2. add it to a set, no duplicates, persist ':' prefix and postfix
# 3. write one emoji string per line to emoji.txt
# 4. add support for utf and random sampling

# Step 1.
import os

# assemble path, filename & uri
path = os.getcwd()
filename = 'emoji.md'
uri = os.path.join(path, filename)

# assert esistence
if os.path.exists(uri) and os.path.isfile(uri):
    print("uri confirmed")

# reading contents of files
emoji_file = open(uri)
file_content = emoji_file.read()

# ...



# ...

# Step 3.
# writing to files
