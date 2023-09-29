from selenium import webdriver
import os
import urllib
from urllib import request
import time
from tqdm.notebook import tqdm

path = r'C:\Program Files (x86)\chromedriver.exe'

url_prefix = "https://yandex.by/images/search?text="

save_folder = 'ParsedImages'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    download_images()

def download_images(topic=input("What do you want to search for? "), n_images=int(input('How many images do you want? '))):
    search_url = url_prefix+topic

    path = r'C:\Program Files (x86)\chromedriver.exe'
    
    driver = webdriver.Chrome(path)
    driver.get(search_url)
    
    value = 0
    for i in tqdm(range(n_images//250 + 1)):
        for j in tqdm(range(25)):
            driver.execute_script("scrollBy(" + str(value) + ", " + str(value + 100) + ");")
            value += 100
            time.sleep(1)
        try:
            driver.find_element_by_css_selector(".more_last_yes").find_element_by_tag_name('a').click()
            time.sleep(1)
        except:
            break
    
    sub = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "serp-list_js_inited", " " ))]').find_elements_by_tag_name('img')
    
    count=0
    for j,i in tqdm(enumerate(sub)):
        if j < n_images:
            src = i.get_attribute('src')                         
            try:
                if src != None:
                    src  = str(src)
                    print(src)
                    count += 1
                    urllib.request.urlretrieve(src, os.path.join(save_folder, topic+str(count)+'.jpg'))
                    time.sleep(1)
                else:
                    raise TypeError
            except Exception as e:              #catches type error along with other errors
                print(f'fail with error {e}')
    
    driver.close()

if __name__ == "__main__":
    main()