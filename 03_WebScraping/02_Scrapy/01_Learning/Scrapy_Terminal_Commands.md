# Scrapy Terminal Commands

Some of the important terminal commands that we need to use while working with Scrapy library are discussed here.

These commands can be executed from the command prompt or, from GitBash terminal.

## Terminal Commands

To see the version of Scrapy we are using:

```shell
scrapy --version
```

To get help from Scrapy:

```shell
scrapy --help
```

To start a new Scrapy project:

```shell
scrapy startproject project_name
```

After initiating the project we must move into the _spider_ folder of the project for further code execution.

The CMD code to move into the _spider_ folder is:

```shell
cd project_name\project_name\spiders
```

The GitBash code to move into the _spider_ folder is:

```shell
cd project_name/project_name/spiders
```

Once we are inside the _spider_ folder of the project; we can create python files for web scraping and web crawling.

These python script are commonly known as _spiders_ and we generally use two types of _spider_, such as:

1. ScrapySpider : For Web Scraping
2. CrawlSpider : For Web Crawling

To view various types of _spider_ that we can generate with Scrapy:

```shell
scrapy genspider -l
```

To generate the python script for _ScrapySpider_ project:

```shell
scrapy genspider spider_name siteURL
```

The `spider_name` and `siteURL` portions can be changed within the _spider python script_ and thus, we can also provide any random text instead of these two.

The _ScrapySpider_ falls under the basic/standard template of Scrapy, i.e., it is the default template.

We can also use the following command to generate the basic template as well:

```shell
scrapy genspider -t basic spider_name siteURL
```

The `-t` stands for the _spider template_ that we are going to use.

To generate the python script for _CrawlSpider_ project:

```shell
scrapy genspider -t crawl crawler_name crawlURL
```

The `crawler_name` and `crawlURL` portions can be changed within the _spider python script_ and thus, we can also provide any random text instead of these two.

To start coding with VSCode; we can then execute:

```shell
code .
```

To execute the spider script; we can use either one from the following commands:

```shell
scrapy crawl spider_pythonfile_name
```

or,

```shell
scrapy runspider spider_pythonfile_name.py
```

_Note: In case of `runspider`; we have to give the `.py` extension after the file name whereas, in case of `crawl`; we just have to write the python file name_

To extract the scraped data into a desired file format:

```cmd
scrapy crawl SpiderFileName -o FileName.csv
```

or,

```cmd
scrapy runspider SpiderFileName.py -o FileName.csv
```

`FileName.csv` represents the CSV file where we can save our output. We can change the extension to `json` to save the result in a JSON file.

The `-o` stands for the _Output_.

=========================================

```cmd
scrapy runspider spider_name.py -o saveclassname.csv -t csv -s CLOSESPIDER_PAGECOUNT=10
```
