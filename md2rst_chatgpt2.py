import os


# os.remove('source/2024')
os.system('python md2rst_chatgpt1.py')

import os

def generate_index_files(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Sort directories and files alphabetically
        dirnames.sort()
        filenames.sort()
        
        # Create the index file
        index_file_path = os.path.join(dirpath, "index.rst")
        with open(index_file_path, 'w') as f:
            # Write the folder name to the index file
            folder_name = os.path.basename(dirpath)
            f.write(f"{folder_name}\n")
            f.write("=" * len(folder_name) + "\n\n")
            
            # Write the table of contents to the index file
            f.write(".. toctree::\n")
            f.write("   :maxdepth: 2\n\n")
            
            for filename in filenames:
                # Ignore hidden files and non-.rst files
                if filename.startswith(".") or not filename.endswith(".rst") or filename == "index.rst":
                    continue
                
                # Write the file name to the index file
                f.write(f"   {os.path.splitext(filename)[0]}\n")
            
            # Write a blank line at the end of the file
            f.write("\n")
            
            # Generate index files for subfolders
            for dirname in dirnames:
                generate_index_files(os.path.join(dirpath, dirname))
                
                # Write a link to the subfolder's index file in the parent index file
                subfolder_index_path = os.path.join(dirname, "index")
                f.write(f"   {subfolder_index_path}\n")
            
            # Write a blank line at the end of the file
            f.write("\n")



generate_index_files('source/Years')