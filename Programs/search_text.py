import os


def return_all_files(directory_path, file_types):
    """
    Method to return all the files, which matches the file type extension
    :param directory_path: directory/folder location for searching files.
            type: string
    :param file_types: Type of file to perform search.
            type: string
            example: .txt, .log, .xml etc..
    :return tuple
    """
    for root, directories, files in os.walk(directory_path):
        for file in files:
            if file.endswith(file_types):
              yield os.path.join(root, file)


def return_all_files_with_search_text(result_files, search_text):
    """
    Search all the files and if search_text is present then write into 'Tech_Made_Me_Lazy.log' file
    If any error found then skip the file and log the error.
    :param result_files: all the files to perform search operation
            type: tuple
    :param search_text: text to find in the files
            type: string
    :return: Writes down all logs to file Tech_Made_Me_Lazy.log'
    """
    output_file = open('Tech_Made_Me_Lazy.log', 'w')
    for file in result_files:
        try:
            with open(file) as f:
                if search_text in f.read():
                    output_file.write('Found text in :' + file + '\n')
        except Exception as error:
            output_file.write('Skipping file:' + file + '\n')
            output_file.write(str(error) + '\n')


directory_path = input('Enter directory or folder location to search : ').strip()
print('Directory :', directory_path)

file_types = tuple(str(x).strip() for x in input('Enter file types to search :').split(','))
print('File Types :', file_types)

search_text = input('Enter text to search :')
print('Search text :', search_text)

result_files = [f for f in return_all_files(directory_path, file_types)]
print('Total Number of files found :', result_files.__len__())

return_all_files_with_search_text(result_files, search_text)

# --------------------------------------
# How to run
# C:\Tech_Made_Me_Lazy\Python\Tech_Made_Me_Lazy_Python\programs>python search_text.py
# Enter directory or folder location to search : C:\Users\sdad\Downloads\Project Documents
# Directory : C:\Users\sdad\Downloads\Project Documents
# Enter file types to search :.txt, .log
# File Types : ('.txt', '.log')
# Enter text to search :the
# Search text : the
# Total Number of files found : 159
