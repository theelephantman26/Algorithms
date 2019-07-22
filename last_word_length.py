def theLastWord(s):
    length = 0
    first_word_seen = False
    if s is '' or s is None:
        return 0
    else:
        for i in range(len(s)-1, -1, -1):
            if s[i] is ' ' and first_word_seen:
                return length
            elif s[i] != ' ' and not first_word_seen:
                length = length + 1
                first_word_seen = True
            elif s[i] != ' ' and first_word_seen:
                length = length + 1
        return length
            

print(theLastWord('a '))