import requests
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
from bs4 import BeautifulSoup

def dividend(ticker):
    ## parsing contents
    url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=' + ticker
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    # 設定編碼為 utf-8 避免中文亂碼問題
    resp.encoding = 'utf-8'

    # 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若該網站沒設定可能會有中文亂碼問題。所以通常會使用 resp.encoding 設定
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, 'html.parser')

    # years is the array storing the years
    parse = soup.select('#divDetail > table > tr > td:nth-child(1) > nobr > b')
    year = []
    for i in range(10):
        year.append(float(parse[i].text))
    year.reverse()
    # storing the dividends
    parse = soup.select('#divDetail > table > tr > td:nth-child(8)')
    dividend = []
    for i in range(10):
        dividend.append(float(parse[i].text))
    dividend.reverse()
    # storing the dividend yeild
    parse = soup.select('#divDetail > table > tr > td:nth-child(17)')
    yeild = []
    for i in range(10):
        yeild.append(float(parse[i].text))
    yeild.reverse()
    # draw the plot
    fig, ax1 = plt.subplots()
    plt.title(ticker + ' Dividend and Yield')
    color = 'tab:blue'
    ax1.set_xlabel('year')
    ax1.set_ylabel('$ dividend', color = color)
    ax1.bar(year, dividend, color = color, label = 'dividend')
    
    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_ylabel('% yeild', color = color)
    ax2.plot(year, yeild, 'o-', color = color, label = 'yeild')
    fig.tight_layout()
    plt.show()
# output a specific year
    # print(soup.select('#divDetail > table > tr:nth-child(2) > td:nth-child(1) > nobr > b')[0].text)
    # output a consesutive list

# print(soup.select('#divDetail > table > tr > td:nth-child(2) > nobr > b')[0].text)
# setting up the parsing
def performance(ticker):
    data = 6       # 10 years spam
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=' + ticker
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    # 設定編碼為 utf-8 避免中文亂碼問題
    resp.encoding = 'utf-8'

    # 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若該網站沒設定可能會有中文亂碼問題。所以通常會使用 resp.encoding 設定
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    # Deal with the year
    year = []
    for i in range(data):
        year.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(1) > nobr')[0].text))
    year.reverse()
    # Deal with gross margin
    gm = []     # gross margin
    # 營業利益率 operating profit
    op = []
    # 稅後淨利 net profit after tax
    npaf = []
    # Deal with sales
    sales = []
    # Deal with EPS (net profit)
    eps = []
    # Deal with ROE and ROA
    roe = []
    roa = []
    # Deal with the eps per share
    epst = []
    for i in range(data):
        gm.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(13) > nobr')[0].text))
        op.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(14) > nobr')[0].text))
        npaf.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(16) > nobr')[0].text))
        sales.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(8) > nobr')[0].text.replace(',', '')))
        eps.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(12) > nobr')[0].text.replace(',', '')))
        roe.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(17) > nobr')[0].text.replace(',', '')))
        roa.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(18) > nobr')[0].text.replace(',', '')))
        epst.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(19) > nobr')[0].text.replace(',', '')))
    gm.reverse()
    op.reverse()
    npaf.reverse()
    sales.reverse()
    eps.reverse()
    roa.reverse()
    roe.reverse()
    epst.reverse()

    # draw the plots
    fig, ax1 = plt.subplots(2, sharex=True)
    ax1[0].set_title(ticker + ' Performance')
    ax1[0].bar(year, sales, color = 'tab:pink', label = 'Sales')
    ax1[0].bar(year, eps, color = 'tab:purple', label = 'Net Profit')
    ax1[0].yaxis.grid(linestyle = '-')
    ax1[0].set_ylabel('$ Million Dollars')
    ax1[0].legend(loc = 1)
    ax2 = ax1[0].twinx()
    ax2.set_ylabel('% Percentage')
    ax2.plot(year, gm, 'o-', color = 'tab:red', label = 'Gross Margin')
    ax2.plot(year, op, 'o-', color = 'tab:blue', label = 'Operating profit')
    ax2.plot(year, npaf, 'o-', color = 'tab:green', label = 'Net Profit')
    ax2.legend(loc = 2)
    
    ax1[1].bar(year, epst, color = 'tab:purple', label = 'EPS')
    ax1[1].set_xlabel('Year')
    ax1[1].set_ylabel('$ EPS')
    ax1[1].legend(loc = 1)
    ax3 = ax1[1].twinx()
    ax3.set_ylabel('% Percentage')
    ax3.plot(year, roe, 'o-', color = 'tab:red', label = 'ROE')
    ax3.plot(year, roa, 'o-', color = 'tab:blue', label = 'ROA')
    ax3.legend(loc = 2)
    fig.tight_layout()
    
    plt.show()
def cash(ticker):
    data = 6        # year spam
    url = 'https://goodinfo.tw/StockInfo/StockCashFlow.asp?STOCK_ID=' + ticker
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    # 設定編碼為 utf-8 避免中文亂碼問題
    resp.encoding = 'utf-8'

    # 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若該網站沒設定可能會有中文亂碼問題。所以通常會使用 resp.encoding 設定
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    # Deal with the year
    year = []
    for i in range(data):
        year.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(1) > nobr')[0].text))
    year.reverse()
    # Deal with the Operating cash flow
    ocf = []
    # Deal with investment cash flow
    icf = []
    # Deal with free cash flow ocf + icf
    fcf = []
    # Deal with 融資現金流
    fincf = []
    # Deal with eps 
    eps = [] 
    # Deal with operating cash flow to eps ratio ocf_t_eps
    ocf_t_eps = []
    # Deal with free cash flow to eps ratio fcf_t_eps
    fcf_t_eps = []
    # Deal with final cash amount #row1 > td:nth-child(17)
    final = []
    for i in range(data):
        eps.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(9) > nobr')[0].text.replace(',', '')))
        ocf.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(10) > nobr')[0].text.replace(',', '')))
        icf.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(11) > nobr')[0].text.replace(',', '')))
        fincf.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(12) > nobr')[0].text.replace(',', '')))
        fcf.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(15) > nobr')[0].text.replace(',', '')))
        final.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(17) > nobr')[0].text.replace(',', '')))
        ocf_t_eps.append(ocf[i] / eps[i] * 100)
        fcf_t_eps.append(fcf[i] / eps[i] * 100)

    ocf.reverse()
    icf.reverse()
    fincf.reverse()
    fcf.reverse()
    ocf_t_eps.reverse()
    fcf_t_eps.reverse()
    final.reverse()
    # draw the plots
    fig, ax = plt.subplots(2, sharex=True)
    ax[0].set_title(ticker + ' Cash Flow Statements')
    ax[0].set_ylabel('$ Million Dollars')
    ax[0].yaxis.grid(linestyle = '-')
    ax[0].bar(year, fcf, color = 'tab:purple',label = 'FCF')
    ax[0].plot(year, ocf, 'o-', color = 'tab:red', label = 'OCF')
    ax[0].plot(year, icf, 'o-', color = 'tab:blue', label = 'ICF')
    ax[0].plot(year, fincf, 'o-', color = 'tab:green', label = 'FinCF')
    ax[0].legend(loc = 2)
    ax[1].bar(year, final, color = 'tab:purple', label = 'Cash')
    ax[1].set_ylabel('$Million Dollars')
    ax[1].set_xlabel('Year')
    ax[1].legend(loc = 1)
    ax1 = ax[1].twinx()
    ax1.set_ylabel('% Percentage')
    ax1.plot(year, ocf_t_eps, 'o-', color = 'tab:red', label = 'ocf / eps')
    ax1.plot(year, fcf_t_eps, 'o-', color = 'tab:blue', label = 'fcf / eps')
    ax1.legend(loc = 2)
    fig.tight_layout()
    ax[0].axhline(color = 'black')

    plt.show()
def rate_of_return(ticker):
    data = 6        # year spam
    url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=' + ticker
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    # 設定編碼為 utf-8 避免中文亂碼問題
    resp.encoding = 'utf-8'

    # 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若該網站沒設定可能會有中文亂碼問題。所以通常會使用 resp.encoding 設定
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    # years is the array storing the years
    parse = soup.select('#divDetail > table > tr > td:nth-child(1) > nobr > b')
    year = []
    for i in range(data):
        year.append(float(parse[i].text))
    year.reverse()
    # storing the dividend yeild
    parse = soup.select('#divDetail > table > tr > td:nth-child(17)')
    yeild = []
    for i in range(data):
        yeild.append(float(parse[i].text))
    yeild.reverse()
    # storing 現金股利發放率
    parse = soup.select('#divDetail > table > tr > td:nth-child(24)')
    rate = []
    for i in range(data):
        rate.append(float(parse[i].text))
    rate.reverse()
    # now scarping ROE from other url
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=' + ticker
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    # 設定編碼為 utf-8 避免中文亂碼問題
    resp.encoding = 'utf-8'

    # 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若該網站沒設定可能會有中文亂碼問題。所以通常會使用 resp.encoding 設定
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    # roe
    roe = []
    for i in range(data):
        roe.append(float(soup.select('#row' + str(i + 1) + ' > td:nth-child(17) > nobr')[0].text.replace(',', '')))
    roe.reverse()
    # gordon rate of return and retained earnings growth
    reg = []
    gror = []
    for i in range(data):
        reg.append(float(roe[i] * (1 - rate[i] / 100.)))
        gror.append(float(reg[i] + yeild[i]))
    # draw the plots
    fig, ax = plt.subplots(sharex=True)
    ax.set_title(ticker + ' Rate of Return')
    ax.set_ylabel('% Percentage')
    ax.plot(year, yeild, 'o-', color = 'tab:red', label = 'yeild')
    ax.plot(year, reg, 'o-', color = 'tab:blue', label = 'REG')
    ax.plot(year, gror, 'o-', color = 'tab:green', label = 'Gordon')
    ax.plot(year, roe, 'o-', color = 'tab:purple', label = 'ROE')
    ax.set_xlabel('Year')
    ax.legend()
    plt.show()
    

    

    
if __name__ == "__main__":
    ticker = input("Enter the ticker of the stock: ")
    
    # choice = 3
    while (True):
        
        print('1: Operating performance')
        print('2: Dividend Policy')
        print('3: Cash Statements')
        print('4: Rate of Return')
        print('q: to quit')
        choice = input('Enter: ')
        if (choice == '1'):
            performance(ticker)
        elif(choice == '2'):
            dividend(ticker)
        elif(choice == '3'):
            cash(ticker)
        elif(choice == '4'):
            rate_of_return(ticker)
        elif(choice == 'q'):
            break
        else:
            print('Wrong input')


