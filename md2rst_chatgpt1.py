import os
import subprocess

input_folder = 'markdown'
output_folder = 'source/Years'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith('.md'):
            input_path = os.path.join(root, filename)
            rel_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, os.path.splitext(rel_path)[0] + '.rst')
            output_folder_path = os.path.dirname(output_path)
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)
            subprocess.run(['pandoc', '-f', 'markdown', '-t', 'rst', '-o', output_path, input_path])

