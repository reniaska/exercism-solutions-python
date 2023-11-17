# https://exercism.org/tracks/python/exercises/wordy

def simple_operation(res, equation_list):
    if '+' in equation_list:
        result = res + int(equation_list[1])
    elif '-' in equation_list:
        result = res - int(equation_list[1])
    elif '*' in equation_list:
        result = res * int(equation_list[1])
    else:
        # '/' in equation_list
        result = res / float(equation_list[1])
    return result


def answer(question):
    question = question.replace('?', '').replace('What is', '').replace('minus', '-').replace(
        'plus', '+').replace('multiplied by', '*').replace('divided by', '/')
    question_list = question.split()
    if any([q.isalpha() for q in question_list]):
        raise ValueError("unknown operation")
    else:
        if len(question_list) == 1 and question_list[0].isdecimal():
            res = int(question_list[0])
        else:
            try:
                res = int(question_list[0])
                for i in range(0, len(question_list) - 1, 2):
                    res = simple_operation(res, question_list[i + 1: i + 3])
            except:
                raise ValueError("syntax error")
    return res
