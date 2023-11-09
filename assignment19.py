def average_word_length(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            total_words = len(words)
            total_length = sum(len(word) for word in words)
            if total_words > 0:
                avg_length = total_length / total_words
            else:
                avg_length = 0

            return avg_length
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = "daily_logs.txt" 
    avg_length = average_word_length(file_path)
    
    if avg_length is not None:
        print(f"Average word length in the text file: {avg_length:.2f}")
    else:
        print("File not found.")