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
        print(self.istatement_data)
        for k,v in self.istatement_data.items():
            va_list = []
            for i in range(len(v)):
                va_list.append((self.istatement_data[k][i]/self.istatement_data['Total Revenue'][i]) * 100)
            va_istatement[k] = self.istatement_data[k]

            print(va_list)



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