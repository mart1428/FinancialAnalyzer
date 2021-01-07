from Scrapper import YFinanceScrapper

class StockAnalyzer(YFinanceScrapper):
    def __init__(self, ticker = None):
        super().__init__(ticker = None)
        self.va_istatement = None
        self.va_bsheet = None

    def __str__(self):
        return super().__str__()

    def vertical_analysis(self):
        '''
            Do vertical analysis on each fiscal year report. 
            Note: vertical analysis could not be executed for cash flow statement, thus, cash flow statement is not included 
        '''
        va_istatement = {}
        for k,v in self.istatement_data.items():
            va_list = []
            for i in range(len(v)):
                va_list.append(round((self.istatement_data[k][i]/self.istatement_data['Total Revenue'][i]) * 100, 2))
            va_istatement[k] = va_list

        va_bsheet = {}
        switch1 = False
        switch2 = False
        for k,v in self.bsheet_data.items():
            va_list = []
            if k != 'Accounts Payable' and not switch1 and not switch2:
                for i in range(len(v)):
                    va_list.append(round((self.bsheet_data[k][i]/self.bsheet_data['Total Assets'][i]) * 100, 2))
                va_bsheet[k] = va_list
                switch1 = False
            elif k != 'Common Stock' and not switch2:
                for i in range(len(v)):
                    va_list.append(round((self.bsheet_data[k][i]/self.bsheet_data['Total Liabilities'][i]) * 100, 2))
                va_bsheet[k] = va_list
                switch1 = True
                switch2 = False
            else:
                for i in range(len(v)):
                    va_list.append(round((self.bsheet_data[k][i]/self.bsheet_data['Total liabilities and stockholders\' equity'][i]) * 100, 2))
                va_bsheet[k] = va_list
                switch2 = True

        self.va_istatement = va_istatement
        self.va_bsheet = va_bsheet

    def print_va(self):
        '''
            Print vertical_analysis() result on screen.
        '''

        line1 = '-' * 110
        line2 = '=' * 110

        bsheet_fmt = "{:<43} | "
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

            for k, v in self.va_bsheet.items():
                print(bsheet_fmt.format(k, str(v) + '%'))
        
        elif length == 2:
            v1, v2 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2))
            print(line1)

            for k, v in self.va_bsheet.items():
                v1, v2 = v
                print(bsheet_fmt.format(k, str(v1) + '%', str(v2) + '%'))

        elif length == 3:
            v1, v2, v3 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2, v3))
            print(line1)

            for k, v in self.va_bsheet.items():
                v1, v2, v3 = v
                print(bsheet_fmt.format(k, str(v1) + '%', str(v2) + '%', str(v3) + '%'))

        elif length == 4:
            v1, v2, v3, v4 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2, v3, v4))
            print(line1)

            for k, v in self.va_bsheet.items():
                v1, v2, v3, v4 = v
                print(bsheet_fmt.format(k, str(v1) + '%', str(v2) + '%', str(v3) + '%', str(v4) + '%'))

        elif length == 5:
            v1, v2, v3, v4, v5 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Balance Sheet', v1, v2, v3, v4, v5))
            print(line1)

            for k, v in self.va_bsheet.items():
                v1, v2, v3, v4, v5 = v
                print(bsheet_fmt.format(k, str(v1) + '%', str(v2) + '%', str(v3) + '%', str(v4) + '%', str(v5) + '%'))

        print(line2 + '\n')


        istatement_fmt = "{:<43} | "
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

            for k, v in self.va_istatement.items():
                print(istatement_fmt.format(k, str(v) + '%'))
        
        elif length == 2:
            v1, v2 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2))
            print(line1)

            for k, v in self.va_istatement.items():
                v1, v2 = v
                print(istatement_fmt.format(k, str(v1) + '%', str(v2) + '%'))

        elif length == 3:
            v1, v2, v3 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2, v3))
            print(line1)

            for k, v in self.va_istatement.items():
                v1, v2, v3 = v
                print(istatement_fmt.format(k, str(v1) + '%', str(v2) + '%', str(v3) + '%'))

        elif length == 4:
            v1, v2, v3, v4 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2, v3, v4))
            print(line1)

            for k, v in self.va_istatement.items():
                v1, v2, v3, v4 = v
                print(istatement_fmt.format(k, str(v1) + '%', str(v2) + '%', str(v3) + '%', str(v4) + '%'))

        elif length == 5:
            v1, v2, v3, v4, v5 = self.fiscalPeriod['Income Statement']
            print(istatement_fmt.format('Income Statement', v1, v2, v3, v4, v5))
            print(line1)

            for k, v in self.va_istatement.items():
                v1, v2, v3, v4, v5 = v
                print(istatement_fmt.format(k, str(v1) + '%', str(v2) + '%', str(v3) + '%', str(v4) + '%', str(v5) + '%'))

        print(line2 + '\n')
            
                


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
analyzer.print_va()