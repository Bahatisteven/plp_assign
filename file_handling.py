# week 4 file handling and exceptions

def process_file():
    try:
        # read the content from input.txt
        with open("input.txt", "r") as infile:
            content = infile.read()
        
        # count the number of words
        word_count = len(content.split())
        
        # convert the text to uppercase
        upper_content = content.upper()
        
        # write the processed text and word count to output.txt
        with open("output.txt", "w") as outfile:
            outfile.write(upper_content)
            outfile.write(f"\n\nWord Count: {word_count}")
        
        print("Successfully created 'output.txt' with processed content and word count.")
    
    except FileNotFoundError:
        print("Error: 'input.txt' file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# run the function
process_file()

# week four assignment 
def file_read_write_with_error_handling():
    try:
        filename = "input.txt"
        
        # try to open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # example modification: reverse the lines
        modified_lines = lines[::-1]
        
        # prepare new filename
        new_filename = "modified_" + filename
        
        # write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)
        
        print(f"Successfully wrote modified content to '{new_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
file_read_write_with_error_handling()
