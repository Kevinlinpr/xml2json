# XML 格式转换 json

### 依赖

> pip3 install langdetect

### 测试

> python3 xml_to_json.py test/strings.xml zh-cn

> python3 xml_to_json.py test/strings.xml en

> python3 xml_to_json.py test/strings.xml UNKNOWN

### 使用

> python3 xml_to_json.py <source_file> <language_flag>

### language_flag

> iso 639-1

> 支持检测55种语言： af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl, pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw
