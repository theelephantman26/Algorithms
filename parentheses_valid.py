def longestValidParentheses1(s):
    """
    :type s: str
    :rtype: int
    """
    list_s = list(s)
    longest_string = ''
    buffer = ''
    check = 0
    for i in range(len(list_s)):
        if buffer is not '':
            if list_s[i] is '(' and list_s[i-1] is ')':
                buffer = buffer + list_s[i]
                check = check+1
            if list_s[i] is ')' and list_s[i-1] is '(':
                buffer = buffer + list_s[i]
                check = check-1

            if list_s[i] is '(' and list_s[i-1] is '(':
                buffer = ''
                check = 0
                buffer = buffer + list_s[i]
                check = check+1
            if list_s[i] is ')' and list_s[i-1] is ')':
                buffer = ''
                check = 0
                buffer = buffer + list_s[i]
                check = check-1
        else:
            if list_s[i] is '(':
                buffer = buffer + list_s[i]
                check = check+1

        if check is 0:
            if len(longest_string) < len(buffer):
                longest_string = buffer
    return longest_string

def longestValidParentheses2(s):
    """
    :type s: str
    :rtype: int
    """
    list_s = list(s)
    register = list()
    open_paren_stack = []
    in_process = False
    register.append('')
    max_length = 0
    buffer = ''
    for i in range(len(list_s)):
        if list_s[i] is '(':
            if len(open_paren_stack) is 0:
                in_process = True
            open_paren_stack.append(list_s[i])
        if list_s[i] is ')':
            if len(open_paren_stack) is 0:
                in_process = False
                register.append('')
            if in_process is True:
                buffer = buffer + open_paren_stack[-1] + ')'
                del(open_paren_stack[-1])
                if len(open_paren_stack) is 0:
                    register[-1] = register[-1]+buffer
                    buffer = ''
    register.append(buffer)
    print(register)
    for string in register:
        if max_length < len(string):
            max_length = len(string)
    return max_length

def longestValidParentheses(s):
    s = list(s)
    register = list()
    stack = list()

    if len(s) is 0:
        return 0
    for i in range(len(s)):
        if s[i] is '(':
            stack.append(i)
        else:
            if len(stack) is 0:
                continue
            else:
                if stack[-1] is i-1:
                    if len(register) > 0 and len(register[-1]) > 0 and register[-1][-1] is stack[-1]-1:
                        register[-1].append(stack[-1])
                        register[-1].append(i)
                    else:
                        register.append([stack[-1],i])
                    del(stack[-1])
                else:
                    for j in range(len(register)):
                        if len(register[j]) > 0:
                            if register[j][0] == stack[-1]+1 and register[j][-1] == i-1:
                                register[j].insert(0, stack[-1])
                                register[j].append(i)
                                del(stack[-1])
                                break
                if len(register) > 1 and register[-1][0] is register[-2][-1]+1:
                    register[-2] = register[-2]+register[-1]
                    del(register[-1])
    print(register)
    max_len = 0
    for sub_string in register:
        if len(sub_string) > max_len:
            max_len = len(sub_string)
    return max_len

print(longestValidParentheses("(()())"))
