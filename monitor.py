import os
import hashlib
import time

# Define the directory to monitor (current directory)
directory_to_monitor = os.getcwd()

# Create a dictionary to store file hashes
file_hashes = {}

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read the file in 64KB chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def monitor_directory():
    while True:
        new_file_hashes = {}
        
        # Walk through the current directory and calculate hashes for all files
        for root, _, files in os.walk(directory_to_monitor):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)
                new_file_hashes[file_path] = file_hash

        # Check for changes in file hashes
        for file_path, new_hash in new_file_hashes.items():
            if file_hashes.get(file_path) != new_hash:
                print(f"File {file_path} has changed!")

        file_hashes = new_file_hashes  # Update the file_hashes dictionary

        time.sleep(5)  # Check for changes every 5 seconds

if __name__ == '__main__':
    monitor_directory()