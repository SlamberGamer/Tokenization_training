from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize
from nltk.tokenize import RegexpTokenizer
regex_tokenizer = RegexpTokenizer('\?', gaps = True)

tox = RegexpTokenizer('[.!?.,]')
#test
# ("!", "?", ".", “,”)

tcase1 = "Excuse me, where can I find a chicken rice shop?"
tans1 = ["Excuse me", "where can I find a chicken rice shop"]

tcase2 = "OMG!!! It is Friday....where should we go for dinner?"
tans2 = ["OMG", "It is Friday", "where should we go for dinner"]

tcase3 = "He’s nervous, but on the surface he looks calm and ready."
tans3 = ["He’s nervous", "but on the surface he looks calm and ready"]

# print(tox.tokenize(tcase1))
regexp_tokenize(tcase1, '[.!?.,]')
print(regex_tokenizer)
# print(sent_tokenize(tcase3))

def tokenise(input):
  tokenise_words = word_tokenize(input)
  stop_words = ("!", "?", ".")
  print(tokenise_words)
  remove = [word for word in tokenise_words if word not in stop_words]
  final_string = ' '.join(remove)
  print(final_string)

# tokenise(tcase1)
  # result = ''
  # print('Pass' if result == expected_output else 'Failed!')

# tokenise(tcase1, tans1)
# tokenise(tcase2, tans2)
# tokenise(tcase3, tans3)