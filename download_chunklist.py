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




