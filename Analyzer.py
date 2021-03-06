from Scrapper import YFinanceScrapper

class StockAnalyzer(YFinanceScrapper):
    def __init__(self, ticker = None):
        super().__init__(ticker = None)
        self.va_istatement = None
        self.va_bsheet = None

        self.ha_istatement = None
        self.ha_bsheet = None

        self.l_analysis = None

        self.e_analysis = None

        self.ror = None

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

        return va_istatement, va_bsheet

    def print_va(self):
        '''
            Print vertical_analysis() result on screen.
        '''

        if(self.va_istatement == None or self.va_bsheet == None):
            print('ERROR: object.vertical_analysis() has not been executed!')
            return -1

        line1 = '-' * 110
        line2 = '=' * 110

        bsheet_fmt = "{:<44} | "
        length = len(self.fiscalPeriod['Balance Sheet'])
        for i in range(length):
            if i < length -1:
                bsheet_fmt += "{:>10} | "
            else:
                bsheet_fmt += "{:>10}"

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

        else:
            print("ERROR")

        print(line2 + '\n')


        istatement_fmt = "{:<44} | "
        length = len(self.fiscalPeriod['Income Statement'])
        for i in range(length):
            if i < length - 1:
                istatement_fmt += "{:>10} | "
            else:
                istatement_fmt += "{:>10}"

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

        else:
            print("ERROR:")

        print(line2 + '\n')
            
    def horizontal_analysis(self, base_year = None, target_year = None):
        '''
            Do horizontal analysis on selected years.
            Year format = YYYY. Example: 2020
            Note: -horizontal analysis is not done on Cash Flow Statement
                  -ttm is not included
                  -this is yearly based analysis
        '''
        ha_istatement = {}
        ha_bsheet = {}

        if base_year == None:
            base_year = input("Enter base year: ")

        if target_year == None:
            target_year = input("Enter target (current) year: ")

        base_year_id = -1
        target_year_id = -1

        counter = 0
        for i in self.fiscalPeriod['Income Statement'][1:]:
            if i[:4] == base_year:
                base_year_id = counter
            elif i[:4] == target_year:
                target_year_id = counter
            counter += 1
            
        for k,v in self.istatement_data.items():
            ha_istatement[k] = [v[target_year_id], v[base_year_id], round((v[target_year_id] - v[base_year_id]) / v[base_year_id] * 100, 2)]
        
        counter = 0
        for i in self.fiscalPeriod['Balance Sheet']:
            if i[:4] == base_year:
                base_year_id = counter
            elif i[:4] == target_year:
                target_year_id = counter
            counter += 1
            
        for k,v in self.bsheet_data.items():
            try:
                ha_bsheet[k] = [v[target_year_id], v[base_year_id], round((v[target_year_id] - v[base_year_id]) / v[base_year_id] * 100, 2)]
            except:
                ha_bsheet[k] = [v[target_year_id], v[base_year_id], '0']


        self.ha_istatement = ha_istatement
        self.ha_bsheet = ha_bsheet

        return [ha_istatement, ha_bsheet]

    def print_ha(self):
        '''
            print horizontal_analysis() result in tabular format
        '''

        line1 = '-' * 92
        line2 = '=' * 92

        if(self.ha_istatement == None or self.ha_bsheet == None):
            print('ERROR: object.horizontal_analysis has not been executed!')
            return -1

        tab_fmt = '{:<44} | {:>19} | {:>10} | {:>10}'

        print(line2)
        print(tab_fmt.format('Income Statement', 'Target/Current Year', 'Base Year', 'Change %'))
        print(line1)

        for k,v in self.ha_istatement.items():
            v1, v2, v3 = v
            print(tab_fmt.format(k, str(v1), str(v2), str(v3) + '%'))

        print(line2 + '\n')

        print(line2)
        print(tab_fmt.format('Balance Sheet', 'Target/Current Year', 'Base Year', 'Change %'))
        print(line1)

        for k,v in self.ha_bsheet.items():
            v1, v2, v3 = v
            print(tab_fmt.format(k, str(v1), str(v2), str(v3) + '%'))

        print(line2)

    def liquidity_analysis(self):
        '''
        Perform liquidity analysis.
        Liquidity analysis consists of current ratio, acid test, cash ratio and net working capital.
        The analysis will be performed on every existing fiscal report except trailing twelve months (ttm).
        '''

        l_analysis = {}
        length = len(self.fiscalPeriod['Balance Sheet'])

        curr_ratio = []
        for i in range(length):
            curr_ratio.append(round(self.bsheet_data.get('Total Current Assets')[i] / self.bsheet_data.get('Total Current Liabilities')[i], 2))        

        quick_ratio = []    #Acid test, Note: Short term investment is not added
        for i in range(length):
            quick_ratio.append(round( ((self.bsheet_data.get('Cash And Cash Equivalents')[i] + self.bsheet_data.get('Net Receivables')[i]) / self.bsheet_data.get('Total Current Liabilities')[i] ), 2))

        cash_ratio = []
        for i in range(length):
            cash_ratio.append(round( (self.bsheet_data.get('Total Cash')[i] / self.bsheet_data.get('Total Current Liabilities')[i] ), 2))

        working_capital = []
        for i in range(length):
            working_capital.append(round( (self.bsheet_data.get('Total Current Assets')[i] - self.bsheet_data.get('Total Current Liabilities')[i] ), 2))
        
        l_analysis['Current Ratio'] = curr_ratio
        l_analysis['Quick Ratio'] = quick_ratio
        l_analysis['Cash Ratio'] = cash_ratio
        l_analysis['Working Capital'] = working_capital

        self.l_analysis = l_analysis

        return l_analysis

    def print_l_analysis(self):
        '''
        Print liquidity analysis results on screen in tabular format.
        '''

        line1 = '-' * 100
        line2 = '=' * 100

        if self.l_analysis == None:
            print("ERROR: liquidity analysis has not been executed!")
            return -1
        
        bsheet_fmt = '{:<44} | '

        length = len(self.fiscalPeriod['Balance Sheet'])
        for i in range(length):
            if i < length -1:
                bsheet_fmt += "{:>10} | "
            else:
                bsheet_fmt += "{:>10}"

        print(line2)
        if length == 1:
            print(bsheet_fmt.format('Liquidity Analysis', self.fiscalPeriod['Balance Sheet'][0]))
            print(line1)

            for k, v in self.l_analysis.items():
                print(bsheet_fmt.format(k, str(v)))
        
        elif length == 2:
            v1, v2 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Liquidity Analysis', v1, v2))
            print(line1)

            for k, v in self.l_analysis.items():
                v1, v2 = v
                print(bsheet_fmt.format(k, str(v1), str(v2)))

        elif length == 3:
            v1, v2, v3 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Liquidity Analysis', v1, v2, v3))
            print(line1)

            for k, v in self.l_analysis.items():
                v1, v2, v3 = v
                print(bsheet_fmt.format(k, str(v1), str(v2), str(v3)))

        elif length == 4:
            v1, v2, v3, v4 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Liquidity Analysis', v1, v2, v3, v4))
            print(line1)

            for k, v in self.l_analysis.items():
                v1, v2, v3, v4 = v
                print(bsheet_fmt.format(k, str(v1), str(v2) , str(v3), str(v4)))

        elif length == 5:
            v1, v2, v3, v4, v5 = self.fiscalPeriod['Balance Sheet']
            print(bsheet_fmt.format('Liquidity Analysis', v1, v2, v3, v4, v5))
            print(line1)

            for k, v in self.l_analysis.items():
                v1, v2, v3, v4, v5 = v
                print(bsheet_fmt.format(k, str(v1), str(v2), str(v3), str(v4), str(v5)))
            
        else:
            print("ERROR:")

        print(line2 + '\n')

    def efficiency_analysis(self):
        '''
        Perform efficiency analysis to the company latest fiscal period. 
        Inventory turnover ratio is only performed if the company has inventory.
        '''
        
        e_analysis = {}

        length = len(self.fiscalPeriod['Balance Sheet'])

        if length <= 1:
            print("ERROR: Not enough data!")
        
        else:
            a_turnover = round(self.istatement_data['Total Revenue'][1] * 2/ (self.bsheet_data['Total Assets'][0] + self.bsheet_data['Total Assets'][1]), 2)

        e_analysis['Asset Turnover Ratio'] = a_turnover

        inventory = self.bsheet_data.get('Inventory', 'None')

        if inventory != 'None':
            i_turnover = round( self.istatement_data['Total Revenue'][1] * 2/ (self.bsheet_data['Inventory'][0] + self.bsheet_data['Inventory'][1]), 2)
            e_analysis['Inventory Turnover Ratio'] = i_turnover

        self.e_analysis = e_analysis

        return e_analysis

    def print_e_analysis(self):
        '''
        Print efficiency analysis result in tabular format
        '''

        line1 = '-' * 60
        line2 = '=' * 60

        if self.e_analysis == None:
            print("ERROR: Efficiency analysis has not been executed!")
            return -1
        
        bsheet_fmt = '{:<44} | {:>10}'
        
        print(line2)
        print(bsheet_fmt.format('Efficiency Analysis', self.fiscalPeriod['Balance Sheet'][0]))
        print(line1)
        for k,v in self.e_analysis.items():
            print(bsheet_fmt.format(k, v))

        print(line2 + '\n')

    def rate_of_return(self):
        '''
        Calculate the rates of return using the last fiscal year report.
        rates of return: - return on equity (roe)
                         - return on assets (roa)
        '''

        ror = {}

        roe = round(self.istatement_data['Net Income'][1] / self.bsheet_data['Total stockholders\' equity'][0], 2)
        roa = round(self.istatement_data['Net Income'][1] * 2 / (self.bsheet_data['Total Assets'][0] + self.bsheet_data['Total Assets'][1]), 2)

        ror['Return on Equity'] = roe
        ror['Return on Assets'] = roa

        self.ror = ror

        return ror

    def print_ror(self):
        '''
        Print rates of return in tabular format
        '''

        line1 = '-' * 60
        line2 = '=' * 60

        if self.ror == None:
            print("ERROR: Rate of return has not been executed!")
            return -1
        
        bsheet_fmt = '{:<44} | {:>10}'
        
        print(line2)
        print(bsheet_fmt.format('Rates of Return', self.fiscalPeriod['Balance Sheet'][0]))
        print(line1)
        for k,v in self.ror.items():
            print(bsheet_fmt.format(k, v))

        print(line2 + '\n')
    

#==========================================End of Code===================================