# IdiomsByElements
Idioms By Elements.

# Structure
```
IdiomsByElements/
|
+- data/
|  |
|  +- chinese-xinhua/ <-- 引自https://github.com/pwxcoo/chinese-xinhua
|  |  |
|  |  +- data/ <-- 数据文件夹
|  |     |
|  |     +- idiom.json <-- 成语
|  |     |
|  |     +- word.json <-- 汉字
|  |     |
|  |     +- xiehouyu.json <-- 歇后语
|  |     |
|  |     +- ci.json <-- 词语
|  +- elements-pinyin
|     |
|     +- data/ <-- 数据文件夹
|        |
|        +- elements.json <-- 元素名称和拼音
|  
+- lib/
|  |
|  +- IdiomsLexicon/
|  |  |
|  |  +- IdiomsDict.py <--读取json文件，包含get_idioms_json()函数
|  |
|  +- SearchByPinyin/
|     |
|     +- Search.py <--穷举法，search_by_pinyin()函数返回匹配列表
|
+- config.py
|
+- main.py 主程序入口
```

# 待解决的问题

- 充实成语语料库
- 检查错误
- 加入模糊匹配（不考虑语调）
- 核对元素拼音名

# 考虑特性

- 使用其他化学命名词汇如：羟、羧、醛、醇等
- 考虑同音字等的替换
