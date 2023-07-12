import re
import string


def get_text() -> str:
    """
    This function contains value of text to have it encapsulated.
    :return: Unformed text.
    """
    return """tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.




it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.




last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def normalize_text(text: str) -> str:
    """
    This function provides normalization of existing text to lower case,
    replacing iz to is (where needed) and capitalizing each sentence.
    :param text: Initial text from get_text() function.
    :return: Normalized text with all the sentences starting with upper case.
    """
    sentences = re.split(r'(?<=[.])\s+', text)
    capitalized_sentences = [sentence.lower().replace(' iz ', ' is ').capitalize() for sentence in sentences]
    return ' '.join(capitalized_sentences)


def make_sentence_from_last_words(capitalized_text: str) -> str:
    """
    This function creates a sentence from the last word of each sentence of the text.
    :param capitalized_text: result of execution of normalize_text() function.
    :return: a sentence created from the last word of each sentence.
    """
    last_words = re.findall(r'[a-z0-9]+\.', capitalized_text)
    last_sentence = [word[:-1] for word in last_words[:-1]] + last_words[-1:]
    return ' '.join(last_sentence).capitalize()


def placing_sentence_to_final_text(capitalized_text: str, formatted_sentence: str) -> str:
    """
    This function adds sentence from make_sentence_from_last_words() function to
    normalized text to have all the text ready.
    :param capitalized_text: result of execution of normalize_text() function.
    :param formatted_sentence: result of execution of make_sentence_from_last_words() function.
    :return: final version of text which is normalized and contains final version of text.
    """
    sentences = re.split(r'(?<=[.])\s+', capitalized_text)
    return (' '.join(sentences[0:3]) + formatted_sentence + ' '.join(sentences[3:])).replace(".", ".\n")


def calculate_whitespaces(text: str) -> int:
    """
    This function counts all the whitespaces which can be present in text using string.whitespace for
    further iteration.
    :param text: Original unformed text.
    :return: Quantity of whitespaces from the text in int format.
    """
    sum_spaces = 0
    for symbol in string.whitespace:
        sum_spaces += text.count(symbol)
    return sum_spaces


initial_text = get_text()
normalized_text = normalize_text(initial_text)
added_sentence = make_sentence_from_last_words(normalized_text)
print(placing_sentence_to_final_text(normalized_text, added_sentence))
print(f'Total quantity of whitespaces with my code is {calculate_whitespaces(initial_text)}')
