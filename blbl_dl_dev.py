# coding:utf-8 #

import urllib
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup as bsoup
import re
import os
from selenium import webdriver
import codecs

dev_url = r'http://www.bilibilijj.com/video/av16189812/'

rqst = Request(dev_url)
user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
headers = { 'User-Agent' : user_agent }
html = urlopen(rqst).read()
sp = bsoup(html, 'html.parser')
vd_url = sp.find('span', class_='Data_Main').\
		 find('span', class_='Data_Data').\
		 find('a')['href']
dmk_url = sp.find('span', class_='Data_Ass').\
		  find('span', class_='Data_Data').\
		  find_all('a')[1]['href']

print(vd_url)
print(dmk_url) #直接下载

vd_code = vd_url.split('/')[-1]+'.php'

vd_fll_url = r'http://www.jijidown.com/FreeDown/'+vd_code

for i in range(2):
	opts = webdriver.ChromeOptions()
	opts.add_extension("fpdnjdlbdmifoocedhkighhlbchbiikl_3_2_1.crx")
	brwsr = webdriver.Chrome(chrome_options=opts)
	brwsr.get(vd_fll_url)
	js_ = brwsr.find_elements_by_tag_name('script')

for js in js_:
	js_ctxt = js.get_attribute('innerHTML')
	if "ctfile" in js_ctxt:
		dl_url = js_ctxt.split('\n')[3].split('\"')[1]
		print(dl_url)

brwsr.get(dl_url)
brwsr.find_element_by_id('free_down_link').click()
# brwsr.quit()
