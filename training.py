from pprint import pprint
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
import pickle
import string

PUNCTUATION = (';', '.', '!', '?',)
trainer = PunktTrainer()
trainer.INCLUDE_ALL_COLLOCS = True

with open('./corpus.txt', 'r') as fs:
    text = fs.read()

trainer.train(text, verbose=True)
params = trainer.get_params()
print(params.abbrev_types)
print(params.collocations)
print(params.sent_starters)
print(params)
with open('vi.pkl', 'wb') as fs:
    pickle.dump(params, fs)
