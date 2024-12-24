
def camel_case_check(words,variableName):
    #convert it to lower case
    variableName = variableName[0].lower() + variableName[1:]

    #create a list
    array = [] 

    current_word = '' #empty string

    for i in variableName:
        if i.isupper(): #If a capital letter is found
            if current_word:
                array.append(current_word)#he current word is completed and added to split_words.
            current_word = i.lower()#A new word begins, starting with the lowercase version of the capital letter.

        else:
            current_word+=i
    
    if current_word:
        array.append(current_word)

    
    return all(word in words for word in array)

# Test cases
print(camel_case_check(["is", "valid", "right"], "isValid"))  # True
print(camel_case_check(["is", "valid", "right"], "IsValid"))  # True
print(camel_case_check(["is", "valid", "right"], "isValId"))  # False


