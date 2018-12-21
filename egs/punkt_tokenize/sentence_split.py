from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

punkt_param = PunktParameters()
punkt_param.abbrev_types = {'g.m.t', 'e.g', 'dr', 'dr', 'vs', "000", 'mr', 'mrs', 'prof', 'inc', 'tp', 'ts', 'ths',
                            'th', 'vs', 'tp', 'k.l', 'a.w.a.k.e', 'a.i', '</i', 'g.w',
                            'ass',
                            'u.n.c.l.e', 't.e.s.t', 'ths', 'd.c', 've…', 'ts', 'f.t', 'b.b', 'z.e', 's.g', 'm.p',
                            'g.u.y',
                            'l.c', 'g.i', 'j.f', 'r.r', 'v.i', 'm.h', 'a.s', 'bs', 'c.k', 'aug', 't.d.q', 'b…', 'ph',
                            'j.k', 'e.l', 'o.t', 's.a'}
sentence_splitter = PunktSentenceTokenizer(punkt_param)
if __name__ == '__main__':
    text = 'Theo người nhà nạn nhân, T. bị dập não trước, gẫy lìa đùi trái, dập chân phải và bị đa chấn thương toàn thân. Hiện T. vẫn lúc tỉnh, lúc mê nên các bác sĩ vẫn chưa thể tiến hành phẫu thuật.'
    for sent in sentence_splitter.tokenize(text):
        print(sent)

