from Scrapper import YFinanceScrapper

class StockAnalyzer(YFinanceScrapper):
    def __init__(self, ticker = None):
        super().__init__(ticker = None)

    def __str__(self):
        return super().__str__()

    def vertical_analysis(self):
        '''
            Do vertical analysis on each fiscal year report
        '''
        va_istatement = {}
        for k,v in self.istatement_data.items():
            va_list = []
            for i in range(len(v)):
                va_list.append((self.istatement_data[k][i]/self.istatement_data['Total Revenue'][i]) * 100)
            va_istatement[k] = va_list

        va_bsheet = {}
        print(self.bsheet_data)
        switch1 = False
        switch2 = False
        for k,v in self.bsheet_data.items():
            va_list = []
            if k != 'Accounts Payable' and not switch1 and not switch2:
                for i in range(len(v)):
                    va_list.append((self.bsheet_data[k][i]/self.bsheet_data['Total Assets'][i]) * 100)
                va_bsheet[k] = va_list
                switch1 = False
            elif k != 'Common Stock' and not switch2:
                for i in range(len(v)):
                    va_list.append((self.bsheet_data[k][i]/self.bsheet_data['Total Liabilities'][i]) * 100)
                va_bsheet[k] = va_list
                switch1 = True
                switch2 = False
            else:
                for i in range(len(v)):
                    va_list.append((self.bsheet_data[k][i]/self.bsheet_data['Total liabilities and stockholders\' equity'][i]) * 100)
                va_bsheet[k] = va_list
                switch2 = True

        print(va_bsheet)
            
                


#==========================================
analyzer = StockAnalyzer()
# print(analyzer)
analyzer.changeTicker('TARO')
analyzer.collect_data()
# print(analyzer)
# print(analyzer.getBSheetData())
analyzer.scrapFiscalPeriod()
# print(analyzer.getFiscalPeriod())
analyzer.vertical_analysis()