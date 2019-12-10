import youtube_dl

class extract_information():

    def __init__(self):
        self.ydl = youtube_dl.YoutubeDL()

    def extract_(self, url):  # htmlからデータ抽出
        return self.ydl.extract_info(url, download=False)

    def extract_formats(self, result):  #extractのデータを代入すると動画データのリストを返す4
        return result['formats']

#ここまで必須

    def get_title(self, result):    #タイトル取得
        title = result['title']
        return title


    def get_data_amount(self, format, round_=False):  #データ容量を返す（Mｂ）
        amount = format['filesize']

        if round_ is not True:
            return amount

        else:
            if amount:
                amount = round(float(amount) / (1024 ** 2))
                return amount
            else:
                return False

    def is_audio_only(self, format):    #音声のみか
        if format['acodec']:
            return True
        else:
            return False

    def is_video_only(self, format):    #動画のみか（60fps, 1080pは動画のみ。あとで音声とくっつける必要あり）
        if format['vcodec']:
            return True
        else:
            return False

    def return_format(self, format):    #動画フォーマットを返す（１０８０Pなど,　音声の場合はtinyを返す・）
        format_note = format['format_note']
        if format_note == 'tiny':
            return '音声'
        else:
            return format_note

    def return_link(self, fomrat):
        return format['url']

    def return_only_mp4(self, formats):
        return_list = []
        for element in formats:
            ext = element['ext']
            if ext == 'mp4':
                return_list += [element]
        return return_list

    def return_only_m4a(self, formats):
        return_list = []
        for element in formats:
            ext = element['ext']
            if ext == 'm4a':
                return_list += [element]
        return return_list

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=g96k0UimW-o"
    a = extract_information()
    results = a.extract_(url=url)
    formats = a.extract_formats(results)
    print(formats)
    mp4 = a.return_only_mp4(formats)
    m4a = a.return_only_m4a(formats)
    print(mp4[0]['url'])
