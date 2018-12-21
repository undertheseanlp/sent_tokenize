from nltk.tokenize.punkt import PunktTrainer
import pickle

PUNCTUATION = (';', '.', '!', '?',)
trainer = PunktTrainer()
trainer.INCLUDE_ALL_COLLOCS = True

with open('./corpus.txt', 'r') as fs:
    text = fs.read()

trainer.train(text, verbose=True)
params = trainer.get_params()
with open('./egs/punkt_tokenize/vi.pkl', 'wb') as fs:
    pickle.dump(params, fs)
