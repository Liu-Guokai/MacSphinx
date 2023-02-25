import os

sphinx_dir = 'source/2024'

index_file_path = os.path.join(sphinx_dir, 'index.rst')

with open(index_file_path, 'w') as f:
    f.write(f"{os.path.basename(sphinx_dir)}\n{'='*len(os.path.basename(sphinx_dir))}\n\n")
    f.write(".. toctree::\n")
    f.write("   :maxdepth: 2\n\n")
    for root, dirs, files in os.walk(sphinx_dir):
        rel_path = os.path.relpath(root, sphinx_dir)
        for filename in files:
            if filename.endswith('.rst') and filename != 'index.rst':
                f.write(f"   {os.path.join(rel_path, os.path.splitext(filename)[0])}\n")
    f.write('\n')





