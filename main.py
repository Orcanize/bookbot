def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    count_characters = get_count_characters(text)
    count_letters = remove_non_letters(count_characters)
    letters_list = list_of_dict(count_letters)

    #sort the list (does not need new variable, as it would then output "None" Grrrr)
    letters_list.sort(reverse=True, key=sort_on)

    # text output start of report
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print("")
    
    # print the whole report of each letter line
    for values in letters_list:
        print(f"The '{values['letter']}' character was found {values['count']} times")

    # text output end of report
    print("--- End report ---")


# reads the book.txt file
def get_book_text(path):
    with open(path) as f:
        return f.read()    

# word count calculation
def get_num_words(text):
    words = text.split()
    return len(words)

# character count calculation
def get_count_characters(text):
    lower_text = text.lower()
    dict = {}
    for char in lower_text:
        if char in dict:
            dict[char] += 1
        # adds characters not in dictionary
        else:
            dict[char] = 1
    return dict

# new dictionary with only the letters
def remove_non_letters(count_characters):
    letter_dict = {}
    letters = ("abcdefghijklmnopqrstuvwxyz") 
    for char in count_characters:
        if char in letters:
                letter_dict[char] = count_characters[char]
    return letter_dict

# necessary to rearrange the dictionary into a nested one to sort
def list_of_dict(count_letters):
    dict_list = []
    for letter in count_letters:
        dict_list.append({"letter" : letter, "count" : count_letters[letter]})
    return dict_list

# necessary for the .sort function to know how to sort
def sort_on(letters_list):
    return letters_list["count"]


main()