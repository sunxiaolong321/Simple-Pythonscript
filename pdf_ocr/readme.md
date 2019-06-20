# 光学识别pdf文档

## Request

* glob
* aip
* docx
* PyPDF2
* wand

## 使用百度ocr识别pdf文档

因pdf文档文字为图片，做了这个脚本来识别pdf文档。
APP_ID, API_KEY, SECRET_KEY从百度开发者中心获取，方法不懂请请自行谷歌或查看百度开发者文档。
```
APP_ID = 'APP_ID'
API_KEY = 'API_KEY'
SECRET_KEY = 'SECRET_KEY'
```

## 细部处理

防止文档过多或过大造成的程序卡顿，采用分段处理文档的方式。当时我处理的文档是48MB，代码部分为`run_convert(filename, res)`。
现在发现`convert_pdf(filename, res=120)`居然可以做装饰器，unbelievabl。
