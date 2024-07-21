import subprocess
import re

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(command)}:")
        print(e.stderr)
        return None

def parse_git_status(status_output):
    deleted_files = []
    new_files = []
    for line in status_output.split('\n'):
        if line.startswith('\tdeleted:'):
            deleted_files.append(line.split(':')[-1].strip())
        elif line.startswith('\tnew file:'):
            new_files.append(line.split(':')[-1].strip())
    return deleted_files, new_files

def find_rename_pairs(deleted_files, new_files):
    rename_pairs = []
    for deleted in deleted_files:
        deleted_base = re.sub(r'\d+\.', '', deleted)
        for new in new_files:
            new_base = re.sub(r'\d+\.', '', new)
            if deleted_base == new_base:
                rename_pairs.append((deleted, new))
                break
    return rename_pairs

def main():
    # Stage all changes
    run_git_command(["git", "add", "-A"])

    # Get Git status
    status_output = run_git_command(["git", "status"])
    print("Current Git status:")
    print(status_output)

    # Parse Git status
    deleted_files, new_files = parse_git_status(status_output)

    # Find rename pairs
    rename_pairs = find_rename_pairs(deleted_files, new_files)

    # Perform git mv for each pair
    for old_file, new_file in rename_pairs:
        print(f"Renaming: {old_file} -> {new_file}")
        run_git_command(["git", "mv", "--force", old_file, new_file])

    # Show final status
    final_status = run_git_command(["git", "status"])
    print("\nFinal Git status:")
    print(final_status)

    # Commit changes
    commit_message = input("Enter commit message (default: 'Batch rename files'): ").strip()
    if not commit_message:
        commit_message = "Batch rename files"
    
    result = run_git_command(["git", "commit", "-m", commit_message])
    
    if result is not None:
        print("\nChanges committed successfully.")
    else:
        print("\nFailed to commit changes.")

if __name__ == "__main__":
    main()