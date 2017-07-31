# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, lets call it a glossary.
# Think of five programming words youve learned about in the previous chapters. Use these words as the keys in your
# glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its
# meaning, or print the word on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning pair in your output.

programming_lang = {'Progarm1': 'Progarm1 meaning', 'Progarm2': 'Progarm2 meaning', 'Progarm3': 'Progarm3 meaning'}
# print(person_details['first_name'])
# print(person_details['last_name'])
# print(person_details['age'])
# print(person_details['city'])

# Do it with for or while loop
for i in programming_lang:
    print ((i),'meaning is: ', programming_lang[i])

