import os

# Helper function to create a directory if it doesn't exist
def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")

# Function to log errors
def log_error(message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(message + "\n")

# Function to check if a file exists
def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        print(f"File '{file_path}' not found.")
        return False

# Function to clean up audio file paths
def get_audio_file_path(audio_folder, file_name):
    return os.path.join(audio_folder, file_name)

