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
    for sent in sentence_splitter.tokenize(
            'Vào giữa những năm 1990, BS. Diệp Giản Minh, sinh năm 1977, có công kiem duoc $55.000.000 việc đơn giản trong một khu rừng. 20 năm sau, ông ta đứng trên một đế chế kinh doanh trị giá 44 tỷ USD. Nhưng giờ đây, đế chế đó đã sụp đổ và Diệp đang bị điều tra, theo CNN.'):
        print(sent)
