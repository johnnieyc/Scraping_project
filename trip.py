from selenium import webdriver
import time
import re
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
import csv

driver = webdriver.Chrome()

# Go to the page that we want to scrape
driver.get("https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html")  


csv_file = open('newtripadvisor.csv','w')
writer = csv.writer(csv_file)
writer.writerow(['hotel','rank','price','hotel_star','address','extended_address','number_of_review','overall_star_of_review','keywords'])


index=1 
url_list = []
for i in range(0, 690, 30):
    url_list.append('https://www.tripadvisor.com/Hotels-g60763-oa'+str(i)+'-New_York_City_New_York-Hotels.html#BODYCON')

for each_url in url_list:
    try:
        driver.get(each_url)
        #print("Scraping Page number " + str(index))
        index=index+1

        #headline = driver.find_elements_by_xpath('//*[@id="rn602426205"]/span')
        #price = driver.find_elements_by_xpath('//*[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div[2]')
        #review_count = driver.find_elements_by_xpath('//*[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/a')
        
        properties = driver.find_elements_by_xpath('//*[@class="property_title prominent"]')
        hotel_name = [x.text for x in properties]
        print(hotel_name)
        
        hotels_hrefs = [x.get_attribute('href') for x in properties]
        print(hotels_hrefs)
        # price = driver.find_elements_by_xpath('//div[@class="priceBlock ui_column is-12-tablet"]')
         
        # price_ = [x.text for x in price]
        # print(price_)

        



        # def price__:
        #     price__ = lambda x: x[0][:5] for x in x
        


        trip_dict = {}
      
        for each,hotel in zip(hotels_hrefs,hotel_name):
            driver.get(each) 
            location = driver.find_element_by_xpath('//span[@class="street-address"]')
            location_name = location.text
            
           
            extended_location = driver.find_element_by_xpath('//span[@class="detail"]/span[2]').text
            
            #locality = driver.find_element_by_xpath('//div[@class="is-hidden-mobile blEntry address ui_link"]/span[2]').text
            





            #price = driver.find_element_by_xpath('//div[@class="premium_offers_area offers"]/div[1]')
            try:
                price = driver.find_element_by_xpath('//div[@class="no_cpu offer premium chevron hacComplete  avail "]')
            except:
                try:
                    price = driver.find_element_by_xpath('//div[@class="premium_offers_area offers"]/a')
                    #price = driver.find_element_by_xpath('//div[@data-pernight]
                except:
                    price = driver.find_element_by_xpath('//div[@class="premium_offers_area offers"]/div[1]')
            
            price_ = price.get_attribute('data-pernight')
            
            

            review_number = driver.find_element_by_xpath('//span[@class="reviewCount"]')
            review_count = review_number.text

            hotel_title = driver.find_element_by_xpath('//h1[@id="HEADING"]')
            hotel_ = hotel_title.text
            

            rank = driver.find_element_by_xpath('//span[@class="header_popularity popIndexValidation"]').text
            



            overall_star = driver.find_element_by_xpath('//div[@class="prw_rup prw_common_bubble_rating rating"]/span[1]')
            hotel_review_star = overall_star.get_attribute('class')[-2:]
            

            hotel_star = driver.find_element_by_xpath('//div[@class="starRating detailListItem"]')
            hotel_stars = hotel_star.text

            keywords = driver.find_elements_by_xpath('//div[@class="prw_rup prw_filters_tag_cloud"]/div/span')
            keywords_list = [keyword.text for keyword in keywords]
            
            
            
            
            trip_dict['hotel'] = hotel_
            trip_dict['rank'] = rank
            trip_dict['price'] = price_
            trip_dict['hotel_star'] = hotel_stars
            trip_dict['address'] = location_name
            trip_dict['extended_address'] = extended_location
            trip_dict['number_of_review'] = review_count
            trip_dict['overall_star_of_review'] = hotel_review_star
            trip_dict['keywords'] = keywords_list

            
            writer.writerow(trip_dict.values())
            

            

            # try:
            #     showmore = driver.find_element_by_xpath('//a[@class="seeHotelDetails detailListItem"]')
            #     showmore.click()
            #     print('clicked')
            #     time.sleep(5)
            #     about = driver.find_elements_by_xpath('//div[@class="is-hidden-desktop tabextra"]//div[@class="ui_column is-12-mobile is-6-tablet"]')[1]
            #     number_of_room = about.find_element_by_xpath('.//div[@class="textitem"]').text
            #     print('======')
            #     print(number_of_room)


            
            # try:
            #     showmore = driver.find_element_by_xpath('//a[@class="seeHotelDetails detailListItem"]')
            #     showmore.click()
            #     print('clicked')
            #     time.sleep(5)
            #     #about = driver.find_elements_by_xpath('//div[@class="is-hidden-desktop tabextra"]//div[@class="ui_column is-12-mobile is-6-tablet"]')[1]
            #     number_of_room = driver.find_element_by_xpath('//*[@id="ABOUT_TAB"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[6]/div[1])')
            #     #number_of_room = driver.find_element_by_xpath('.//div[@class="is-hidden-desktop tabextra"]').text
            #     print('======')
            #     print(number_of_room)

            # except:
            #     print('not clicked')
            #     pass

            


       
            
            
                


                
                
       
            
                                                

    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break




