# python
学习python ,学习写的爬虫小程序


#创建项目
1、scrapy startproject tencent
2、编写TencentItem 文件，写入要爬取的信息
3、scrapy genspider tencentPosition "tencent.com"
4、编写TencentpositionSpider
5、编写管道文件TencentPipeline
6、在settings.py 打开ITEM——PIPELINES 管道文件配置

