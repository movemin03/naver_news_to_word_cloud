# Naver News Word Cloud

Naver News Word Cloud is a program that crawls Naver news articles and converts them into word clouds.

You can download the executable (exe) file through this link: [Download Naver News Word Cloud](https://github.com/movemin03/naver_news_word_cloud/blob/master/naver_news_word_cloud.exe)

---

## 1. Instructions for Executable File (exe) Users:

1. Download the exe file.
2. Before running the program, make sure to install JDK.
    - JDK can be downloaded from the following link: [Java SE Downloads](https://www.oracle.com/java/technologies/downloads/#jdk19-windows)
3. After installation, set the JAVA_HOME environment variable.
    - For example:
        - System Properties -> Advanced -> Environment Variables -> System variables Edit -> New:
            - Name: JAVA_HOME
            - Value: C:\Program Files\Java\jdk-19\bin
        - System Properties -> Advanced -> Environment Variables -> System variables Edit -> Path:
            - Add: C:\Program Files\Java\jdk-19\bin
4. Enjoy using the program!

## 2. Instructions for Python File (py) Users:

1. Install Python 3.10
    - jpype only works with Python versions up to 3.10. Therefore, use Python 3.10.
    - Python can be installed from the following link: [Python Downloads](https://www.python.org/downloads/)
2. Install JDK.
    - JDK can be downloaded from the following link: [Java SE Downloads](https://www.oracle.com/java/technologies/downloads/#jdk19-windows)
    - and set Jave Home environment
3. install requirements:
```cmd
pip install bs4, requests, pandas, lxml, konlpy, Cython, JPype1
```
**Note:**
To install konlpy and JPype1, you need to install JDK first.
and
Below are the libraries that need to be downloaded and installed separately.
**wordcloud: ** download it manually from [here](https://www.autoitscript.com/site/autoit/downloads/).
 and install it using:
[here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud) and install it using below command
```python
pip install folder_path\wordcloud-1.8.1-cp311-cp311-win_amd64.whl
```
4. To convert .py files to .exe using pyinstaller:
```cmd
pyinstaller --onefile --add-data="C:\\python311\\Lib\site-packages\\konlpy\\;.\konlpy" --add-data="C:\\python311\\Lib\site-packages\\konlpy\\java;.\\konlpy\\java" --add-data="C:\\python311\\Lib\site-packages\\konlpy\\tag\\*;.konlpy\\tag" --add-data="__init__.py;wordcloud" --add-data="__main__.py;wordcloud" --add-data="_version.py;wordcloud" --add-data="color_from_image.py;." --add-data="DroidSansMono.ttf;wordcloud" --add-data="query_integral_image.pyd;wordcloud" --add-data="stopwords;wordcloud" --add-data="tokenization.py;wordcloud" --add-data="wordcloud.py;wordcloud" --add-data="wordcloud_cli.py;wordcloud" naver_news_word_cloud.py
```

---
---

#네이버 뉴스를 크롤링한 후 이를 워드클라우드로 변환해주는 프로그램입니다
[여기](https://github.com/movemin03/naver_news_word_cloud/blob/master/naver_news_word_cloud.exe
) 링크를 통해 exe 파일을 다운받을 수 있습니다.

## 1. exe 파일 사용시
 가. exe 파일을 다운로드 해주세요.
 나. 실행하기 전에 JDK 를 설치해주세요.
 나-1. JDK 는 [다음](https://www.oracle.com/java/technologies/downloads/#jdk19-windows) 링크를 통해 설치할 수 있습니다.
 
 나-2. 설치 완료 후 환경변수 설정이 필요합니다
 예를 들어,
 시스템 속성 - 고급 - 환경변수 -> 시스템 변수 편집 -> 새로 만들기 ->이름: JAVA_HOME 변수 값: C:\Program Files\Java\jdk-19\bin
 시스템 속성 - 고급 - 환경변수 -> 시스템 변수 편집 -> Path -> C:\Program Files\Java\jdk-19\bin
 다. 즐기세요!
 
## 2. 코드 파일 (py) 사용시
  가. 파이썬 [여기서](https://www.python.org/downloads/) 설치:
jpype 가 파이썬 3.10 버전까지에서만 작동하기 때문에 3.10 버전 사용 필요
  가-1. 파이썬 설치법 =
    customize installation -> pip, tcl/tk and IDLE, for all users 3개 체크
    -> add python to environment variables 체크
    -> locaton 은 C:\python310\ 으로 하고 install
    시스템 속성 - 고급 - 환경변수 -> 시스템 변수 편집 -> Path -> C:\python311\ 와 C:\python311\Scripts 추가
  나. JDK [여기서](https://www.oracle.com/java/technologies/downloads/#jdk19-windows) 설치
  환경설정도 하세요
  시스템 속성 - 고급 - 환경변수 -> 시스템 변수 편집 -> 새로 만들기 ->이름: JAVA_HOME 변수 값: C:\Program Files\Java\jdk-19\bin
  시스템 속성 - 고급 - 환경변수 -> 시스템 변수 편집 -> Path -> C:\Program Files\Java\jdk-19\bin
  
  다. cmd 를 오른쪽 버튼을 눌러서 관리자 권한으로 실행 (execute cmd with administrative authority)
  ```cmd
  pip install bs4, requests, pandas
  ```
  pip install lxml 
  ==> 만약 에러가 생긴다면 [여기서](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) 다운받고 pip install 파일위치\lxml-4.9.0-cp311-cp311-win_amd64.whl
  
  pip install wordcloud
  ==> 만약 에러가 생긴다면 [여기서](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud) 다운받고 pip install 파일위치\wordcloud-1.8.1-cp311-cp311-win_amd64.whl
  
  pip install konlpy
  ==> JDK 가 깔려 있어야 오류가 나지 않습니다.
  
  3. py 파일을 pyinstaller 로 exe file 로 변경하려고 한다면
  가. konlpy 와 wordcloud 를 --add-data 해주어야 합니다. 그렇지 않으면 stopword 가 없다거나 konlpy 에서 tag 파일을 찾을 수 없다는 오류가 나올 것입니다.
  가-1. konlpy 와 wordcloud 는 보통 사용자의 파이썬 설치 위치의 lib 폴더 안에 있습니다.
  가-2. 저는 아래와 같이 입력했으니 참고해주세요.
  ```cmd
  pyinstaller --onefile --add-data="C:\\python311\\Lib\site-packages\\konlpy\\;.\konlpy" --add-data="C:\\python311\\Lib\site-packages\\konlpy\\java;.\\konlpy\\java" --add-data="C:\\python311\\Lib\site-packages\\konlpy\\tag\\*;.konlpy\\tag" --add-data="__init__.py;wordcloud" --add-data="__main__.py;wordcloud" --add-data="_version.py;wordcloud" --add-data="color_from_image.py;." --add-data="DroidSansMono.ttf;wordcloud" --add-data="query_integral_image.pyd;wordcloud" --add-data="stopwords;wordcloud" --add-data="tokenization.py;wordcloud" --add-data="wordcloud.py;wordcloud" --add-data="wordcloud_cli.py;wordcloud" naver_news_word_cloud.py
  ```
  나. 필수는 아니지만 오류가 계속된다면 JPype 와 Cython 설치를 고려하세요. JPype 는 자바 프로그램(konlpy)을 실행시켜주는 모듈, Cython 은 C 기반 프로그램을 실행시킬 수 있게 합니다.
  ```cmd
  pip install Cython, JPype1
  ```
