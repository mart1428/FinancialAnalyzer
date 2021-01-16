# Financial Analyzer
A financial analyzer that helps user in analyzing the financial health of a company. The companies' data are obtained through web scrapping (using BeautifulSoup). The analyzer methods will use the selected company fiscal year reports on Yahoo Finance. The purpose of this program is to help user in analyzing a company's health based on the previous financial reports. 

#### Scrapper.py 
Scrapper.py contains YFinanceScrapper class. The object of this class scraps all of the financial statements (Income Statements, Balance Sheet, and Cash Flow Statements). The methods of scraping are based on the html of Yahoo Finance (as of January 17, 2021). This class also contains print methods for printing the financial statements in tabular formats.

#### Analyzer.py
Analyzer.py contains StockAnalyzer class. The object of this class uses various methods of analyzing. The class also inherits YFinanceScrapper from scrapper.py. The available methods of analyzing (as of January 17, 2021) are vertical analysis, horizontal analysis, liquidity analysis, and efficiency analysis. This class also includes print methods for each analyzing methods. 

#### Main.py
Main.py is the main program for this project. Main.py will help user to navigate through the available functions