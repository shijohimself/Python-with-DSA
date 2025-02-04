my_str = "python is good language"

def longestWord(string):
    longest_word = ""
    current_word = ""
    for ch in string:
        if ch == " ":
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""
        else:
            current_word += ch
    if len(current_word) > len(longest_word):
        longest_word = current_word
    return longest_word

print(longestWord(my_str))
