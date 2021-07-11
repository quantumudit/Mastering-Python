### Selecting an Element

There are four primary methods to select elements in Scrapy; such as:

1. `get()` and `extract_first()`
2. `getall()` and `extract()`

#### `get()` and `extract_first()` Method

Both of these methods are same in terms of functionality.

- Extracts one element only
- If more than one matches are found then it returns only the first match

#### `getall()` and `extract()` Method

Both of these methods are same in terms of functionality.

- Returns a list of elements
- If more than one matches are found then it returns all in a list

### Extracting Data

In Scrapy we can extract data by using 2 types of selectors; such as:

1. CSS Selectors
2. XPath Selectors

#### CSS Selectors

The CSS selectors are relatively easier than the XPath selectors.

Getting the text from a class name:

```python
response.css('.classname::text()').extract()
```

=============================

NOTE (Important):

Xpath escapes the root node and scrapes the whole page and thats when within a loop we need to provide the "." before "//" to force the Xpath to search inside the loop node.

-- Saving the scraped data; run the following command:

PIPELINES :

> in settings.py file uncomment "ITEM_PIPELINES"
