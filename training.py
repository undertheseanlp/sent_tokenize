from pprint import pprint
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

trainer = PunktTrainer()
trainer.INCLUDE_ALL_COLLOCS = True
# Corpus: One sentence per line
with open('./corpus/corpus_test.txt', 'r') as fs:
    text = fs.read()
rs = trainer.train(text)
abbrev_types = trainer.get_params().abbrev_types
print(abbrev_types)
