import os

import img2pdf

dirname =  "i:\\Program files\\comic\\gufengmh\\zuiqiangfantaoluxitong 最强反套路系统\\40\\0000000000000000000"
with open("name.pdf","wb") as f:
	imgs = []
	for fp, dir, fn in os.walk(dirname):
		for fname in fn:
			if not fname.endswith(".jpg"):
				continue
			path = os.path.join(fp,fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
			print(path)
	f.write(img2pdf.convert(imgs))

