# coding:utf-8
from selenium.webdriver.common.action_chains import *
from bs4 import BeautifulSoup
import chardet
from selenium import webdriver
import time,re,codecs
from selenium.webdriver.support import expected_conditions as EC

class QunaSpider(object):

	def crawl(self,root_url):
		f = codecs.open(u'信息.txt', 'a', 'utf-8')
		driver = webdriver.Firefox()
		driver.set_page_load_timeout(50)
		driver.get(root_url)

		driver.implicitly_wait(10) # 控制间隔时间，等待浏览器反映
		driver.switch_to_frame('login_frame')
		ele_enter = driver.find_element_by_id("img_out_389058106")
		ele_enter.click()
		driver.switch_to_default_content()
		driver.implicitly_wait(10)
		try:
			ele_close = driver.find_element_by_id("dialog_button_1")
			ele_close.click()
		except:
			pass
		driver.implicitly_wait(5)
		ele_friend = driver.find_element_by_id("aMyFriends")
		ele_friend.click()
		time.sleep(3)
		js = "window.scrollTo(0, 570);"
		driver.execute_script(js)
		driver.switch_to_frame(driver.find_element_by_class_name('app_canvas_frame'))	
		while True:
			ele_imgs = driver.find_elements_by_class_name("avatar")
			time.sleep(3)		
			for ele_img in ele_imgs:				
				ActionChains(driver).move_to_element(ele_img).perform()
				time.sleep(2)
				driver.switch_to_default_content()
				htm_const=driver.page_source
				soup=BeautifulSoup(htm_const,'html.parser')
				name=list(soup.find(class_='nickname ui-mr5 textoverflow').span.strings)[0]
				info=list(soup.find(class_='card-user-basicinfo').p.strings)[0]
				print(name)
				print(info)
				f.write(name+' '+info)
				f.write('\r\n')
				driver.switch_to_frame(driver.find_element_by_class_name('app_canvas_frame'))
			try:
				driver.find_element_by_css_selector(".qz-button-disabled.qz-button.btn-pager-next")
				f.close()
				break
			except:
				pass
			next_page=driver.find_element_by_css_selector(".qz-button.btn-pager-next")
			next_page.click()
			time.sleep(3)				

		
		

				
					



if __name__=='__main__':
	spider = QunaSpider()
	spider.crawl('https://i.qq.com/?s_url=http%3A%2F%2Fuser.qzone.qq.com%2F389058106%2Finfocenter')
