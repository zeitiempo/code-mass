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
print(dmk_url)

# dmk_fll_url = r'http://www.jijidown.com'+dmk_url
# urllib.urlretrieve(dmk_fll_url, 'dev_dmk')
vd_fll_url = r'http://www.jijidown.com'+vd_url

'''
dl_rqst = Request(vd_fll_url, headers=headers)
dl_html = urlopen(dl_rqst).read()
dl_sp = bsoup(dl_html, 'html.parser')
dl_fll_url = dl_sp.find_all('a')
thdr_url = r''

for dl_url in dl_fll_url:
	precent_hrf = dl_url['href']
	if 'thunder:' in precent_hrf:
		thdr_url = precent_hrf

with open('thdr_url', 'wb') as f:
	f.write(thdr_url)

/html/body/div[2]/div[3]/div[6]/span[2]/a[3]

print(thdr_url)
'''
opts = webdriver.ChromeOptions()
opts.add_extension("fpdnjdlbdmifoocedhkighhlbchbiikl_3_2_1.crx")
brwsr = webdriver.Chrome(chrome_options=opts)
brwsr.get(vd_fll_url)
brwsr.refresh()
current_url = brwsr.current_url
print(current_url)
change_url = current_url.split(r'?')[0].replace(r'asp', 'php#')
print(change_url)
brwsr.get(change_url)
js_ = brwsr.find_elements_by_tag_name('script')

dv_dl_url_pttn = re.compile('http')

with codecs.open('js', 'w', 'utf-8') as f_js:
	for js in js_:
		js_ctxt = js.get_attribute('innerHTML')
		if "ctfile" in js_ctxt:
			f_js.write(js_ctxt+'\n')
			if re.match(dv_dl_url_pttn, js_ctxt):
				print(re.match(dv_dl_url_pttn, js_ctxt).group[0])

brwsr.quit()
