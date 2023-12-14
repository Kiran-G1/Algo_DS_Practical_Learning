import sys

def bubble_sort(words):
    n = len(words)

    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                # Swap the elements if they are in the wrong order
                words[j], words[j+1] = words[j+1], words[j]

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        # Read words from each line and store them in a list
        words = [line.strip() for line in file]

        # Perform bubble sort on the list of words
        bubble_sort(words)

        # Print the sorted words
        print("Sorted words:")
        for word in words:
            print(word)
            pass

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
