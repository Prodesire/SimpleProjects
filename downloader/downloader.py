import requests
import threading
import os


class Downloader:
    def __init__(self, url, filename=None, thread_num=5):
        self.url = url
        self.thread_num = thread_num
        self.filename = filename if filename else os.path.basename(url)
        head = requests.head(url)
        self.total = int(head.headers['Content-Length'])
        print('Total data length is', self.total)

    def get_data_range(self):
        offset = self.total // self.thread_num
        data_range = [(i * offset, '') if i == self.thread_num - 1
                      else (i * offset, (i + 1) * offset)
                      for i in range(self.thread_num)]
        return data_range

    def download(self, start, end):
        headers = {'Range': 'Bytes={}-{}'.format(start, end), 'Accept-Encoding': '*'}
        res = requests.get(self.url, headers=headers)
        print('Download data {}-{} success'.format(start, end))
        self._file.seek(start)
        self._file.write(res.content)

    def run(self):
        self._file = open(self.filename, 'wb')
        thread_list = []
        n = 0
        for each_range in self.get_data_range():
            print('Thread {} start {}-{}'.format(n, *each_range))
            n += 1
            t = threading.Thread(target=self.download, args=each_range)
            t.start()
            thread_list.append(t)

        for t in thread_list:
            t.join()
        print('Download done!')
        self._file.close()


# Example of Downloader
url = 'http://g.hiphotos.baidu.com/image/h%3D200/sign=57c485df7cec54e75eec1d1e893a9bfd/241f95cad1c8a786bfec42ef6009c93d71cf5008.jpg'
d = Downloader(url, 'avatar.jpg')
d.run()
