import string

def characterSort(strings):
    if len(strings)==0:
        return ''
    else:
        joined_characters = list(''.join(strings))
        final_string_to_sort = []
        for char in joined_characters:
            if char in string.ascii_lowercase:
                final_string_to_sort.append(char)
        final_string_to_sort.sort()
        return ''.join(final_string_to_sort)

input = ['#','dcab']
print(characterSort(input))
