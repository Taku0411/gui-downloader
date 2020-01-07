import youtube_dl


class extract_information():

    def __init__(self):
        self.ydl = youtube_dl.YoutubeDL()

    def extract_(self, url):  # htmlからデータ抽出
        return self.ydl.extract_info(url, download=False)

    def extract_formats(self, result):
        return result['formats']

    def get_title(self, result):
        title = result['title']
        return title

    def get_data_amount(self, format, round_=False):
        amount = format['filesize']

        if round_ is not True:
            return amount

        else:
            if amount:
                amount = round(float(amount) / (1024 ** 2))
                return amount
            else:
                return False

    def is_audio_only(self, format):
        if format['acodec']:
            return True
        else:
            return False

    def is_video_only(self, format):
        if format['vcodec']:
            return True
        else:
            return False

    def return_format(self, format):
        format_note = format['format_note']
        if format_note.find('tiny') >= 0:
            return '音声'
        else:
            return format_note

    def return_link(self, _format):
        return _format['url']

    def return_vcodec(self, _format):
        return _format['vcodec']

    def return_only_mp4(self, formats):
        return_list = []
        for element in formats:
            ext = element['ext']
            if ext == 'mp4':
                if 'avc'  in element['vcodec']:
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
    mp4 = a.return_only_mp4(formats)
    m4a = a.return_only_m4a(formats)
    print(mp4)
