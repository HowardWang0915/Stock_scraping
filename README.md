# Stock Scraping 
A small web-scraping program to scrape financial statements from [goodinfo](goodinfo.tw) using beautifulsoup. 
Reading financial statements can be tough without graph support.
The program can help visualize financial datas to get a breif understanding of the past performance of a company and help you predict the future

## **First features:**
* Operating performance
  * 毛利率
  * 營業利益率
  * 稅後淨利率
  * ROE/ROA
  * EPS
* History Dividend
  * 現金股利
  * 殖利率
* Cash Flow
  * 營業現金流
  * 投資現金流
  * 融資現金流
  * 自由現金流
  * 稅後淨利/營業現金流
  * 期末現金總額
* Estimate your rate of return with Gordon's formula
  * ROE
  * 現金股息殖利率
  * 高登報酬率

## **How to use the program:**
Open terminal and type:
```
python3 goodinfo.py
```
It will prompt
```
Enter the ticker of the stock: 
```
For Example we take 3008 (大力光)
```
Enter the ticker of the stock: 3008
```
It will prompt:
```
1: Operating performance
2: Dividend Policy
3: Cash Statements
4: Rate of Return
q: to quit
Enter: 
```
Say we want to see the operating performance of 3008
```
1: Operating performance
2: Dividend Policy
3: Cash Statements
4: Rate of Return
q: to quit
Enter: 1
```
It will open matplotlib and plot for you.

## **To be added:**
* Balance sheet analysis
* P/E Ratio Analysis
* Technical Analysis but I am so poor at this

## **Known bugs:**
* Companies paying dividend in quaters may cause scraping failure while scaping the dividend data. EX. 2330 台積電
* It is impossible to scrape multiple company's data at one time due to the request limit of the server, might want to change the source of the datas.
* You may exceed the request limit and gets blocked if you use the Gordon's analysis too frequently.
* May want to switch to `seaborn` since `matplotlib` is freaking ugly.
