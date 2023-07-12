import re
import string

text = """tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.




it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.




last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# normalizing text with splitting by regexp pattern and using list comprehension to generate a list of normalized sentences
# with replaced iz in proper places. Then merging text to have it organized as text
sentences = re.split(r'(?<=[.])\s+', text)
capitalized_sentences = [sentence.lower().replace(' iz ', ' is ').capitalize() for sentence in sentences]
capitalized_text = ' '.join(capitalized_sentences)

# finding last word of each sentence by using findall function
# for last_sentence we are adding slice of each item to remove . sign
# then we are joining and capitalizing this sentence.
last_words = re.findall(r'[a-z0-9]+\.', capitalized_text)
last_sentence = [word[:-1] for word in last_words[:-1]] + last_words[-1:]
formatted_sentence = ' '.join(last_sentence).capitalize()

# inserting sentence of last words into text.
sentences = re.split(r'(?<=[.])\s+', capitalized_text)
final_text = (' '.join(sentences[0:3]) + formatted_sentence + ' '.join(sentences[3:])).replace(".", ".\n")

# creating a variable to contain value of all the possible spacing chars
# iterating over string.whitespace.
sum_spaces = 0
for symbol in string.whitespace:
    sum_spaces += text.count(symbol)

# Output of final text
print(final_text)

#Output of
print(f'Total quantity of whitespaces with my code is {sum_spaces}')
