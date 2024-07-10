# How would you read a file named data.txt and print its contents line by line?
def read_file_and_print(filename):
    """
    Reads a file and prints its contents line by line.

    Args:
    filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Use strip() to remove any leading/trailing whitespace, including newlines.
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


read_file_and_print('data.txt')
