from selenium import webdriver
from datetime import date
import pandas as pd
import time
import datetime

options = webdriver.ChromeOptions()
# options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
driver = webdriver.Chrome(options=options)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}


content_list = []
review_title_list = []
review_content_list = []
product_list = []
productName_list = []
product_url = []

def getCategoryUrlList(main_url):
    driver.get(main_url)
    a_href = '//*[@id="__next"]/div[1]/div[1]/div[3]/div/div/main/div/div[4]/div/div/div[{}]/div/a'

    for i in range(1, 21):
        a_href_lists = driver.find_elements_by_xpath(a_href.format(i))
        for a_href_list in a_href_lists:
            product_list.append(a_href_list.get_attribute("href"))  # get_attribute href만 가져오기
    return product_list

# def productTitle(url):
#     driver.get(url)
#     product_name = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/h2')
#     return product_name.text

def reviewCrawling(url):
    title_lists = []
    content_list = []
    date_list = []
    starRating_list = []
    info_breed_list = []
    info_age_list = []

    url = url + "/reviews?page={}"  # ex) https://dogpre.com/product/84863/reviews
    print("지금 상품은 ", url[19:32], "입니다.")

    for pageNum in range(1):    # 일단 리뷰페이지에서 1,2페이지만 받기
        driver.get(url.format(pageNum))
        print("***************지금은 리뷰 ", pageNum, "페이지 입니다.***************")
        time.sleep(5)

        review_title_url = '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[2]/main/div[4]/div[{}]/div[2]/div[1]/div/h3'
        review_content_url = '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[2]/main/div[4]/div[{}]/div[2]/div[1]/div/div'
        review_date_url = '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[2]/main/div[4]/div[{}]/div[1]/div/div[1]'
        dog_info_breed_url = '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[2]/main/div[4]/div[{}]/div[1]/div/div[3]/span[1]'
        dog_info_age_url = '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[2]/main/div[4]/div[{}]/div[1]/div/div[3]/span[2]'
        star_rate_url = '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[2]/main/div[4]/div[{}]/div[1]/div/div[1]/span'

        for i in range(1, 31):
            review_titles = driver.find_elements_by_xpath(review_title_url.format(i))
            for review_title in review_titles:
                # print("***** 리뷰 제목 *****")
                # print(review_title.text)
                if "," not in review_title.text:
                    title_lists.extend(review_title.text.split(','))
                else:
                    title_lists.append(review_title.text.replace(",", ""))

            review_contents = driver.find_elements_by_xpath(review_content_url.format(i))
            for review_content in review_contents:
                # print("***** 리뷰 내용 *****")
                # print(review_content.text)
                content_list.append(review_content.text)

            review_dates = driver.find_elements_by_xpath(review_date_url.format(i))
            for review_date in review_dates:
                # print("***** 리뷰 날짜 *****")
                # print(review_date.text)
                date_list.extend(review_date.text.split(','))

            star_rates = driver.find_elements_by_xpath(star_rate_url.format(i))
            for star_rate in star_rates:
                # print("***** 별점 *****")
                # print(star_rate.get_attribute("aria-label"))
                starRating_list.append(star_rate.get_attribute("aria-label"))

            dog_info_breeds = driver.find_elements_by_xpath(dog_info_breed_url.format(i))
            for dog_info_breed in dog_info_breeds:
                # print("***** 강아지 정보 *****")
                # print(dog_info.text)
                info_breed_list.extend(dog_info_breed.text.split(','))

            dog_info_ages = driver.find_elements_by_xpath(dog_info_age_url.format(i))
            for dog_info_age in dog_info_ages:
                # print("***** 강아지 정보 *****")
                # print(dog_info.text)
                info_age_list.extend(dog_info_age.text.split(','))

        # for i in range(30):
        #     print("***** ", i, "번째 리뷰입니다.*****")
        #     print("***** 리뷰 제목 *****")
        #     print(title_list[i])
        #     print("*****", i, "번째 리뷰 내용 *****")
        #     print(sample_list[i])
        #     print("***** 리뷰 날짜 *****")
        #     print(date_list[i])
        #     print("***** 리뷰 별점 *****")
        #     print(starRating_list[i])
        #     print("***** 강아지 종 *****")
        #     print(info_breed_list[i])
        #     print("***** 강아지 나이 *****")
        #     print(info_age_list[i])

        # print(len(sample_lists))
        # for sample_list in sample_lists:
        #     bonmun_lists.append(sample_list)
        # sample_lists = []
        # content_list = []
        # for i in range(len(content_list)):
        sample_lists = []
        sample_lists = list(filter(None, content_list))
        # if content_list[i] == "3":
        #     content_list.remove("3")
        # elif content_list[i] == "2":
        #     content_list.remove("2")
        sample_list = []
        for sample_list in sample_lists:
            item_mod2 = sample_list.replace(",", "")
            review_content_list.append(item_mod2)

    return title_lists, review_content_list, date_list, starRating_list, info_breed_list, info_age_list


def getItemData(url):
    driver.get(url)
    product_name = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/h2')
    productName = product_name.text
    print(productName)
    title_lists, review_content_list, date_list, starRating_list, info_breed_list, info_age_list = reviewCrawling(url)
    return {'item_name': productName, 'review_title': title_lists, 'review_content': review_content_list, 'review_date': date_list, 'review_star': starRating_list, 'dog_breed': info_breed_list, 'dog_age': info_age_list}

def getAllItemData():
    product_urls = getCategoryUrlList("https://dogpre.com/category/036")
    # for product_url in product_urls:
    #     item_list = []
    #     item_data = reviewCrawling(product_url)
    #     item_list.append(item_data)
    # return item_list
    for i in range(2):
        item_list = []
        item_data = getItemData(product_urls[i])
        print(item_data)
        item_list.append(item_data)
    return item_list

def main():
    # today = date.today()
    # filename = f'dogPre{today.year}_{today.month}_{today.day}'
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y_%m_%d_%H-%M-%S")
    fileName = str(nowDate) + 'dogpre'

    item_data_list = getAllItemData()
    main_list = []
    for item_data in item_data_list:
        main_list.append([item_data['item_name'], item_data['review_title'], item_data['review_content'], item_data['review_date'], item_data['review_star'], item_data['dog_breed'],item_data['dog_age']])

    df = pd.DataFrame(main_list)   # pd.DataFrame 생성
    df.columns = ['item_name', 'review_title', 'review_content', 'review_date', 'review_star', 'dog_breed', 'dog_age']   # columns 설정
    df.to_csv(fileName+'.csv',encoding='utf-8-sig')   # DataFrame을 csv 파일로 저장
    print("Finish Crawling!")

main()

# now = datetime.datetime.now()
# nowDate = now.strftime("%Y_%m_%d_%H-%M-%S")
# fileName = str(nowDate) + 'dogpre'
# df.to_csv(fileName + '.csv', encoding='utf-8-sig')