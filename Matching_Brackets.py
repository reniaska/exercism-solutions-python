#https://exercism.org/tracks/python/exercises/matching-brackets

def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if len(stack) == 0:
                return False
            last_in_stack = stack.pop()
            if char == ')':
                if last_in_stack != '(':
                    return False
            if char == '}':
                if last_in_stack != '{':
                    return False
            if char == ']':
                if last_in_stack != '[':
                    return False

    return len(stack) == 0