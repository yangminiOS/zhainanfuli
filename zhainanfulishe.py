#-*-coning:utf-8 -*-

import requests
import re
import os

def get_total_html(total_url):
    response = requests.get(total_url)
    if response.status_code ==200:
        try:
            response.encoding = response.apparent_encoding
            return response.text
        except:
            return None
            print 'return total_html error'

    else:
        print 'total_html code error'


def get_total_urls(total_html,url_lists):
    pattern = re.compile('<article class="home.*?<a href="(.*?)".*?title="(.*?)".*?</a>.*?</article>',re.S)
    items = re.findall(pattern,total_html)
    for item in items:

        url_lists.append([item[0],item[1]])

def get_one_html(one_url):
    response = requests.get(one_url)
    if response.status_code ==200:
        try:
            response.encoding = response.status_code
            return response.text
        except:
            print 'return one html error'
            return None
    else:
        print 'open one html error'

def get_one_images_url(one_html):
    pattern = re.compile('<p>.*?<img class=.*?src="(.*?)".*?</p>,*?')
    items = re.findall(pattern,one_html)
    return items


def save_image(image_url,file_name):
    response = requests.get(image_url)
    if response.status_code ==200:
        try:
            data = response.content
            f = open(file_name,'wb')
            f.write(data)
            print 'save sucess'
            f.close()
        except:
            print " save image error"

def save_images(images_url,name):
    for url in  images_url:
        url_name = url
        image_name = url_name[40:]
        path = name+'/'+image_name
        print path
        save_image(url_name,path)

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print 'mkdir sussess'
        return True
    else:
        print 'dif is have'
        return False


def main():
    total_lists = []
    total_url ='http://www.zhainanfulishe.net/nvshen/page/'
    for i in range(1,32):
        url = total_url+str(i)
        html = get_total_html(url)
        get_total_urls(html,total_lists)
        for item in total_lists:
            images_url = item[0]
            mkdir(item[1])
            one_html =get_one_html(images_url)
            save_images(get_one_images_url(one_html),item[1])


if __name__ == '__main__':
    main()