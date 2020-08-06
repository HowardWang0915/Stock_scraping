# Stock Scraping 
A small web-scraping program to scrape financial statements from [goodinfo](goodinfo.tw) using beautifulsoup. 
Reading financial statements can be tough without graph support.
The program can help visualize financial datas to get a breif understanding of the past performance of a company and help you predict the future

**First features:**
* Operating performance
* History Dividend
* Cash Flow
* Estimate your rate of return with Gordon's formula
**To be added:**
* Balance sheet analysis

**Known bugs:**
* Companies paying dividend in quaters may cause scraping failure while scaping the dividend data. EX. 2330 台積電
* It is impossible to scrape multiple company's data at one time due to the request limit of the server, might want to change the source of the datas.
* You may exceed the request limit and gets blocked if you use the Gordon's analysis too frequently.
* May want to switch to seaborn since matplotlib is ugly.VV
