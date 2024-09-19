import requests
import json
# '''
#     http://www.aladin.co.kr/ttb/api/ItemList.aspx
#     ?ttbkey=[TTBKey]&QueryType=ItemNewAll&MaxResults=10&start=1&SearchTarget=Book&output=xml&Version=20131101
# '''
API_URL = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx"
API_KEY = "ttbrmsgnl111237001"
# API_URL = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=ItemNewSpecial&MaxResults=50&start=1&SearchTarget=Book&output=xml&Version=20131101"
params = {
    'ttbkey': API_KEY,
    'QueryType' : 'Bestseller',
    'MaxResults' : '50',
    'SearchTarget' : "Book",
    'Version' : '20131101',
    'output' : 'JS'
}

data = requests.get(API_URL,params=params).json()
items = data.get('item',[])
my_dict=[]
for item in items:
    num = item.get('isbn13')
    title = item.get('title')
    author = item.get('author')
    date = item.get('pubDate')
    description = item.get('bestDuration')
    salespoint = item.get('salesPoint')
    
    new_dict = {
        '국제 표준 도서 번호' : num,
        '저자' : author,
        '제목' : title,
        '출간일' : date,
        '기간' : description,
        '판매지' : salespoint
        
    }
    my_dict.append(new_dict)
print(json.dumps(my_dict,indent=1,ensure_ascii=False))
