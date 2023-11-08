#https://exercism.org/tracks/python/exercises/diamond

def rows(letter):
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    idx = letters.index(letter)
    arr = []
    for level in range(0, 2 * idx +1):
        line = ''
        for j in range(0, 2 * idx + 1):
            if level <= idx:
                if j == idx-level or j == idx + level:
                    line += letters[level]
                else:
                    line += ' '
            else:
                if j == level - idx or j == 3 * idx - level:
                    line += letters[2 * idx - level]
                else:
                    line += ' '
        arr.append(line)
    return arr