from pathlib import Path # Import Path from pathlib module
current_dir=Path.cwd() # Get the current working directory
current_file=Path(__file__).name # Get the current file name

print(f"Files in {current_dir}:") # Print the current directory

for filepath in current_dir.iterdir(): # Iterate over each file in the current directory
    if filepath.name==current_file: 
        continue # Skip the current file to avoid reading itself

    print(f" - {filepath.name}") # Print the file name

    if filepath.is_file(): # Check if the path is a file
        content = filepath.read_text(encoding='utf-8') # Read the file content
        print(f"   Content:{content}") # Print the file content