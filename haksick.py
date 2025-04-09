import requests
from bs4 import BeautifulSoup

url = "https://www.hs.ac.kr/kor/8398/subview.do"  # 한신대 식단표 게시판 고정 주소
res = requests.get(url, verify=False)  # 주소 들어가서 정보 읽기
res.raise_for_status()  # 문제가 있으면 프로그램 종료
soup = BeautifulSoup(res.text, "html.parser")  # HTML 문서 파싱
link = soup.find(attrs={"class": "artclLinkView"})  # class가 artclLinkView인 태그를 찾음
url2 = 'https://www.hs.ac.kr%s' % link["href"]  # 최신 게시글 링크 가져오기

# 이미지 크롤링
html = requests.get(url2, verify=False).text  # 최신 게시글 들어가서 정보 읽기
soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.select('img')  # img 태그 모두 가져오기

# 첫 번째 이미지 출력
if img_tags:  # img 태그가 존재하는지 확인
    first_img_url = img_tags[0]['src']  # 첫 번째 img 태그의 src 속성값 가져오기
    print(f"First image URL: {first_img_url}")  # 첫 번째 이미지 URL 출력
else:
    print("No images found.")  # 이미지가 없을 경우 메시지 출력

# # 이미지 저장
# for idx, img_tag in enumerate(img_tags):  # img 태그 모두 반복
#     img_url = img_tag['src']  # img 태그의 src 속성값 가져오기
#     img_name = f'raw_{idx + 1}.jpeg'  # 이미지 이름 지정 (raw_1.jpeg, raw_2.jpeg, ...)
#     img_data = requests.get(img_url, verify=False).content  # 이미지 데이터 가져오기
#     with open(img_name, 'wb') as f:  # 이미지 저장
#         f.write(img_data)
#     print(f"Saved: {img_name}")  # 저장된 이미지 이름 출력