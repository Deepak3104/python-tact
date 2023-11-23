import re

def remove_index_and_full_stop(line):
    # Define a regular expression pattern to match index followed by a full stop
    pattern = re.compile(r'(\d+)\.')

    # Replace the matched pattern with an empty string (removing the index and full stop)
    modified_line = re.sub(pattern, '', line)

    return modified_line

def remove_quotes(line):
    # Replace quotes with an empty string
    modified_line = line.replace('"', '')

    return modified_line

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # Remove index and full stop, then remove quotes in each line
            modified_line = remove_quotes(remove_index_and_full_stop(line))

            # Write the result to the new file
            output_file.write(modified_line)

# Example usage:
input_file_path = 'lines.txt'
output_file_path = 'lines1.txt'
process_file(input_file_path, output_file_path)

print(f"Processing complete. Result saved to {output_file_path}")