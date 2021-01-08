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
        self.fiscalPeriod = {}

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
        '''
        Change the object ticker
        '''
        self.__ticker = ticker
        self.get_urls()
        self.__bsheet_isEmpty = True
        self.__istatement_isEmpty = True
        self.__cflow_isEmpty = True
        self.bsheet_data = {}
        self.istatement_data = {}
        self.cflow_data = {}


    def get_urls(self):
        '''
            Get the urls of the ticker
        '''
        if self.__ticker != None:
            self.__bsheet_url = "https://ca.finance.yahoo.com/quote/" + self.__ticker + '/balance-sheet?p=' + self.__ticker 
            self.__istatement_url = 'https://ca.finance.yahoo.com/quote/' + self.__ticker + '/financials?p=' + self.__ticker
            self.__cflow_url = 'https://ca.finance.yahoo.com/quote/' + self.__ticker + '/cash-flow?p=' + self.__ticker

    def scrapFiscalPeriod(self):
        '''
        Record the fiscal period into a dictionary.
        '''

        bsheet_pg = requests.get(self.__bsheet_url)
        bsheet_soup = BeautifulSoup(bsheet_pg.content, 'html.parser')

        istatement_pg = requests.get(self.__istatement_url)
        istatement_soup = BeautifulSoup(istatement_pg.content, 'html.parser')

        cflow_pg = requests.get(self.__cflow_url)
        cflow_soup = BeautifulSoup(cflow_pg.content, 'html.parser')

        bsheet_table = bsheet_soup.find_all("div", {"class" : "D(tbhg)"})
        istatement_table = istatement_soup.find_all("div", {"class" : "D(tbhg)"})
        cflow_table = cflow_soup.find_all('div', {'class' : 'D(tbhg)'})

        self.fiscalPeriod["Balance Sheet"] = bsheet_table[0].get_text(separator = '|').split('|')[1:]
        self.fiscalPeriod["Income Statement"] = istatement_table[0].get_text(separator = '|').split('|')[1:]
        self.fiscalPeriod["Cash Flow Statement"] = cflow_table[0].get_text(separator = '|').split('|')[1:]

        return self.fiscalPeriod

    def collect_data(self):
        '''
        Collect the data for the ticker using the urls.
        '''

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

        try:
            self.scrapFiscalPeriod()
        except:
            print("ERROR: Fiscal period not found!")

    
    def scrapBSheet(self):
        '''
        Scrap the balance sheet on yFinance
        '''
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
        '''
        Scrap the Income Statement from yFinance webpage
        '''
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
        '''
        Scrap the Cash Flow Statement from yFinance
        '''
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


    def print_bsheet(self):
        line1 = '-' * 110
        line2 = '=' * 110

        bsheet_fmt = "{:<44} | "
        length = len(self.fiscalPeriod['Balance Sheet'])
        for i in range(length):
            if i < length -1:
                bsheet_fmt += "{:<10} | "
            else:
                bsheet_fmt += "{:<10}"

        print(line2)
        if length == 1:
            print(bsheet_fmt.format('Balance Sheet', self.fiscalPeriod['Balance Sheet'][0]))
            print(line1)

            for k, v in self.bsheet_data.items():
                print(bsheet_fmt.format(k, str(v)))
        
        elif length == 2:
            v1, v2 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2))
            print(line1)

            for k, v in self.bsheet_data.items():
                v1, v2 = v
                print(bsheet_fmt.format(k, str(v1), str(v2)))

        elif length == 3:
            v1, v2, v3 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2, v3))
            print(line1)

            for k, v in self.bsheet_data.items():
                v1, v2, v3 = v
                print(bsheet_fmt.format(k, str(v1), str(v2), str(v3)))

        elif length == 4:
            v1, v2, v3, v4 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2, v3, v4))
            print(line1)

            for k, v in self.bsheet_data.items():
                v1, v2, v3, v4 = v
                print(bsheet_fmt.format(k, str(v1), str(v2), str(v3), str(v4)))

        elif length == 5:
            v1, v2, v3, v4, v5 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2, v3, v4, v5))
            print(line1)

            for k, v in self.bsheet_data.items():
                v1, v2, v3, v4, v5 = v
                print(bsheet_fmt.format(k, str(v1), str(v2), str(v3), str(v4), str(v5)))

        print(line2 + '\n')

    def print_istatement(self):
        line1 = '-' * 110
        line2 = '=' * 110

        istatement_fmt = "{:<44} | "
        length = len(self.fiscalPeriod['Income Statement'])
        for i in range(length):
            if i < length - 1:
                istatement_fmt += "{:<10} | "
            else:
                istatement_fmt += "{:<10}"

        print(line2)
        if length == 1:
            print(istatement_fmt.format('Income Statement', self.fiscalPeriod['Income Statement'][0]))
            print(line1)

            for k, v in self.istatement_data.items():
                print(istatement_fmt.format(k, str(v)))
        
        elif length == 2:
            v1, v2 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2))
            print(line1)

            for k, v in self.istatement_data.items():
                v1, v2 = v
                print(istatement_fmt.format(k, str(v1), str(v2)))

        elif length == 3:
            v1, v2, v3 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2, v3))
            print(line1)

            for k, v in self.istatement_data.items():
                v1, v2, v3 = v
                print(istatement_fmt.format(k, str(v1), str(v2), str(v3)))

        elif length == 4:
            v1, v2, v3, v4 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2, v3, v4))
            print(line1)

            for k, v in self.istatement_data.items():
                v1, v2, v3, v4 = v
                print(istatement_fmt.format(k, str(v1), str(v2), str(v3), str(v4)))

        elif length == 5:
            v1, v2, v3, v4, v5 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2, v3, v4, v5))
            print(line1)

            for k, v in self.istatement_data.items():
                v1, v2, v3, v4, v5 = v
                print(istatement_fmt.format(k, str(v1), str(v2), str(v3), str(v4), str(v5)))

        print(line2 + '\n')

    def print_cflow(self):
        line1 = '-' * 110
        line2 = '=' * 110

        cflow_fmt = "{:<44} | "
        length = len(self.fiscalPeriod['Cash Flow Statement'])
        for i in range(length):
            if i < length - 1:
                cflow_fmt += "{:<10} | "
            else:
                cflow_fmt += "{:<10}"

        print(line2)
        if length == 1:
            print(cflow_fmt.format('Cash Flow Statement', self.fiscalPeriod['Cash Flow Statement'][0]))
            print(line1)

            for k, v in self.cflow_data.items():
                print(cflow_fmt.format(k, str(v)))
        
        elif length == 2:
            v1, v2 = self.fiscalPeriod['Cash Flow Statement']
            print(cflow_fmt.format('Cash Flow Statement', v1, v2))
            print(line1)

            for k, v in self.cflow_data.items():
                v1, v2 = v
                print(cflow_data.format(k, str(v1), str(v2)))

        elif length == 3:
            v1, v2, v3 = self.fiscalPeriod['Cash Flow Statement']
            print(cflow_fmt.format('Cash Flow Statement', v1, v2, v3))
            print(line1)

            for k, v in self.cflow_data.items():
                v1, v2, v3 = v
                print(cflow_fmt.format(k, str(v1), str(v2), str(v3)))

        elif length == 4:
            v1, v2, v3, v4 = self.fiscalPeriod['Cash Flow Statement']
            print(cflow_fmt.format('Cash Flow Statement', v1, v2, v3, v4))
            print(line1)

            for k, v in self.cflow_data.items():
                v1, v2, v3, v4 = v
                print(cflow_fmt.format(k, str(v1), str(v2), str(v3), str(v4)))

        elif length == 5:
            v1, v2, v3, v4, v5 = self.fiscalPeriod['Cash Flow Statement']
            print(cflow_fmt.format('Cash Flow Statement', v1, v2, v3, v4, v5))
            print(line1)

            for k, v in self.cflow_data.items():
                v1, v2, v3, v4, v5 = v
                print(cflow_fmt.format(k, str(v1), str(v2), str(v3), str(v4), str(v5)))

        print(line2 + '\n')

    def getBSheetData(self):
        return self.bsheet_data

    def getIStatementData(self):
        return self.istatement_data

    def getCFlowData(self):
        return self.cflow_data

    def getFiscalPeriod(self):
        return self.fiscalPeriod

#========================================== End of Code ===========================================