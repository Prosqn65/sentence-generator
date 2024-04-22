import os
import json
import random

def load_dictionary(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def generate_sentence(word_dict, min_length, max_length):
    sentence_length = random.randint(min_length, max_length)
    sentence = []
    for _ in range(sentence_length):
        pos = random.choice(list(word_dict.keys()))
        word = random.choice(word_dict[pos])
        sentence.append(word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dictionary_file = os.path.join(script_dir, "word_dictionary.json")
    word_dict = load_dictionary(dictionary_file)
    num_sentences = input("Enter number of sentences: ")
    if not num_sentences.isdigit():
        print("Invalid input. Please enter a valid number.")
        return
    num_sentences = int(num_sentences)
    min_sentence_length = 3
    max_sentence_length = 10

    all_sentences = []

    for _ in range(num_sentences):
        sentence = generate_sentence(word_dict, min_sentence_length, max_sentence_length)
        all_sentences.append(sentence)

    all_sentences_row = '. '.join(all_sentences)
    print(all_sentences_row)

if __name__ == "__main__":
    main()
