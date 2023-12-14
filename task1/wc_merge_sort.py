import sys

def merge_sort(words):
    if len(words) > 1:
        mid = len(words) // 2
        left_half = words[:mid]
        right_half = words[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                words[k] = left_half[i]
                i += 1
            else:
                words[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            words[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            words[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_wrapper(words):
    merge_sort(words)

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        # Read words from each line and store them in a list
        words = [line.strip() for line in file]

        # Perform merge sort on the list of words
        merge_sort_wrapper(words)

        # Print the sorted words
        print("Sorted words:")
        for word in words:
            print(word)
            pass

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
