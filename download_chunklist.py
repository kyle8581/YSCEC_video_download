import requests

def get_chunklist(url):
    chunk_list = []
    r = requests.get(url)
    f = open("chunklist.txt", "wb")
    f.write(r.content)
    f.close()
    f = open("chunklist.txt", "r")
    for line in f:
        if ".ts" in line:
            chunk_list.append(line.strip())

    return chunk_list






if __name__ == '__main__':
    get_chunklist("https://cdn.yonsei.ac.kr/yonsei/_definst_/mp4:yscecictl_yscec/410493/1600164565/%ED%99%95%EB%A5%A0%ED%86%B5%EA%B3%84(3.4(2)).mp4/chunklist.m3u8")