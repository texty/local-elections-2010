# local-elections-2010-scraper

Ukranian local elections 2010. Candidates, councils and counties.

## Copyright

All data was scraped from [ІАС "Місцеві вибори"](http://cvk.gov.ua/pls/vm2015/) which is an official website of [ЦВК](http://cvk.gov.ua/).

## How to install

1. Install scrapy. See instructions on [official scrapy website](http://scrapy.org/). Install version 1.x
2. Clone or download this repository.

## How to run

    scrapy crawl mayors

## To get csv data

    scrapy crawl municipal -o municipal-2010.csv -t csv


