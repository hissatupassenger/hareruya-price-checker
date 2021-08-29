import re
from collections import Counter

data = open("crawl_result.dat").readlines()
exp_pattern = '(?<=\[).*(?=\])'
exps = [re.search(exp_pattern, text).group() for text in data if re.search(exp_pattern, text)]
#print(Counter(exps))

name_pattern = '(?<=\《).*(?=\》)'

names = [re.search(name_pattern, text).group() for text in data if re.search(name_pattern, text)]
#print(Counter(names))


lang_pattern = '(?<=\【).*(?=\】)'

langs = [re.search(lang_pattern, text).group() for text in data if re.search(name_pattern, text)]
#print(Counter(langs))

card = { l.split("\t")[1]:l.split("\t")[0] for l in open("card.csv").readlines()}
brand = { l.split("\t")[13]:[l.split("\t")[0],l.split("\t")[1],l.split("\t")[4],l.split("\t")[14].rstrip()] for l in open("brand.csv").readlines()} 

for line in data:
    if re.search(name_pattern, line):
        #英語名しかなければ文字列そのままで、日本語名があったら"/"以下をとるようにして英語名を取得した。
        name_en =  re.search(name_pattern, line).group() if len(re.search(name_pattern, line).group().split("/"))==1 else re.search(name_pattern, line).group().split("/")[1]
        #print(name_en)
        if name_en in card:
            #print(card[name_en])
            pass
        else:
            #print("Dandan?")
            continue
        brand_candi = [brand[b][0] for b in brand if card[name_en]==b ]
        print(len(brand_candi))
