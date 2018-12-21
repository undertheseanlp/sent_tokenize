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
    text = 'Vào giữa những năm 1990, BS. Diệp Giản Minh, sinh năm 1977, có công kiem duoc $55.000.000 việc đơn giản trong một khu rừng.'
    text = 'Trong những ngày qua, khi “Mệnh lệnh 02” của Giám đốc Công an TP Hà Nội về việc lập lại trật tự giao thông đô thị đã nhận được sự đồng tình ủng hộ của đa số người dân thủ đô. Hàng nghìn trường hợp vi phạm trật tự giao thông đô thị đã được cơ quan chức năng trên toàn địa bàn TP Hà Nội xử lí. Tuy nhiên một số bất cập đã được lực lượng Công an thống kê và đề xuất với cơ quan quản lí Nhà nước.'
    text = 'The University of Chicago Press là một địa chỉ uy tín để các độc giả tìm đọc về Hayek.Dự án Collected Works of F. A. Hayek của họ đã cho xuất bản 19 tác phẩm và một quyển tự truyện của Hayek với sự biên tập kỹ lưỡng và tổng hợp thêm các bài phỏng vấn, bài báo nghiên cứu và thư tay, và một số bản thảo chưa được công bố của Hayek.'
    for sent in sentence_splitter.tokenize(text):
        print(sent)

