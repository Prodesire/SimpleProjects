# coding:utf-8
import sys
import time
import io
from functools import partial


class Tail:
    def __init__(self, filename, output_func=sys.stdout.write):
        self.filename = filename
        self.output_func = output_func

    def tail(self, n=5):
        try:
            with open(self.filename) as f:
                self._file = f
                self._file_length = f.tell()
                f.seek(0, io.SEEK_END)
                self._show_last_lines(n)
                while True:
                    line = f.readline()
                    if line:
                        self.output_func(line)
                    else:
                        time.sleep(1)
        except Exception as e:
            print('Open file error!')
            print(e)

    def _show_last_lines(self, n):
        line_len = 1000
        read_len = line_len * n
        while True:
            if read_len > self._file_length:
                self._file.seek(0)
                last_content = self._file.read()
                break
            last_content = self._file.read()
            lines_num = last_content.count('\n')
            if lines_num >= n:
                break
            line_len += 500

        for line in last_content.split('\n')[-n:]:
            self.output_func(line + '\n')


# Example of Tail
t = Tail('test.txt', output_func=partial(print, end='', flush=True))
t.tail()
