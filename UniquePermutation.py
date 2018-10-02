import numpy as np
import string

alphabets = list(string.ascii_lowercase)
length = 7
sequence = np.random.choice(alphabets[:length], 1000)
remember = list()
starts_at = 0
for i in range(len(sequence)):
    if len(remember) != length:
        if sequence[i] in remember:
            remember.append(sequence[i])
            delete_till = remember.index(sequence[i])
            del(remember[0:delete_till+1])
            starts_at = starts_at + delete_till + 1
        else:
            remember.append(sequence[i])
    else:
        break

if len(remember) == length:
    print(sequence[starts_at:starts_at+length])
else:
    print('No String present')
