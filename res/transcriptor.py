def transcript(input_lang, output_lang, word):
    if input_lang=="en" and output_lang=="ru":
        print("In future.")
    if input_lang=="ru" and output_lang=="en":
        new_word_letters=[]
        word_chars=list(word)
        for letter in word_chars:
            if letter=='а':
                new_word_letters.append('a')
            if letter=='б':
                new_word_letters.append('b')
            if letter=='в':
                new_word_letters.append('v')
            if letter=='г':
                new_word_letters.append('g')
            if letter=='д':
                new_word_letters.append('d')
            if letter=='е':
                new_word_letters.append('e')
            if letter=='ё':
                new_word_letters.append('jo')
            if letter=='ж':
                new_word_letters.append('zh')
            if letter=='з':
                new_word_letters.append('z')
            if letter=='и':
                new_word_letters.append('i')
            if letter=='й':
                new_word_letters.append('i')
            if letter=='к':
                new_word_letters.append('k')
            if letter=='л':
                new_word_letters.append('l')
            if letter=='м':
                new_word_letters.append('m')
            if letter=='н':
                new_word_letters.append('n')

            if letter=='о':
                new_word_letters.append('o')
            if letter=='п':
                new_word_letters.append('p')
            if letter=='р':
                new_word_letters.append('r')
            if letter=='с':
                new_word_letters.append('s')
            if letter=='т':
                new_word_letters.append('t')
            if letter=='у':
                new_word_letters.append('u')
            if letter=='ф':
                new_word_letters.append('f')
            if letter=='х':
                new_word_letters.append('x')
            if letter=='ц':
                new_word_letters.append('c')
            if letter=='ч':
                new_word_letters.append('ch')
            if letter=='ш':
                new_word_letters.append('sh')
            if letter=='щ':
                new_word_letters.append('sh')
            if letter=='ъ':
                new_word_letters.append('"')
            if letter=='ы':
                new_word_letters.append('i')
            if letter=='ь':
                new_word_letters.append("'")
            if letter=='э':
                new_word_letters.append('e')
            if letter=='ю':
                new_word_letters.append('ju')
            if letter=='я':
                new_word_letters.append('ja')
            if letter==' ':
                new_word_letters.append(' ')

        new_word = ''.join(new_word_letters)

    return(new_word)