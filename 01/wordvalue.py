from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    scrab_words = open(DICTIONARY, 'r')
    words = [x.strip() for x in scrab_words.readlines()]
    scrab_words.close()
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word.upper():
        score += LETTER_SCORES.get(letter, None) or 0
    return score


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    hi_score = 0
    for word in words:
        score = calc_word_value(word)
        if score > hi_score:
            hi_score = score
            hi_word = word
    return hi_word

if __name__ == "__main__":
    pass  # run unittests to validate
