import sys

def quick_sort(words):
    if len(words) <= 1:
        return words
    else:
        pivot = words[0]
        less = [word for word in words[1:] if word < pivot]
        greater = [word for word in words[1:] if word >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        # Read words from each line and store them in a list
        words = [line.strip() for line in file]

        # Perform quicksort on the list of words
        sorted_words = quick_sort(words)

        # Print the sorted words
        print("Sorted words:")
        for word in sorted_words:
            print(word)
            pass

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
