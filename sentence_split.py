from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import pickle
import string

punkt_param = PunktParameters()


def get_spliter():
    with open('vi.pkl', 'rb') as fs:
        punkt_param = pickle.load(fs)

    punkt_param.sent_starters = {}
    abbrev_types = ['g.m.t', 'e.g', 'dr', 'dr', 'vs', "000", 'mr', 'mrs', 'prof', 'inc', 'tp', 'ts', 'ths',
                    'th', 'vs', 'tp', 'k.l', 'a.w.a.k.e', 't', 'a.i', '</i', 'g.w',
                    'ass',
                    'u.n.c.l.e', 't.e.s.t', 'ths', 'd.c', 've…', 'ts', 'f.t', 'b.b', 'z.e', 's.g', 'm.p',
                    'g.u.y',
                    'l.c', 'g.i', 'j.f', 'r.r', 'v.i', 'm.h', 'a.s', 'bs', 'c.k', 'aug', 't.d.q', 'b…', 'ph',
                    'j.k', 'e.l', 'o.t', 's.a']
    abbrev_types.extend(string.ascii_uppercase)
    for abbrev_type in abbrev_types:
        punkt_param.abbrev_types.add(abbrev_type)
    for abbrev_type in string.ascii_lowercase:
        punkt_param.abbrev_types.add(abbrev_type)
    return PunktSentenceTokenizer(punkt_param)


count = 0
if __name__ == '__main__':
    sentences = '''Bà T trả cho ông S. 1 tỉ đồng. Khi quốc hội và BS. Bình qua Trung Quốc nhất trí xóa bỏ giới hạn nhiệm kỳ chủ tịch hồi tháng 3, Chủ tịch Tập Cận Bình dường như đã vươn tới đỉnh cao quyền lực trong nền chính trị nước này. Trong bối cảnh Tổng thống Mỹ Donald Trump gây hoang mang với những tuyên bố chỉ trích đồng minh, bài trừ tự do thương mại, ông Tập dường như cảm thấy đã đến lúc Trung Quốc vươn lên nắm vai trò lãnh đạo toàn cầu và hiện thực hóa "Giấc mơ Trung Hoa" của mình, theo SCMP.

    Một trong những công cụ quan trọng để ông Tập hiện thực hóa tham vọng toàn cầu của mình chính là sáng kiến "Vành đai và Con đường" nhằm vươn tầm ảnh hưởng đến nhiều quốc gia trên thế giới thông qua các dự án xây dựng cơ sở hạ tầng. Trong nước, ông tiếp tục đẩy mạnh chiến dịch chống tham nhũng "đả hổ, diệt ruồi" nhằm thu hút sự ủng hộ của dư luận và lực lượng vũ trang.

    Trong nửa đầu năm 2018, ông Tập liên tục xuất hiện ở các diễn đàn quốc tế quan trọng, nhấn mạnh về chính sách ủng hộ tự do thương mại và chống biến đổi khí hậu, xây dựng hình ảnh hoàn toàn đối lập với Trump trên trường quốc tế. Những tuyên bố của ông Tập cho thấy Trung Quốc dường như đang nỗ lực thách thức trật tự thế giới do Mỹ dẫn đầu trong lĩnh vực kinh tế và công nghệ.
    Khi quốc hội Trung Quốc nhất trí xóa bỏ giới hạn nhiệm kỳ chủ tịch hồi tháng 3, Chủ tịch Tập Cận Bình dường như đã vươn tới đỉnh cao quyền lực trong nền chính trị nước này. Trong bối cảnh Tổng thống Mỹ Donald Trump gây hoang mang với những tuyên bố chỉ trích đồng minh, bài trừ tự do thương mại, ông Tập dường như cảm thấy đã đến lúc Trung Quốc vươn lên nắm vai trò lãnh đạo toàn cầu và hiện thực hóa "Giấc mơ Trung Hoa" của mình, theo SCMP.

Một trong những công cụ quan trọng để ông Tập hiện thực hóa tham vọng toàn cầu của mình chính là sáng kiến "Vành đai và Con đường" nhằm vươn tầm ảnh hưởng đến nhiều quốc gia trên thế giới thông qua các dự án xây dựng cơ sở hạ tầng. Trong nước, ông tiếp tục đẩy mạnh chiến dịch chống tham nhũng "đả hổ, diệt ruồi" nhằm thu hút sự ủng hộ của dư luận và lực lượng vũ trang.

Trong nửa đầu năm 2018, ông Tập liên tục xuất hiện ở các diễn đàn quốc tế quan trọng, nhấn mạnh về chính sách ủng hộ tự do thương mại và chống biến đổi khí hậu, xây dựng hình ảnh hoàn toàn đối lập với Trump trên trường quốc tế. Những tuyên bố của ông Tập cho thấy Trung Quốc dường như đang nỗ lực thách thức trật tự thế giới do Mỹ dẫn đầu trong lĩnh vực kinh tế và công nghệ.

Tuy nhiên, tình hình dần xấu đi vào nửa sau của năm 2018, khi những thách thức liên tiếp trỗi dậy cả trong nước và quốc tế, đặt ông Tập vào tình thế khó khăn hơn rất nhiều.

Hồi tháng 6, Trump tuyên bố áp thuế đối với 50 tỷ USD hàng hóa của Trung Quốc, sau nhiều lần ám chỉ về một cuộc chiến tranh thương mại giữa hai siêu cường. Động thái này của Trump dường như khiến Bắc Kinh bất ngờ, khi trước đó truyền thông và một số học giả hàng đầu nước này vẫn khẳng định kinh tế Trung Quốc có thể soán ngôi Mỹ trong tương lai gần. Trung Quốc sau đó đáp trả bằng đòn áp thuế tương tự với hàng hóa Mỹ.

Sự cứng rắn của Trung Quốc khiến Trump quyết định tung ra đòn áp thuế thứ hai, nhắm vào 200 tỷ USD hàng hóa nước này, đẩy cuộc chiến tranh thương mại lên cao trào với động thái trả đũa của Trung Quốc áp thuế lên toàn bộ hàng hóa nhập khẩu từ Mỹ còn lại trị giá 60 tỷ USD. Tuy nhiên, dư luận nước này bắt đầu đặt câu hỏi về chiến lược "ăn miếng trả miếng" với Mỹ, khi nhiều học giả công khai chỉ trích cách tiếp cận quá cứng rắn của nước này trong chiến tranh thương mại.

Yan Xuetong, viện trưởng Viện Quan hệ Quốc tế tại Đại học Thanh Hoa, cảnh báo rằng Trung Quốc có nguy cơ quay trở lại tình trạng trì trệ và bị cô lập như trong thời kỳ Mao Trạch Đông. "Khi Trump áp dụng chiến lược bảo hộ, Trung Quốc nên mở cửa và buộc các doanh nghiệp nhà nước cải cách. Nhưng chả ai phản ứng với lời tôi nói. Không ai nghe tôi". Trên mạng xã hội, một loạt chuyên gia kinh tế, học giả nổi tiếng Trung Quốc cũng có những phản ứng tương tự.

Những học giả này cho rằng nếu Trung Quốc không tỏ ra quá tự tin và kiêu ngạo về sức mạnh của mình thông qua sáng kiến "Vành đai và Con đường" cũng như chương trình "Made in China 2025", Mỹ có thể đã không tung ra những đòn đánh quyết liệt như vậy.

"Vành đai và Con đường", sáng kiến được coi là tâm huyết do ông Tập khởi xướng từ năm 2013, không chỉ khiến các chuyên gia Trung Quốc hoài nghi, nó còn bộc lộ nhiều nhược điểm và liên tục phải đối mặt với những lời chỉ trích trong năm qua. Nhiều "siêu dự án" trong sáng kiến này bị phê phán là đội giá gấp nhiều lần so với giá trị thực, năng lực nhà thầu Trung Quốc yếu kém, không quan tâm tới nhu cầu phát triển của quốc gia sở tại mà chỉ phục vụ lợi ích chiến lược của Bắc Kinh.

Ở châu Phi, dự án đường sắt Nairobi-Mombasa thua lỗ trầm trọng sau một năm vận hành, khi các doanh nghiệp địa phương vẫn kiên quyết sử dụng phương tiện đường bộ để vận tải hàng hóa trên tuyến đường chiến lược này. Ở Sri Lanka, chính phủ nước này lâm vào nợ nần khi tham gia sáng kiến "Vành đai và Con đường" đến mức phải bàn giao cảng chiến lược Hambantota cho Trung Quốc quản lý.

Nhiều quốc gia cũng bắt đầu cảnh giác với nguy cơ "sập bẫy nợ" khi tham gia sáng kiến. Tân Thủ tướng Pakistan Imran Khan đã quyết định cắt giảm 2 tỷ USD trong dự án đường sắt thuộc Hành lang Kinh tế Trung Quốc - Pakistan (CPEC) bởi "Pakistan là nước nghèo, không thể kham nổi gánh nặng từ những khoản nợ khổng lồ".

Thủ tướng Malaysia Mahathir Mohamad đã hủy các dự án tỷ USD với Trung Quốc vì cho rằng các điều khoản của chúng quá bất lợi cho Kuala Lumpur. Ngay cả Myanmar, nước có quan hệ thân cận với Trung Quốc, cũng đã giảm giá trị dự án xây cảng nước sâu Kyaukpyu từ 7,2 tỷ USD xuống còn 1,3 tỷ USD.

Không chỉ các dự án trong sáng kiến "Vành đai và Con đường", nhiều tập đoàn công nghệ Trung Quốc trong năm qua cũng hứng chịu những chỉ trích ngày càng lớn từ các nước phương Tây về hành vi gián điệp kinh tế. Mỹ và một loạt đồng minh như Australia, New Zealand, Canada, Nhật... đã "cấm cửa" tập đoàn Huawei tham gia vào các dự án xây dựng mạng 5G vì lo ngại nguy cơ an ninh.'''
    sentence_splitter = get_spliter()
    sentences = sentences.replace("\n"," ")
    #print(sentences)
    for sentence in sentence_splitter.sentences_from_text(sentences):
        print(sentence)
