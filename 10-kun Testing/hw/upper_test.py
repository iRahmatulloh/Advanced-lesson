from random import shuffle, randintfrom upper import upper_evenOdddef shuffle_word():    word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    num = randint(3, 18)    count = 0    while word:        if count == num:            break        else:            word.append(' ')        count += 1    shuffle(word)    return ''.join(word)def upper_Odd(txt: str, even_odd: str) -> str:    res = ""    for ind, st in enumerate(txt):        if even_odd.lower() == 'juft':            if st == ' ':                res += st            elif ind % 2 != 0:                res += st.upper()            else:                res += st        elif even_odd.lower() == 'toq':            if st == ' ':                res += st            elif ind % 2 == 0:                res += st.upper()            else:                res += st        else:            raise ValueError("Siz 'even_odd'ga xato qiymat bergansiz! ")    return resdef testUpper_toq():    for _ in range(101):        save_shuffle = shuffle_word()        assert upper_Odd(save_shuffle, 'toq') == upper_evenOdd(save_shuffle, 'toq')def testUpper_juft():    for _ in range(101):        save_shuffle = shuffle_word()        assert upper_Odd(save_shuffle, 'juft') == upper_evenOdd(save_shuffle, 'juft')