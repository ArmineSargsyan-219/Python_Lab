import os

def read_file_safe(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
        with open(filename, 'r') as file:
            content = file.read()
        return content

    except FileNotFoundError as fnf_error:
        return str(fnf_error)

    except IOError as io_error:
        return f"An I/O error occurred: {io_error}"
    
print(read_file_safe('data.txt'))

print(read_file_safe('missing.txt'))

