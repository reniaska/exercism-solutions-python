# https://exercism.org/tracks/python/exercises/crypto-square

def cipher_text(plain_text):
    plain_text = "".join([character.lower() for character in plain_text if character.isalnum()])
    num_rows = round(len(plain_text) ** 0.5)
    if num_rows * num_rows >= len(plain_text):
        num_cols = num_rows
    else:
        num_cols = num_rows + 1
    plain_text += ' ' * (num_rows * num_cols - len(plain_text))

    message = ''
    for row in range(num_cols):
        message += "".join(list(plain_text)[row::num_cols])
        if num_rows > 1 and row < num_cols - 1:
            message += " "

    return message
