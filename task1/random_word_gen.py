import random
import string

def generate_random_word(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_and_save_words(file_path, num_words):
    with open(file_path, 'w') as file:
        for _ in range(num_words):
            word = generate_random_word()
            file.write(word + '\n')

def main():
    sizes = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]

    for size in sizes:
        file_path = f'random_words_{size}.txt'
        generate_and_save_words(file_path, size)
        print(f"Generated and saved {size} random words in {file_path}")

if __name__ == "__main__":
    main()
