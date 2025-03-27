import requests
from bs4 import BeautifulSoup
import os
if os.path.isdir("images") != True:
	os.mkdir("images")
	os.chdir("images")
else:
	os.chdir("images")
query = ["carrioncrow", "commonblackbird", "commonchiffchaff", "commonraven", "commonwoodpigeon", "goose", "magpie", "robin", "seagull", "wren"]

for bird in query:

	images = []
	currentdir = os.getcwd()
	
	if os.path.isdir(currentdir+"/"+bird) != True:
		os.makedirs(bird)
	os.chdir(currentdir+"/"+bird)
	print(os.getcwd())
	
	def request(count, bird, images):
		url = "https://www.google.com/search?tbm=isch&q="+bird+"bird"+str(count)+"photo"
		print(url)
		r = requests.get(url)
		print(r.status_code)
		if r.status_code == 200:
			soup = BeautifulSoup(r.text, "html.parser")
			html = soup.prettify
			img = soup.find_all("img")
			print(img)
			count = 0
			for i in img:
				count += 1
			print(count)
			for i in range(1, count):
				cur = str(img[i])
				cur = cur.replace('<img alt=""','')
				cur = cur.replace('class="DS1iW" src="','')
				cur = cur.replace('"/>', '')
				print(cur)
				images.append(cur)
				if cur[1] == "<" or cur[1] == "'":
					images.pop()
			print(images)
		else:
			print(r.status_code)

	a = 0

	for i in range(0, 50):
		request(i, bird, images)
		
	for i in images:
		if os.path.isfile("image"+str(a)+".png") != True:
			f = open("image"+str(a)+".png", "xb")
		else:
			f = open("image"+str(a)+".png", "wb")
		try:
			print(os.getcwd())
			print(images[a])
			link=requests.get(images[a])
			f.write(link.content)
			a+=1
			print(a)
		except KeyboardInterrupt:
			print("ok")
			break
		except ConnectionError:
			for j in range(0, 10):
				print(os.getcwd())
				print(images[a])
				link=requests.get(images[a])
				f.write(link.content)
				print(a, "repeated")
		except requests.exceptions.InvalidSchema:
			print("skipped invalid link")
			pass
	os.chdir(currentdir)
