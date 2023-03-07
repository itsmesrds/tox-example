import os
import concurrent.futures

# specify the directory path to read the file names
directory_path = 'C:/Users/username/Desktop/'

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
def write_file_names_to_file(directory_path, output_file_name):
    # create a thread pool executor with 5 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # submit the write_file_names function to the executor
        future = executor.submit(write_file_names, directory_path)
        file_list = future.result()

    # open the output file in write mode
    with open(output_file_name, 'w') as file:
        # write each file name to the output file
        for file_name in file_list:
            file.write(file_name + '\n')

    print("File names written to file: ", output_file_name)

# call the write_file_names_to_file function
write_file_names_to_file(directory_path, output_file_name)
