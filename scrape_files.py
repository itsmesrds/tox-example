import os
import concurrent.futures

# specify the base directory paths to read the file names
base_directory_paths = ['C:/Users/username/Desktop/Folder1', 'C:/Users/username/Desktop/Folder2', 'C:/Users/username/Desktop/Folder3']

# specify the output file name to write the file names
output_file_name = 'file_names.txt'

# function to write the file names to a file
def write_file_names(directory_path):
    # get all the file names present in the directory
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_list.append(file_name)

    return file_list

# use multi-threading to write file names to file in parallel
def write_file_names_to_file(base_directory_paths, output_file_name):
    # create a thread pool executor with 5 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # submit the write_file_names function to the executor for each base directory path
        futures = []
        for directory_path in base_directory_paths:
            future = executor.submit(write_file_names, directory_path)
            futures.append(future)

        # get the file names returned by the write_file_names function for each base directory path
        file_list = []
        for future in concurrent.futures.as_completed(futures):
            file_list += future.result()

    # open the output file in write mode
    with open(output_file_name, 'w') as file:
        # write each file name to the output file
        for file_name in file_list:
            file.write(file_name + '\n')

    print("File names written to file: ", output_file_name)

# call the write_file_names_to_file function
write_file_names_to_file(base_directory_paths, output_file_name)
