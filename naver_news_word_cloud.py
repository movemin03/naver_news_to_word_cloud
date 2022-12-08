#크롤링시 필요한 라이브러리 불러오기
from bs4 import BeautifulSoup
import requests
import re
import datetime
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
import csv
import sys


# wordcloud 변경
def wordcloud():
    print("윈도우10/11 의 경우 해당 파일에 마우스 올리고 오른쪽 클릭 - 경로로 복사 기능 사용 가능")
    location = input("csv 파일 위치를 입력해주세요 .csv 까지 입력: ")
    try:
        location = location.replace('"', "")
    except:
        pass
    f = open(location, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    filter = []
    print("데이터 읽어오는 중...")
    for line in rdr:
        filter.append(line[3])

    okt = Okt()
    print("명사 추출 중...")
    nouns = okt.nouns(str(filter))  # 명사만 추출

    words = [n for n in nouns if len(n) > 1]  # 단어의 길이가 1개인 것은 제외

    data = Counter(words)  # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함

    yes_or_no = input("별도로 설정할 글꼴이 있으신가요? 기본은 맑은 고딕입니다. yes/no")


    if yes_or_no == "yes":
        print("윈도우10/11 의 경우 해당 파일에 마우스 올리고 오른쪽 클릭 - 경로로 복사 기능 사용 가능")
        font = input("가지고 있는 글꼴 파일 경로 입력(.ttf 까지): ")
        try:
            font = font.replace('"', "")
        except:
            pass

    else:
        font = 'malgun'

    yes_or_no = input("별도로 설정할 배경색이 있으신가요? 기본은 white 입니다 1. black 2. white 숫자만 입력")

    if yes_or_no == "1":
        background = 'black'
    else:
        background = 'white'

    yes_or_no = input("별도로 설정할 가로 세로값이 있나요? 기본은 가로*세로 1080px*1080px 입니다 yes/no")

    if yes_or_no == "yes":
        print("가로값: ")
        width = input(int())
        print("세로값: ")
        height = input(int())
    else:
        width = 1080
        height = 1080

    yes_or_no = input("별도로 설정할 최대 단어 수가 있나요? 기본은 100개 입니다 yes/no")

    if yes_or_no == "yes":
        print("뽑을 단어 수 지정: ")
        max_words = input(int())
    else:
        max_words = int(100)

    yes_or_no_2 = input("지정할 마스크가 있나요? yes/no")

    if yes_or_no_2 == "yes":
        print("윈도우10/11 의 경우 해당 파일에 마우스 올리고 오른쪽 클릭 - 경로로 복사 기능 사용 가능, .png까지 입력")
        icon_path = input("경로 입력: ")
        try:
            icon_path = icon_path.replace('"', '')
        except:
            pass
        try:
            icon = Image.open(icon_path)
            plt.imshow(icon)
            global mask
            mask = Image.new("RGB", icon.size, (255, 255, 255))
            mask.paste(icon, icon)
            mask = np.array(mask)
        except ValueError:
            print ("bad transparency mask 입니다. 마스크 적용이 실패했습니다. 기본형인 사각형으로 진행합니다")
            mask = None
    else:
        mask = None
        pass


    wc = WordCloud(font_path = font, width=width, height=height, scale=2.0, max_font_size=250, max_words = max_words, background_color=background, mask=mask)
    gen = wc.generate_from_frequencies(data)
    plt.figure()

    if yes_or_no_2 == "yes" and mask != None:
        yes_or_no = input("마스크가 지정되어 있습니다. 지정된 마스크의 색을 글씨에 입히시겠습니까? 기본값 no. yes/no 입력")
        if yes_or_no =="yes":
            image_colors = ImageColorGenerator(mask)
            plt.imshow(wc.recolor(color_func=image_colors))
        else:
            plt.imshow(gen)
    else:
        plt.imshow(gen)


    print("사진 파일 변환 중...")
    now_2 = datetime.datetime.now()
    now_2.strftime('%Y%m%d_%H시%M분%S초')
    now_3 = str(now_2).replace(":", "_")
    wc.to_file('워드클라우드' + str(now_3) + '.png')
    print("변환되었습니다\n")

    yes_or_no = input("어떤 단어가 얼마만큼 나왔는지도 확인하고 싶나요? yes/no")
    if yes_or_no == "yes":
        with open('단어빈도수'+ str(now_3) + '.csv', 'w') as f:
            w = csv.writer(f)
            w.writerow(data.keys())
            w.writerow(data.values())
        print("파일이 저장되었습니다")
    else:
        pass

    yes_or_no == ""
    yes_or_no_2 == ""



# 페이지 url 형식에 맞게 바꾸어 주는 함수 만들기
  #입력된 수를 1, 11, 21, 31 ...만들어 주는 함수
def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num+1
    else:
        return num+9*(num-1)

# 크롤링할 url 생성하는 함수 만들기(검색어, 크롤링 시작 페이지, 크롤링 종료 페이지)

def makeUrl(search, start_pg, end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        global url
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(start_page)
        return url
    else:
        urls = []
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        print("생성 url 가공중... 시간이 걸립니다")
        return urls

def makeUrl_2(search, start_pg, end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&sort=1&start=" + str(start_page)
        return url
    else:
        urls = []
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&sort=1&start=" + str(page)
            urls.append(url)
        print("생성 url 가공중... 시간이 걸립니다")
        return urls

# html에서 원하는 속성 추출하는 함수 만들기 (기사, 추출하려는 속성값)
def news_attrs_crawler(articles,attrs):
    attrs_content=[]
    for i in articles:
        attrs_content.append(i.attrs[attrs])
    return attrs_content

# ConnectionError방지
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

def crawling():
#####뉴스크롤링 시작#####


    # 검색어 입력
    global search
    search = input("검색할 키워드를 입력해주세요:")
    # 검색 시작할 페이지 입력
    global page
    print("1쪽 당 10개의 기사입니다. 200개의 기사가 필요하면 시작1-종료20")
    page = int(input("\n크롤링할 시작 페이지를 입력해주세요. ex)1(숫자만입력):")) # ex)1 =1페이지,2=2페이지...
    print("\n크롤링할 시작 페이지: ", page, "페이지")
    # 검색 종료할 페이지 입력
    global page2
    page2 = int(input("\n크롤링할 종료 페이지를 입력해주세요. ex)1(숫자만입력):"))  # ex)1 =1페이지,2=2페이지...

    # naver url 생성

    search_option = input("어떤 순으로 검색하실건가요? 기본값은 최신순입니다. 1. 인기순 2. 최신순  숫자만 입력: ")

    global url
    if search_option == "1":
        url = makeUrl(search, page, page2)
    else:
        url = makeUrl_2(search, page, page2)


    # 뉴스 크롤러 실행
    global news_titles
    news_titles = []
    global news_url
    news_url = []
    global news_contents
    news_contents = []
    global news_dates
    news_dates = []

    for i in url:
        original_html = requests.get(i, headers=headers)
        html = BeautifulSoup(original_html.text, "html.parser")

        url_naver = html.select(
            "div.group_news > ul.list_news > li div.news_area > div.news_info > div.info_group > a.info")
        url = news_attrs_crawler(url_naver, 'href')
        news_url.append(url)

    # 제목, 링크, 내용 담을 리스트 생성
    global news_url_1
    news_url_1 = []

    # 1차원 리스트로 만들기(내용 제외)
    for i in news_url:
        for j in i:
            news_url_1.append(j)

    # NAVER 뉴스만 남기기
    global final_urls
    final_urls = []
    for i in range(len(news_url_1)):
        if "news.naver.com" in news_url_1[i]:
            final_urls.append(news_url_1[i])
        else:
            pass
    print("네이버 뉴스만 솎아내는 중...")

    # 뉴스 내용 크롤링

    for i in final_urls:
        global progress
        progress = progress + 1
        print(str(progress) + "/ 최대" + str((page2 + 1 - page) * 10) + " 항목 처리중")

    # 각 기사 html get하기
        news = requests.get(i, headers=headers)
        news_html = BeautifulSoup(news.text, "html.parser")
        # 뉴스 제목 가져오기
        title = news_html.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
        if title == None:
            title = news_html.select_one("#content > div.end_ct > div > h2")

        # 뉴스 본문 가져오기
        content = news_html.select("div#dic_area")
        if content == []:
            content = news_html.select("#articeBody")

        # 기사 텍스트만 가져오기
        # list합치기
        content = ''.join(str(content))

        # html태그제거 및 텍스트 다듬기
        pattern1 = '<[^>]*>'
        title = re.sub(pattern=pattern1, repl='', string=str(title))
        content = re.sub(pattern=pattern1, repl='', string=content)
        pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
        content = content.replace(pattern2, '')

        news_titles.append(title)
        news_contents.append(content)


        global news_date
        try:
            html_date = news_html.select_one("div#ct> div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span")

            news_date = html_date.attrs['data-date-time']
        except AttributeError:
            news_date = news_html.select_one("#content > div.end_ct > div > div.article_info > span > em")
            news_date = re.sub(pattern=pattern1, repl='', string=str(news_date))
        # 날짜 가져오기
        news_dates.append(news_date)


    print("\n검색된 시도 갯수: 총 ", (page2 + 1 - page), '페이지')
    print("성공한 갯수:" + str(progress))
    print("검색 성공 갯수가 시도 갯수보다 적은 경우 검색 페이지 수를 늘려서 시도해보세요\n")

    print('news_title: ', len(news_titles))
    print('news_url: ', len(final_urls))
    print('news_contents: ', len(news_contents))
    print('news_dates: ', len(news_dates))

    ###데이터 프레임으로 만들기###

    #데이터 프레임 만들기
    global news_df
    news_df = pd.DataFrame({'date':news_dates,'title':news_titles,'link':final_urls,'content':news_contents})
    news_df

    #중복 행 지우기
    news_df = news_df.drop_duplicates(keep='first',ignore_index=True)
    print("중복 제거 후 행 개수: ",len(news_df))

    #데이터 프레임 저장
    now = datetime.datetime.now()
    news_df.to_csv('{}_{}.csv'.format(search,now.strftime('%Y%m%d_%H시%M분%S초')),encoding='utf-8-sig',index=False)


# ==============================================================================

print("네이버 뉴스 컨텐츠 크롤링 프로그램입니다.")
print("버전 정보: 2022-12-07 ver\n")

exit_or_not = "yes"
while exit_or_not == "yes" or exit_or_not == "y":
    what = input("\n어떤 것을 하시겠습니까? 1. 워드클라우드 변경 2. 뉴스 크롤링 *번호만 입력해주세요*: ")
    if what == "1":
        wordcloud()
    elif what == "2":
        progress = 0
        crawling()
    else:
        print("잘못 입력하셨습니다. 처음으로 돌아갑니다\n")
        pass
print("완료되었습니다. 처음으로 돌아가려면 yes 나 y 를, 종료하려면 아무키나 눌러주세요")
what = input()

sys.exit()
