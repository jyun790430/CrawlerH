# coding=utf-8

import time
import urllib3
import threading
import Queue as queue


mp4List = [
	"https://cm.phncdn.com/videos/201912/22/270448771/720P_1500K_270448771.mp4?QToo6WdwS-9DuhIkQ2aXzmji3Lmku-nKyBEqvWzdH1NNNyz5HD6ecAa8n4As5ld4SIgDheZD0P50_UKjOQR-7OGqCNq6oqQWQGVMjuW4zg54sbF2jbn_WD7vMJQNLaN-rkVwn-65zjs646Ol1gCUKaGwNUxEqNf1ZZlB5vd5D-zf88kOW8RwkV-mVMhhgBje39WK9UOo0nbm",
	"https://em.phncdn.com/videos/202001/01/272944681/720P_1500K_272944681.mp4?validfrom=1581355722&validto=1581362922&rate=500k&burst=1800k&hash=WuCdSZ4O6WBpPN3RYZD0YcJomxM%3D",
	"https://em.phncdn.com/videos/202002/03/281621871/720P_1500K_281621871.mp4?validfrom=1581355724&validto=1581362924&rate=500k&burst=1600k&hash=TapOUTe6rSDYV9DAOdkJezg5%2B34%3D",
	"https://cm.phncdn.com/videos/202001/23/278672421/720P_1500K_278672421.mp4?iUZ-l5FAjzlWgx3t87plwFxB6DmRsvXHepr2iBSUb_Dx1qGHtk_fyQMOyYn4nQzx5wxD0Uf7huNT3HHaBhIsts5LGj0nu4exz_q6Wh4SPHCCbH8uIjd3L9dTFBnIDLlMblzPOlYBXcEnG9Utf0Qcr75vev_XIbDR3R8Y_IHzFbWuauc-odZumi6jpT0jxal7Me9wBYCFxx0",
	"https://dv.phncdn.com/videos/202001/05/274091251/720P_1500K_274091251.mp4?ttl=1581362926&ri=2764800&rs=4000&hash=2ca8ed250305eaecb1b5f090354a5cc0",
	"https://cm.phncdn.com/videos/202001/28/280053621/720P_1500K_280053621.mp4?A3UjequeY_2iJpI5MTpWprz7WE1WS25id_sl2KdTbqbXZc1L8F0TnEJEJwuWmJDBGxexwt7Bl1PYbmpagQ5PtCDsBuDM8jd8NDvcEUJdJBq9zt0uCXIljRiWxY_irgHBzwYANsg-RYWWgfY1SR2tE8RmlecWwFEoMe75Usb-vlGmqTm8ajMYYlIm2E66FmsnDq8xmbixjKk",
	"https://em.phncdn.com/videos/202002/05/282205781/720P_1500K_282205781.mp4?validfrom=1581355729&validto=1581362929&rate=500k&burst=2200k&hash=FIKBhQD42hP%2FI5BI5UWlthH7EUM%3D",
	"https://dm.phncdn.com/videos/201912/20/270079851/720P_1500K_270079851.mp4?ttl=1581362930&ri=1228800&rs=4000&hash=48157f14fc253e6727acb48bbe6ec01e"
]

# for url in mp4List:
# 	http = urllib3.PoolManager()
# 	r = http.request('GET', url, preload_content=False)
# 	fileName = timestamp = int(time.time() * 1000.0)
# 	with open(str(fileName) + '.mp4', 'wb') as out:
# 		while True:
# 			data = r.read(1000)
# 			if not data:
# 				break
# 			out.write(data)
# 	print(url)
# 	r.release_conn()

class Download(threading.Thread):
	def __init__(self, queue, num):
		threading.Thread.__init__(self)
		self.queue = queue
		self.num = num

	def run(self):
		while self.queue.qsize() > 0:
			# 取得新的資料
			url = self.queue.get()

			# 處理資料
			print ("開始下載:" + str(self.num))
			self._getVideo(url)
			print("下載結束")

			time.sleep(1)

	def _getVideo(self, url):
		#urllib3.disable_warnings()

		http = urllib3.PoolManager()
		r = http.request('GET', url, preload_content=False)
		fileName = timestamp = int(time.time() * 1000.0)
		with open(str(fileName) + '.mp4', 'wb') as out:
			while True:

				data = r.read(1000)
				if not data:
					break
				out.write(data)
		print(url)
		print(fileName)
		r.release_conn()


my_queue = queue.Queue()

# 將資料放入佇列
for i in mp4List:
	my_queue.put(i)

# 建立兩個 Worker
my_worker1 = Download(my_queue, 1)
my_worker2 = Download(my_queue, 2)
my_worker3 = Download(my_queue, 3)

# 讓 Worker 開始處理資料
my_worker1.start()
my_worker2.start()
my_worker3.start()

# 等待所有 Worker 結束
my_worker1.join()
my_worker2.join()
my_worker3.join()



