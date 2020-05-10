
import requests

for i in range(2):
    for n in range(7):
        for m in range(6):
            for j in range(10):
                id=str(i)+str(n)+str(m)+str(j)
                url='https://bili.meijuzuida.com/20190829/21330_470bd6e7/1000k/hls/167902672fa00{}.ts'.format(id)
                headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
                response=requests.get(url,headers=headers)
                data=response.content
                with open('告别高中的夏天.mp4','ab') as f:
                    f.write(data)
                    print(id)
















