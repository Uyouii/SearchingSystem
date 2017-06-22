# Searching System

利用倒排索引和向量空间模型实现的信息检索系统

## 运行
环境要求：python3 

在初次运行程序前请下载词干还原依赖的语料库

在main.py中已经注释掉下载语料库的命令
```python
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("punkt")
nltk.download("maxnet_treebank_pos_tagger")
```
取消注释后运行一次即可，语料库下载完成即可正常运行

windows下如果嫌弃语料库下载比较慢，可以直接将根目录下的`nltk_data`文件夹替换掉user下的`AppData/Roaming/nltk_data`文件夹，根目录的`nltk_data`文件夹是已经下载好的语料库

语料库下载完成后请将相应的下载语注释掉。

在`SearchSystem`目录下运行命令：
```batch
python main.py
```

> 注意：运行前请不要修改工程文件的名字和相对位置

`SearchSystem`工程目录是pycharm的工程