from Scrapper import YFinanceScrapper

class StockAnalyzer(YFinanceScrapper):
    def __init__(self, ticker = None):
        super().__init__(ticker = None)

    def __str__(self):
        return super().__str__()

    def vertical_analysis(self):
        pass



#==========================================
analyzer = StockAnalyzer()
print(analyzer)
analyzer.changeTicker('TARO')
analyzer.collect_data()
print(analyzer)
print(analyzer.getBSheetData())