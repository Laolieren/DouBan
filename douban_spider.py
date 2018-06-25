import json
import requests

tv_types = [
    "american",
    "english",
    "korean_drama",
    "domestic",
    "hongkong",
    "japanese",
    "animation",
    "variety"
]
for i in range(8):
    headers = {
        "Referer": "https://m.douban.com/tv/" + tv_types[i],
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

    start = 0
    out = False
    while True:
        url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_" + tv_types[
            i] + "_hot/items?os=ios&for_mobile=1&start=%d&count=18&loc_id=108288" % (
            start)
        response = requests.get(url, headers=headers, timeout=10)
        ret = json.loads(response.content.decode())
        start += 18
        for b in range(18):
            try:
                tv_name = ret['subject_collection_items'][b]['title']
                tv_rate = ret['subject_collection_items'][b]['rating']['value']
                tv_year = ret['subject_collection_items'][b]['year']
                with open(tv_types[i] + ".txt", "a") as f:
                    f.write(tv_name + '     ' + str(tv_rate) + '     ' + tv_year + '\n')
            except Exception as r:
                out = True
                print("数据爬取完毕")
                break
        if out:
            break