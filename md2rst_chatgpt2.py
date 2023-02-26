# import os

# sphinx_dir = 'source/2024'

# index_file_path = os.path.join(sphinx_dir, 'index.rst')

# with open(index_file_path, 'w') as f:
#     f.write(f"{os.path.basename(sphinx_dir)}\n{'='*len(os.path.basename(sphinx_dir))}\n\n")
#     f.write(".. toctree::\n")
#     f.write("   :maxdepth: 2\n\n")
#     for root, dirs, files in os.walk(sphinx_dir):
#         rel_path = os.path.relpath(root, sphinx_dir)
#         for filename in files:
#             if filename.endswith('.rst') and filename != 'index.rst':
#                 f.write(f"   {os.path.join(rel_path, os.path.splitext(filename)[0])}\n")
#     f.write('\n')



import os


# os.remove('source/2024')
os.system('python md2rst_chatgpt1.py')



def generate_index_file(folder_path):
    """Generate .rst index file for a folder containing subfolders."""

    # Check if the folder contains subfolders
    subfolders = [subfolder for subfolder in os.listdir(folder_path)
                  if os.path.isdir(os.path.join(folder_path, subfolder))]
    if not subfolders:
        # The folder does not contain any subfolders, so no index file is needed
        return

    # Generate the .rst index file
    index_path = os.path.join(folder_path, 'index.rst')
    with open(index_path, 'w') as f:
        f.write('{}\n'.format(folder_path))
        f.write('{}\n'.format('=' * len(folder_path)))
        f.write('\n')

        for subfolder in sorted(subfolders):
            subfolder_path = os.path.join(folder_path, subfolder)
            f.write('{}\n'.format(subfolder))
            f.write('{}\n'.format('-' * len(subfolder)))
            f.write('\n')
            generate_index_file(subfolder_path)

        for file in sorted(os.listdir(folder_path)):
            if file.endswith('.rst'):
                file_path = os.path.join(folder_path, file)
                f.write('{}\n'.format(file))
                f.write('{}\n'.format('-' * len(file)))
                f.write('\n')
generate_index_file('source/2024')