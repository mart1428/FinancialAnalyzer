#Derived from borisng0112ca/StockScreeningScript/webscraping.py
from bs4 import BeautifulSoup
import requests

class YFinanceScrapper():
    def __init__(self, ticker = None):
        self.__ticker = ticker
        self.bsheet_data = {}
        self.istatement_data = {}
        self.cflow_data = {}
        self.__bsheet_isEmpty = True
        self.__istatement_isEmpty = True
        self.__cflow_isEmpty = True
        if self.__ticker != None:
            self.__bsheet_url = "https://ca.finance.yahoo.com/quote/" + self.__ticker + '/balance-sheet?p=' + self.__ticker 
            self.__istatement_url = 'https://ca.finance.yahoo.com/quote/' + self.__ticker + '/financials?p=' + self.__ticker
            self.__cflow_url = 'https://ca.finance.yahoo.com/quote/' + self.__ticker + '/cash-flow?p=' + self.__ticker

    def __str__(self):
        s = 'Ticker: ' + str(self.__ticker) + '\n' +\
            'Balance Sheet Collected: ' + str(not self.__bsheet_isEmpty) + '\n' + \
            'Income Statement Collected: ' + str(not self.__istatement_isEmpty) + '\n' +\
            'Cash Flow Statement Collected: ' + str(not self.__cflow_isEmpty)
        return s

    def changeTicker(self, ticker):
        self.__ticker = ticker
        self.get_urls()
        self.__bsheet_isEmpty = True
        self.__istatement_isEmpty = True
        self.__cflow_isEmpty = True
        self.bsheet_data = {}
        self.istatement_data = {}
        self.cflow_data = {}


    def get_urls(self):
        if self.__ticker != None:
            self.__bsheet_url = "https://ca.finance.yahoo.com/quote/" + self.__ticker + '/balance-sheet?p=' + self.__ticker 
            self.__istatement_url = 'https://ca.finance.yahoo.com/quote/' + self.__ticker + '/financials?p=' + self.__ticker
            self.__cflow_url = 'https://ca.finance.yahoo.com/quote/' + self.__ticker + '/cash-flow?p=' + self.__ticker

    def collect_data(self):
        try:
            self.scrapBSheet()
        except:
            self.__bsheet_isEmpty = True
        else:
            self.__bsheet_isEmpty = False

        try:
            self.scrapIStatement()
        except:
            self.__istatement_isEmpty = True
        else:
            self.__istatement_isEmpty = False

        try:
            self.scrapCFlow()
        except:
            self.__cflow_isEmpty = True
        else:
            self.__cflow_isEmpty = False

    
    def scrapBSheet(self):
        try:
            pg = requests.get(self.__bsheet_url)
            soup = BeautifulSoup(pg.content, "html.parser")

            table = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
            for i in table:
                rows = i.find_all("div", {"class" : "rw-expnded"})

        except:
            print("ERROR: Ticker not found or wrong URLs")

        else:
            for row in rows:
                col2 = row.get_text(separator = '|').split('|')[1]
                    
                try: 
                    int(col2.replace(',',''))
                except:
                    continue
                else:
                    self.bsheet_data[row.get_text(separator = '|').split('|')[0]] = []
                    for i in row.get_text(separator = '|').split('|')[1:]:
                        dt = i.replace(',','')
                        
                        if(dt == '-'):
                            self.bsheet_data[row.get_text(separator = '|').split('|')[0]].append(0)
                        else:
                            self.bsheet_data[row.get_text(separator = '|').split('|')[0]].append(int(dt))

    def scrapIStatement(self):
        try:
            pg = requests.get(self.__istatement_url)
            soup = BeautifulSoup(pg.content, "html.parser")

            table = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
            for i in table:
                rows = i.find_all("div", {"class" : "rw-expnded"})

        except:
            print("ERROR: Ticker not found or wrong URLs")

        else:
            for row in rows:
                col2 = row.get_text(separator = '|').split('|')[1]
                    
                try: 
                    int(col2.replace(',',''))
                except:
                    continue
                else:
                    self.istatement_data[row.get_text(separator = '|').split('|')[0]] = []
                    for i in row.get_text(separator = '|').split('|')[1:]:
                        dt = i.replace(',','')
                        
                        if(dt == '-'):
                            self.istatement_data[row.get_text(separator = '|').split('|')[0]].append(0)
                        else:
                            self.istatement_data[row.get_text(separator = '|').split('|')[0]].append(int(dt))

    def scrapCFlow(self):
        try:
            pg = requests.get(self.__cflow_url)
            soup = BeautifulSoup(pg.content, "html.parser")

            table = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
            for i in table:
                rows = i.find_all("div", {"class" : "rw-expnded"})

        except:
            print("ERROR: Ticker not found or wrong URLs")
        else:
            for row in rows:
                col2 = row.get_text(separator = '|').split('|')[1]
                    
                try: 
                    int(col2.replace(',',''))
                except:
                    continue
                else:
                    self.cflow_data[row.get_text(separator = '|').split('|')[0]] = []
                    for i in row.get_text(separator = '|').split('|')[1:]:
                        dt = i.replace(',','')
                        
                        if(dt == '-'):
                            self.cflow_data[row.get_text(separator = '|').split('|')[0]].append(0)
                        else:
                            self.cflow_data[row.get_text(separator = '|').split('|')[0]].append(int(dt))

    def getBSheetData(self):
        return self.bsheet_data

    def getIStatementData(self):
        return self.istatement_data

    def getCFlowData(self):
        return self.cflow_data

#==========================================
#---Test---
# yFinanceScrapper = YFinanceScrapper('TARO')

# yFinanceScrapper.collect_data()
# print(yFinanceScrapper.data)

# yFinanceScrapper.changeTicker('TSLA')
# yFinanceScrapper.collect_data()
# print(yFinanceScrapper.data)