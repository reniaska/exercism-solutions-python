# https://exercism.org/tracks/python/exercises/secret-handshake

def commands(binary_str):
    code = []
    if binary_str[-1] == '1':
        code.append('wink')
    if binary_str[-2] == '1':
        code.append('double blink')
    if binary_str[-3] == '1':
        code.append('close your eyes')
    if binary_str[-4] == '1':
        code.append('jump')
    if binary_str[0] == '1':
        return code[::-1]
    else:
        return code
