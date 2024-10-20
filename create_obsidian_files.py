import os
import datetime
import sys

# Get the Obsidian vault path from environment variable
OBSIDIAN_VAULT_PATH = os.environ.get('OBSIDIAN_VAULT_PATH')

if not OBSIDIAN_VAULT_PATH:
    print("Error: OBSIDIAN_VAULT_PATH environment variable is not set.")
    exit(1)

def create_file(file_path, common_tag):
    full_path = os.path.join(OBSIDIAN_VAULT_PATH, file_path)
    directory = os.path.dirname(full_path)
    
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Create the file if it doesn't exist
    if not os.path.exists(full_path):
        with open(full_path, 'w') as f:
            f.write(f"#{common_tag}\n")
        print(f"Created: {full_path}")
    else:
        print(f"File already exists: {full_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python create_obsidian_files.py <common_tag> <file1> <file2> ...")
        exit(1)

    common_tag = sys.argv[1]
    files_to_create = sys.argv[2:]

    # Create files
    for file in files_to_create:
        # Replace {{date}} with current date
        file = file.replace("{{date}}", datetime.datetime.now().strftime("%Y-%m-%d"))
        create_file(file, common_tag)

    print("File creation complete.")

if __name__ == "__main__":
    main()

    ython create_obsidian_files.py project_alpha "Daily Notes/{{date}}.md" "Projects/Alpha/tasks.md" "Ideas/alpha_brainstorm.md" "Research/alpha_resources.md"