import os
import shutil

def backup(source_dir, dest_dir):
    try:
        # Get the list of files in source directory
        file_list = os.listdir(source_dir)
        
        # Loop through files and copy to destination if they are new or modified
        for file in file_list:
            source_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)
            
            # Check if the file is newer in the source directory or not present in the destination
            if os.path.isfile(source_path) and (not os.path.exists(dest_path) or os.path.getmtime(source_path) > os.path.getmtime(dest_path)):
                shutil.copy2(source_path, dest_path)  # Copy with metadata
                
                print(f"File '{file}' backed up successfully.")
        
        print("Backup completed.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Defining source and backup directories
    source_directory = "/home/phani557/Python-and-Bash-Scripting"
    backup_directory = "/tmp/pythonscriptsbackupdir"
    # Backing up source directory into backup directory using backup function defined above
    backup(source_directory,backup_directory)