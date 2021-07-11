# Scrapy Shell Commands

Some of the important shell commands that we need to use while working with Scrapy library are discussed here.

These commands can be executed from the command prompt or, from GitBash terminal.

## Shell Commands

For opening the Scrapy shell:

```shell
scrapy shell
```

To fetch the site URL:

```shell
fetch("https://www.exampleURL.com/")
```

To see the response from the URL:

```shell
response
```

_Note : A response of 200 indicates that the site can be accessed._

After fetching the URL; we can run selector commands as usual to see the output; i.e., we can use `response.xpath()` or, `response.css()`

For quitting the Scrapy Shell:

```cmd
quit()
```
