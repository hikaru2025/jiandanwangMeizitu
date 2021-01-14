from  bs4 import  BeautifulSoup
import  re
import  requests
import  time



def getImageUrl(url):

    if  len(url):
        print('下载结束')
        return


    headers = {
        'authority': 'jandan.net',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_ga=GA1.2.1312662122.1610614238; _gid=GA1.2.612791173.1610614238; PHPSESSID=vnnfbrg8uve6scoo0r7ts1mg4u',
    }

    response = requests.get(url, headers=headers)
    sp=BeautifulSoup(response.text,"lxml")
    # 获取图片链接列表
    for im in sp.find_all(name='a',text='[查看原图]'):
        imageurl='http:'+im['href']
        print(imageurl )
        download(imageurl)

    time.sleep(2)


    # 获取下一页地址
    nextUrl= sp.find_all(name='a',attrs={"title":"Older Comments"})[0]['href']
    if len(nextUrl):
        nextUrl='http:'+nextUrl
        print(nextUrl)

    getImageUrl(nextUrl)

def download(imageUrl):
    image=requests.get(imageUrl)
    imageName=getFileName(imageUrl)
    with open('D:\\beauties\\'+imageName,'wb+') as f:
        f.write(image.content)
        f.close()

def getFileName(imageUrl):
    if len(imageUrl):
        return re.findall(r'[^\/]+(?!.*\/)',imageUrl)[0]

if __name__ == '__main__':
    getImageUrl('https://jandan.net/ooxx/MjAyMTAxMTQtMTEw')