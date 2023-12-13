def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    sorted_characters = chars_count_to_sorted_list(character_count)
    print(f"{num_words} words found in the document.")
    
    for character in sorted_characters:
        print(f"The character '{character['char']}' was used {character['num']} times.")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words(text):
    return len(text.split())

def sort_on(d):
    return d["num"]

def chars_count_to_sorted_list(character_count):
    sorted_list = []
    
    for character in character_count:
        if character.isalpha():
            sorted_list.append({"char": character, "num": character_count[character]})
            
    return sorted(sorted_list, reverse=True, key=sort_on)

def get_character_count(text):
    characters = {}
    
    for character in text.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
        
    return characters

main()
