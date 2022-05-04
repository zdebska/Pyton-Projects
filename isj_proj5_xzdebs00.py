#!/usr/bin/env python3



def gen_quiz(qpool, *indexes, altcodes = 'ABCDEF', quiz=None):
    if not quiz:
        quiz = []
    for index in indexes:
        try:
            quiz.append((qpool[index][0], [": ".join(x) for x in zip(altcodes, qpool[index][1])]))
        except IndexError as error_txt:
            print(f"Ignoring index {index} - {error_txt}")
    return quiz
    

