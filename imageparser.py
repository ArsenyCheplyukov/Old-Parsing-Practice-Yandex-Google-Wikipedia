from selenium import webdriver
import os
import urllib
from urllib import request
import time
from tqdm import tqdm  # Change this line

path = r'chromedriver.exe'

url_prefix = "https://www.google.com/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiE7InesOPxAhWF_SoKHXgvCikQ_AUoAXoECAIQAw&biw=929&bih=888"

save_folder = 'ParsedImages'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    download_images()
    
def download_images(topic=input("What do you want to search for? "), n_images=int(input('How many images do you want? '))):
    search_url = url_prefix+topic+url_postfix
    
    driver = webdriver.Chrome(path)
    driver.get(search_url)
    
    value = 0
    for i in tqdm(range(int(n_images/100))):
        for j in tqdm(range(int(n_images/20))):
            driver.execute_script("scrollBy(" + str(value) + ", " + str(value + 100) + ");")
            value += 100
            time.sleep(1)
        try:
            driver.find_element_by_css_selector('.mye4qd').click()
        except:
            break
    
    elem1 = driver.find_element_by_id('islmp')
    sub = elem1.find_elements_by_tag_name('img')
    
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
            except Exception as e:
                print(f'fail with error {e}')
    
    driver.close()
    
if __name__ == "__main__":
    main()
