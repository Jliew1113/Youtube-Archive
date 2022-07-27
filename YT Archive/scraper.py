from bs4 import BeautifulSoup as bs
from selenium import webdriver 
import pandas as pd 
import urllib.request as rq
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC 
    
driver = webdriver.Chrome(executable_path=r'C:\Users\liews\Downloads\chromedriver.exe') 
driver.get("https://www.youtube.com/results?search_query=photography&sp=EgIQAQ%253D%253D")

#scroll down to the bottom before starting the next step
user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
            links.append(i.get_attribute('href'))

print(len(links))

df = pd.DataFrame(columns = ['channel_title', 'channel_thumbnail', 'channel_url', 'channel_description', 'channel_subscribers', 'video_url', 'video_title', 'video_thumbnail', 'video_description', 'video_views', 'video_date', 'video_likes', 'video_dislikes', 'video_comments'])

wait = WebDriverWait(driver, 10)

for x in links:
    try:
        if x == None:continue

        driver.get(x)
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip()
        soup = bs(content,"html.parser")

        result = {}

        result['title'] = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text

        result['thumbnail'] = soup.find('link', itemprop = 'thumbnailUrl')['href']

        des_div = soup.find("div", {'id':'description', 'slot':'content', 'class': 'style-scope ytd-video-secondary-info-renderer'})
        des_formatted = des_div.find('yt-formatted-string')
        result['description'] = des_formatted.get_text()

        channel_title = soup.find('link', itemprop = 'name')['content']

        channel_sub = soup.find('yt-formatted-string', {'id':'owner-sub-count', 'class': 'style-scope ytd-video-owner-renderer'}).get_text().strip('subscribers')

        channelid = soup.find('meta', itemprop = 'channelId')['content']
        channel_url = "https://www.youtube.com/channel/" + channelid

        pagetmp = rq.urlopen(channel_url)
        souptmp = bs(pagetmp, 'html.parser')
        channel_des = souptmp.find("meta", itemprop="description")['content']
        channel_thumbnail = souptmp.find('link', rel = 'image_src')['href']

        result["views"] = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#count span"))).text.strip(' views')

        result['date_published'] = soup.find('meta', itemprop='datePublished')['content']

        try:
            text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "style-scope ytd-toggle-button-renderer style-text"})
            result["likes"] = ''.join([ c for c in text_yt_formatted_strings[0].attrs.get("aria-label") if c.isdigit() ])
            result["likes"] = 0 if result['likes'] == '' else int(result['likes'])
            result["dislikes"] = ''.join([ c for c in text_yt_formatted_strings[1].attrs.get("aria-label") if c.isdigit() ])
            result['dislikes'] = 0 if result['dislikes'] == '' else int(result['dislikes'])
        except TypeError:
            result["likes"] = 0
            result["dislikes"] = 0
 
        v_comments = ''
        count = 0
        for item in range(1): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
    
        try:
            tmp = driver.find_element_by_id("content-text")
            for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
                if (count == 5): break
                v_comments += (str(count) + ') ' + comment.text + '\n')
                count += 1
        except NoSuchElementException:
            v_comments += 'No comment'

        df.loc[1] = [channel_title, channel_thumbnail, channel_url, channel_des, channel_sub, x, result['title'], result['thumbnail'], result["description"], result["views"], result["date_published"],  result["likes"],  result["dislikes"], v_comments]
        df.to_csv('txt1.csv', mode = 'a', header=False)
    
    except:
        continue
    


