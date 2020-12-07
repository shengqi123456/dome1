# =============================================================================
# 好看视频_v0.1
# =============================================================================
import re
import os
import time
import queue
import requests
import threading
import pandas as pd


class Haokan:
    def __init__(self):
        self.url = 'https://haokan.baidu.com/videoui/page/search?pn=%d&rn=20&_format=json&tab=video&query=%s'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
        }
        self.savaPath = './videos'  # 视频存储路径

    def get_info(self, keywords, page):
        '''
        搜索关键字，获取相关视频信息
        '''
        self.result = []  # 相关视频信息
        for p in range(1, page + 1):
            res = requests.get(self.url % (p, keywords), headers=self.headers)
            data = res.json()['data']['response']
            videos = data['list']
            self.result.extend(videos)
            print('"第%d页"爬取完成!' % (p + 1))
        self.result = pd.DataFrame(self.result)
        self.result.to_excel('%s.xlsx' % keywords, index=False)
        # 定义队列，用于多线程下载视频
        self.url_queue = queue.Queue()
        for vid, url in zip(self.result['vid'], self.result['url']):
            self.url_queue.put((vid, url))

    def get_videoUrl(self, url):
        '''
        提取视频信息中的视频源地址
        '''
        res = requests.get(url, headers=self.headers)
        html = res.text
        videoUrl = re.findall('<video class="video" src=(.*?)>', html)[0]
        return videoUrl

    def download_video(self, videoId, videoUrl):
        '''
        下载视频文件
        '''
        # 如果视频存储目录不存在则创建
        if not os.path.exists(self.savaPath):
            os.mkdir(self.savaPath)
        res = requests.get(videoUrl, headers=self.headers)
        with open('%s/%s.mp4' % (self.savaPath, videoId), 'wb') as f:
            f.write(res.content)

    def run(self):
        while not self.url_queue.empty():
            t_s = time.time()
            vid, url = self.url_queue.get()
            try:
                video_url = self.get_videoUrl(url)
                self.download_video(vid, video_url)
            except:
                print('"%s.mp4"下载失败!' % vid)
                continue
            t_e = time.time()
            print('"%s.mp4"下载完成!(用时%.2fs)' % (vid, t_e - t_s))


if __name__ == "__main__":
    keywords = '多啦A梦'
    page = 1  # 爬取页数，每页20条信息
    t_s = time.time()
    haokan = Haokan()
    haokan.get_info(keywords, page)
    N_thread = 3  # 线程数
    thread_list = []
    for i in range(N_thread):
        thread_list.append(threading.Thread(target=haokan.run))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    t_e = time.time()
    print('任务完成!(用时%.2fs)' % (t_e - t_s))