# Task5 - WORD COUNT TOOL
import string

def count_words(text):
    """Count the number of words in the given text."""
    if not text:
        raise ValueError("The text is empty.")
    
    # Remove punctuation and split text into words
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
    
    # Count the number of words
    word_count = len(words)
    return word_count

def main():
    try:
        while True:
            choice = input("Do you want to input text (1) or read from a file (2)? (1/2): ")
            
            if choice == '1':
                text = input("Enter the text: ")
                word_count = count_words(text)
                print("Word count:", word_count)
            elif choice == '2':
                filename = input("Enter the filename: ")
                try:
                    with open(filename, 'r') as file:
                        text = file.read()
                        word_count = count_words(text)
                        print("Word count:", word_count)
                except FileNotFoundError:
                    print("Error: File not found.")
                except Exception as e:
                    print("Error:", e)
            else:
                print("Invalid choice. Please enter '1' or '2'.")

            another_text = input("Do you want to count words in another text? (yes/no): ").lower()
            if another_text != 'yes':
                break
                
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
