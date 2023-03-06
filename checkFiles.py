import os

# specify the directory path to validate the file names
directory_path = 'C:/Users/username/Desktop/'

# specify the list of file names to compare against
file_names = ['file1.txt', 'file2.docx', 'file3.pdf']

# function to validate the file names in the directory
def validate_file_names(directory_path, file_names):
    # get all the file names present in the directory
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_list.append(file)

    # initialize two lists to store matched and unmatched file names
    matched_files = []
    unmatched_files = []

    # check if all the file names in the list are present in the directory
    for name in file_names:
        if name in file_list:
            matched_files.append(name)
        else:
            unmatched_files.append(name)

    # check if there are any extra files present in the directory
    for file in file_list:
        if file not in file_names:
            unmatched_files.append(file)

    # return the two lists of matched and unmatched file names
    return matched_files, unmatched_files

# call the validate_file_names function and print the result
matched_files, unmatched_files = validate_file_names(directory_path, file_names)

print("Total matched files: ", len(matched_files))
print("Matched files: ", matched_files)
print("Total unmatched files: ", len(unmatched_files))
print("Unmatched files: ", unmatched_files)
