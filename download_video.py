import requests
import shutil
from download_chunklist import get_chunklist
BASE_URL = input("가져온 URL에서 /media_**.ts 부분을 제외하고 입력해 주세요 : ")
OUTPUT_FILE_NAME = input("생성할 비디오 파일명을 입력해 주세요 (ex. yonsei.mp4) : ")
chunk_size = 256

chunk_list = get_chunklist(BASE_URL+"/chunklist.m3u8")
with open(OUTPUT_FILE_NAME,'wb') as f:
    for ts in chunk_list:
        cur_url = BASE_URL+"/"+ts
        r = requests.get(cur_url, stream=True)
        for chunk in r.iter_content(chunk_size= chunk_size):
            f.write(chunk)
        print(ts+"...ok")
