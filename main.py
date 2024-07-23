def main():
    
    print("--- Begin report of books/frankenstein.txt ---")
    count_words()
    count = character_count()
    count = convert_to_list(count)
    count.sort(reverse=True, key=sort_on)
    for tup in count:
            print(f"The {tup[0]} character was found {tup[1]} times ")
    print("--- End Report ---")

def count_words():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        words = file_contents.split()
        count = 0
        for i in words:
            count += 1
        print(f"{count} words found in the document\n")


def character_count():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        lower_char = file_contents.lower()

        char_count = {}

        for i in lower_char:
            if i.isalpha():    
                if i not in char_count:
                    char_count[i] = 1
                else: 
                    char_count[i] += 1
        return char_count
    
def convert_to_list(dict):
    list1 = list(dict.items())
    return list1

def sort_on(tup):
    return tup[1]
                              
if __name__ == '__main__':
    main()