
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import base64
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn


host = "aHR0cHM6Ly93d3cuYnRidHQxMi5jb20="

save_dir = "/image"

def parser_cate():
    """ 从栏目获取详情页链接列表 """
    host_url = base64.b64decode("aHR0cHM6Ly93d3cuYnRidHQxMi5jb20=").decode("utf-8")
    url = host_url + "/forum-index-fid-957.htm"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    links_list = soup.find_all(name="a", attrs={"class": "subject_link thread-new"})
    links_list = [host_url + "/" + i.get("href") for i in links_list]
    return links_list


def parser_detail(url):
    """ 从详情页获取图片链接 """
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    p_list = soup.find_all(name="p")
    img_list = [p.find(name="img") for p in p_list]
    src_list = [i.get("src") for i in img_list if i]
    src_list = ["https://www.btbtt12.com" + i for i in src_list]
    return src_list
    
    
def download_img(img_list):
    """ 将图片链接列表中的图片下载到本地 """
    for i in img_list:
        # 使用 urlretrive 下载
        img_path = Path(save_dir) / Path(i).name
        try:
            with open(img_path, "wb") as f:
                req = requests.get(i)
                f.write(req.content)
            print("已下载 ->", img_path)
        except Exception as e:
            print("下载图片异常 ->", str(e))
            continue
    
    
def main_handle():
    """" 组合任务 """
    pages = parser_cate()
    for page in pages:
        src_list = parser_detail(page)
        download_img(src_list)
        

# 定时任务配置 #
scheduler = BackgroundScheduler()

scheduler.add_job(
    main_handle,
    "interval",
    hours = 1
)




app = FastAPI()

@app.on_event("startup")
def task_start():
    scheduler.start()
    job = scheduler.get_jobs()[0]
    print("job ->",job)


@app.on_event("shutdown")
def task_down():
    scheduler.shutdown()
    print("job down")


if __name__ == "__main__":
    
    uvicorn.run(app="btt_img:app", port=12345)
