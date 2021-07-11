# Bypass Restrictions

Many websites generally impose various restrictions to not allow bots to scrape the data from their website.

We can bypass these restrictions Scrapy in various ways; such as:

1. Bypassing restrictions using User-Agent
2. Bypassing restrictions using proxy servers
3. Bypassing restriction by disobeying `robots.txt` guidelines

## Bypassing Restrictions using User-Agent

The website asks for the identity of the browser when we try to browse that website and this identity of the browser is known as _User-Agent_.

**Note**
_To see the User-Agent of our browser; we can simply search: `"what is my user agent"` in our Google Chrome browser_

Some websites restricts our native _User-Agent_ to scrape their website and sometimes they may ban the _User-Agent_ temporarily or, permanently to scrape their website.

There are two ways to bypass such restriction, such as:

1. Using _User-Agents_ allowed by the website
2. Rotating multiple _User-Agents_

### Using _User-Agents_ Allowed by the Website

To bypass these restrictions; we can use _User-Agents_ that are allowed by that particular website.

All of the websites has to allow Google to crawl their website in order to show their content on Google search. So, we can basically replace our _User-Agent_ with Google's _User-Agent_ (AKA _GoogleBot_) to trick the website into thinking that Google is crawling their website and not us.

To use the _GoogleBot_ while scraping the website; we just need to paste the following code snippet in the `settings.py` file of the project:

```python
'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
```

### Rotating Multiple _User-Agents_

Another way to bypass the _User-Agent_ restriction is to keep on rotating multiple _User-Agents_ to fake the website into thinking that a lot of browsers are hitting their website instead of just one.

To do so; we can install a python library named: **scrapy-user-agents**

We have to execute the following command to install the _scrapy-user-agents_ library:

```cmd
pip install scrapy-user-agents
```

After installation, we just need to paste the following code in the `settings.py` file to activate the process while scraping:

```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
```

This library has it's own _User-Agents_ file included in their repository that contains about `2200` user agent strings (i.e., browser names) to rotate through.

## Bypassing Restrictions using Proxy Servers

There are two ways to bypass the restrictions by using proxies; such as:

1. Using python library (Rotating IPs)
2. Manually rotating a list of proxies

### Rotating IPs with Python Library

Some of the websites can recognize our IP address and might ban us if we scrape a lot of data from their website. It can be a temporary or, a permanent ban from their website.

An IP address is basically an unique address of our computer.

**Note**
_To see the IP address of our computer; we can simply search: `"what is my ip"` in our Google Chrome browser_

However, we can also bypass this restriction by using other IP address (or, proxies) instead of our own.

One way to use the proxy servers is to use a different IP address (except our own IP) while requesting the website each time, i.e., rotating the IPs

The proxies we use are not the IP address of any other computer but, these are the unique IPs that are not used by anyone. So, we are not doing any identity theft by using proxy servers.

In order to rotate the IP address while scraping any website; we can make use of a python library named: **scrapy-proxy-pool**

We have to execute the following command to install the _scrapy-proxy-pool_ library:

```cmd
pip install scrapy-proxy-pool
```

After installation, we just need to paste the following code in the `settings.py` file to activate the process while scraping:

```python
PROXY_POOL_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}
```

This library uses the [Free Proxy List](https://free-proxy-list.net/) website to rotate different IPs.

### Manual Method of Using Proxies

We can manually choose some IP addresses to rotate instead of using any library too.

We can get a list of proxies by simple web search. These are nothing but a list of IPs in a text files.

Some of the proxy lists that we can find in GitHub are as follows:

- [Clarketm GitHub Proxy List](https://github.com/clarketm/proxy-list/blob/master/proxy-list.txt)
- [ShiftyTR GitHub Proxy List](https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt)

## Bypassing Restrictions by disobeying `robots.txt` guidelines

Some of the website imposes guidelines against scraping their data and they mentioned it in a file named `robots.txt`

We can view this file by specify `robots.txt` after the main URL of the website.

_For example:_
We can view the `robots.txt` guidelines by Facebook here: [https://facebook.com/robots.txt](https://facebook.com/robots.txt)

By default; Scrapy obeys these guidelines and scrapes the website accordingly; however, sometime these guidelines may restrict us from getting the data that we need.

Therefore, in some cases we need to disobey these guidelines and to do so; we just need to set the `ROBOTSTXT_OBEY` condition to `False` in the `settings.py` file of the Scrapy project; as follows:

```python
ROBOTSTXT_OBEY = False
```
