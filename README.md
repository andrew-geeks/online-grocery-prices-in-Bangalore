## Historical Online grocery price dataset ~ Bengaluru(Bangalore), India
![workflow badge](https://github.com/andrew-geeks/online-grocery-prices-in-Bangalore/actions/workflows/scrape_price.yml/badge.svg)

Dataset of grocery(vegetables) which includes its daily price📈,MRP,etc in an online site(Bangalore). These data can be helpful in data anaytics and for creating different machine learning models. 
>Prices🏷️ are taken at daily basis. All datasets are stored in .csv format.

## Availabe datasets
* [Potato🥔](https://github.com/andrew-geeks/online-grocery-prices-in-Bangalore/blob/main/datasets/potato1kgprice_dataset.csv) _22-06-2022 onwards(price per kg)_.
* [Onion🧅](https://github.com/andrew-geeks/online-grocery-prices-in-Bangalore/blob/main/datasets/onion1kgprice_dataset.csv) _19-12-2022 onwards(price per kg)_.
* [Tomato🍅](https://github.com/andrew-geeks/online-grocery-prices-in-Bangalore/blob/main/datasets/tomato1kgprice_dataset.csv) _01-08-2023 onwards(price per kg)_.
* [Carrot🥕](https://github.com/andrew-geeks/online-grocery-prices-in-Bangalore/blob/main/datasets/carrot1kgprice_dataset.csv) _01-08-2023 onwards(price per kg)_.

## How are they mined?
We use Selenium library to scrape data from an online site(bigbasket) and store it in csv files. The process is simple and is automated🤖 using GitHub actions. The code runs at 12:00hrs IST in a daily basis. The code is open-source and can be reused. Citations required..

## Libraries Used
* Selenium
* webdriver_manager
* datetime
* csv

## Updates🆕↗️
>- ⚠️03-10-2023: Due to upgradation in source site, data of **September month is not available!** All issues are fixed and data scraping begins from 03-10-2023.
>- 🎯01-08-2023: 2 new datasets have been added!


>If you like these datasets, feel free to star🌟/fork🍴 this [repository](https://github.com/andrew-geeks/online-grocery-prices-in-Bangalore). Thank You🙏!
