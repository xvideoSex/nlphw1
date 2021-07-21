#encoding=utf-8
import jieba
import jieba.analyse
content = open('hw1-dataset.txt', 'rb').read()
words = jieba.cut(content, cut_all=False)
print("Default Mode: " + ", ".join(words))
