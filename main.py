def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    split_file = list(file_contents.split())
    counter = 0
    for word in split_file:
        counter += 1
    print(counter)
    



main()