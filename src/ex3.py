
def create_files(input_file):
    large_word = set()
    small_word = set()
    with open(f'files/{input_file}', "r") as text_file:
        while True:
            line = text_file.readline()
            if not line:
                 break
            line = line.split()
            for word in line:
                word = word.replace(".","")
                word = word.replace("?","")
                
                if (len(word) > 2):
                    large_word.add(word)
                
                else:
                    small_word.add(word)
    
    with open("large-words.txt", "w") as large_word_txt:
        for word in large_word:
            large_word_txt.writelines(word + "\n")

    with open("small-words.txt", "w") as small_word_txt:
        for word in small_word:
            small_word_txt.writelines(word + "\n")






def ex3():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")

ex3()