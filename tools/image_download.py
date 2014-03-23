""""多线程下载电影图片
部分douban图片无法正常显示，可以利用此程序将图片下载到本地
"""


from hashlib import sha1
from queue import Queue
from threading import Thread
from urllib.request import urlopen
from urllib.error import HTTPError
from pymongo import MongoClient

db = MongoClient().bastogne
queue = Queue()
movies = db.movie.find()

for movie in movies:
    queue.put(movie['image'])


class DownloadThread(Thread):
    def run(self):
        while queue.empty() is False:
            url = queue.get()
            with open('e:/Temp/bastogne/image/' + sha1(url.encode()).hexdigest() + '.jpg', 'wb') as f:
                try:
                    res = urlopen(url)
                    f.write(res.read())
                except HTTPError as e:
                    print(url, e)
                    continue


if __name__ == '__main__':
    for i in range(10):
        download = DownloadThread()
        download.start()
    queue.join()

    print('下载完毕')

