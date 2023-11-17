#https://exercism.org/tracks/python/exercises/transpose

def transpose(lines):
    rows = lines.split('\n')
    rows = [row.replace(' ', '_').ljust(len(max(rows, key=len))) for row in rows]
    return '\n'.join(''.join(row).rstrip(' ').replace('_', ' ') for row in zip(*rows))