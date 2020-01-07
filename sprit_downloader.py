import urllib.request
from compat_ import urlopen
import random
import string
from concurrent import futures
import os, sys


class DLmanager():

    def __init__(self, queue, n, abs_path):
        self.output_list = []
        self.name = self.random_name()
        self.ext = queue['ext']
        self.dlbytes = queue['filesize']
        self.dl_bytes = 0
        self.dl_percent = 0
        print('id;', self.name)
        self.downloader(queue=queue, n=n, abs_path=abs_path)
        self.marginer(abs_path)
        self.delete_part()

    def random_name(self):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
        return ''.join(randlst)

    def spritter(self, queue, n):
        filesize = queue['filesize']
        a, b = divmod(filesize, n)
        sprit_list = []
        for i in range(n):
            if (i+1) == n:
                sprit_list += [[a * i + 1, filesize]]
            elif i == 0:
                sprit_list += [[0, a * (i + 1)]]
            else:
                sprit_list += [[a * i + 1, a * (i + 1)]]
        return sprit_list

    def downloader(self, queue, n, abs_path):
        download_list = self.spritter(queue, n)
        url = queue['url']
        i = 1
        future_list = []
        print('downloading')
        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            for part in download_list:
                headers = {'range': 'bytes={}-{}'.format(part[0], part[1])}
                if abs_path == '':
                    path = '{}.part{}'.format(self.name, i)
                else:
                    path = '{}/{}.part{}'.format(abs_path, self.name, i)
                self.output_list += [path]
                future = executor.submit(self.download_, url, path, headers)
                future_list.append(future)
                i += 1
            _ = futures.as_completed(future_list)

    def download_(self, url, path, headers):  # 書き込み処理
        with open(path, 'wb') as fh:
            for chunk in self.get(url, headers):
                length = len(chunk)
                self.dl_bytes += length
                self.dl_percent += (length * 100 /self.dlbytes)
                fh.write(chunk)

    def get(self, url, headers):
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        response = urlopen(req)
        return self.stream_response(response)

    def stream_response(self, response, chunk_size=8 * 1024):
        """Read the response in chunks."""
        while True:
            buf = response.read(chunk_size)
            if not buf:
                break
            yield buf

    def marginer(self, abs_path):
        print('file marging')
        with open('{}/{}.{}'.format(abs_path, self.name, self.ext), 'wb') as op:
            for part in self.output_list:
                data = open(part, 'rb')
                op.write(data.read())
                op.flush()
        print('merge finished')

    def delete_part(self):
        for part_ in self.output_list:
            os.remove(part_)
