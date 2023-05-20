from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Price, No_sold, rating, description, store, free_shipping, thumbnail, 
# product_link, quantity_available, quantity_sold, no_of_reviews, 
# estimated_delivery, discount, specification


PATH = '/home/menka/Documents/My-project/tech_with_tim/chromedriver'
driver = webdriver.Chrome(PATH)

URL = 'https://www.aliexpress.com/'

driver.get(URL)

print('==== Page Loading ====')
driver.implicitly_wait(10)

search = driver.find_element(By.ID, 'search-key')
search.send_keys("phone")
search.send_keys(Keys.ENTER)

try:
    print('==== Loading Phone Page ====')
    div_tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="list--gallery--34TropR"]')))
    print('==== Getting all Videos Tag ====')
    a_tags = div_tag.find_elements(By.XPATH, '//a[@class="manhattan--container--1lP57Ag cards--gallery--2o6yJVt"]')
    print('1')
    for a_tag in a_tags:
        print('3')
        a_tag.click()
        print('2')
        driver.switch_to.window(driver.window_handles[-1])
        try:
            tag = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="product-main-wrap"]')))
            print('Start extracting')
            print(tag)
            Thumbnail = tag.find_element(By.XPATH, '//div[@class="image-view-magnifier-wrap"]/img').get_attribute('src')
            print('thumbnail')
            Description = tag.find_element(By.XPATH, '//div[@class="product-title"]/h1')
            print('describe')
            No_of_reviews = tag.find_element(By.XPATH, '//div[@class="product-reviewer"]/div/span')
            print('review')
            Price = tag.find_element(By.CLASS_NAME, '//*[@id="root"]/div/div[2]/div/div[2]/div[5]/div/span')
            print('price')
            No_sold = tag.find_element(By.XPATH, '//span[@class="product-reviewer-sold"]')
            print('sold')
            Rating = tag.find_element(By.XPATH, '//span[@class="overview-rating-average"]')
            print('rating')
            Free_shipping = tag.find_element(By.XPATH, '//strong[@data-spm-anchor-id="a2g0o.detail.1000016.i7.69bf4a15LtWKHo"]')
            print('free shipping')
            Product_link = a_tag.get_attribute('href')
            print('product_link')
            Quantity_available = tag.find_element(By.XPATH, '//span[@class data-spm-anchor-id="a2g0o.detail.1000016.i8.69bf4a15LtWKHo"]')
            print('quality_available')
            Estimated_delivery = tag.find_element(By.XPATH, '//div[@class="dynamic-shipping-line dynamic-shipping-contentLayout"]/span/span')
            print('estimated delivery')
            Discount = tag.find_element(By.XPATH, '//div[@class="tip-box"]/span')
            print('discount')
            Phone_spec = tag.find_element(By.XPATH, '//div[@class="sku-title"]/span')
            print('phone spec')
            All_info = {'Price:', Price,
                        'No_sold:', No_sold,
                        'Rating:', Rating,
                        'Description:', Description,
                        'Free_shipping:', Free_shipping,
                        'Thumbnail:', Thumbnail,
                        'Product_link:', Product_link,
                        'Quantity_available:', Quantity_available,
                        'No_of_reviews:', No_of_reviews,
                        'Estimated_delivery:', Estimated_delivery,
                        'Discount:', Discount,
                        'Phone_spec:', Phone_spec}
            print(All_info)
            driver.quit()
        except:
            print('Not seen')
            driver.quit()
except:
    driver.quit()
    