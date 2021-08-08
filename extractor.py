import re
from collections import Counter

data = open("crawl_result.dat").readlines()
exp_pattern = '(?<=\[).*(?=\])'
exps = [re.search(exp_pattern, text).group() for text in data if re.search(exp_pattern, text)]
Counter(exps)

name_pattern = '(?<=\《).*(?=\》)'

names = [re.search(name_pattern, text).group() for text in data if re.search(name_pattern, text)]
Counter(name)


lang_pattern = '(?<=\【).*(?=\】)'

langs = [re.search(name_pattern, text).group() for text in data if re.search(name_pattern, text)]
Counter(langs)

