def count_digits_letters(sentence):
    #start writing your code here
    letters_count=0
    digits_count=0
    for i in sentence:
        if i.isalpha() and i!=" ":
            letters_count=letters_count+1
        elif i.isdigit() and i!=" ":
            digits_count=digits_count+1
        else:
            pass
    return [letters_count,digits_count]
    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
