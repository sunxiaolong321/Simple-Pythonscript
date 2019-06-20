# 拼接pdf，合成word

##　Request  

* docx
* pdfminer
* python 3.6

## 实现逻辑

使用os.list遍历目录，读取pdf名称和路径，使用pdfminer用于拼接数据，最后存入word中