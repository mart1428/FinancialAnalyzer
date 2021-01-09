from Analyzer import StockAnalyzer
import os

def main():
    analyzer = StockAnalyzer()
    while(True):
        print(menu('0'))

        choice = str(input("Enter choice: "))

        if choice.lower() == "g":
            ticker = str(input("Enter Company's Ticker: "))
            analyzer.changeTicker(ticker.upper())
            print("Financial data received!")

            choice = str(input("Print statements [y/n]? "))
            if choice.lower() == 'y':
                analyzer.print_istatement()
                analyzer.print_bsheet()
                analyzer.print_cflow()

        elif choice.lower() == 'a':
            while(True):
                print(menu('1'))

                choice = str(input("Enter choice: "))

                if choice.lower() == 'v':
                    analyzer.vertical_analysis()
                    choice = str(input("Print result [y/n]? "))

                    if choice.lower() == 'y':
                        analyzer.print_va()
                
                elif choice.lower() == 'h':
                    analyzer.horizontal_analysis()
                    choice = str(input("Print result [y/n]? "))

                    if choice.lower() == 'y':
                        analyzer.print_ha()

                elif choice.lower() == 'l':
                    analyzer.liquidity_analysis()
                    choice = str(input("Print result [y/n]? "))

                    if choice.lower() == 'y':
                        analyzer.print_l_analysis()

                elif choice.lower() == 'q':
                    break

        elif choice.lower() == 'q':
            print("Exiting Program...")
            os._exit(0)

        else:
            print("Invalid choice")

def menu(choice):
    if choice == "0":
        s = '''
             - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            |    G - Get financial data                                               |
            |    A - Perform an analysis // go to sub function                        |
            |    Q - Quit program                                                     |
             - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
            '''

    elif choice == "1":
        s = '''
             - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            |    V - Perform vertical analysis                      |
            |    H - Perform horizontal analysis                    |
            |    L - Perform liquidity analysis                     |
            |    Q - Exit to previous section                       |
             - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            '''


    return s

if __name__ == '__main__':
    main()