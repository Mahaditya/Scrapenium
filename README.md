# Scrapenium
General purpose web scraping using Selenium

Right now scraper can scrape elements using xpaths only.
Use chrome developers tools to find xpaths.

#### Entering urls

There is a list in urls.py called url_list.
Enter all the urls you want to scrape from as strings.
Scraper will open each url in order and scrape from that url.

#### Selecting elements to scrape.

There is a dictionary in node_selectors.py called xpaths.

Here are the key value pairs-

Key is a string you want to be the name of your coloumn in csv.
value is a string of xpath of the elements

All the elements mentioned in node_selectors.py xpaths dictionary will be scraped.

from all the pages same elements would be extracted so make sure all the pages have same kind of structure.

