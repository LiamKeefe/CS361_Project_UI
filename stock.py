"""
Name: Liam Keefe
Course: CS361 Assignment 7
Due Date: 11/8/2023
Description: Basic UI template for the CS361 Project.
Requires a MacOS/Linux environment for the usage of the clear prompt
"""
import os
import json

################################ System functions


def clear_prompt()-> None:
    """Function that clears the terminal of MacOS/Linux devices"""
    os.system('clear')
    
################################# App functions

def home_page()->str:
    """Home page for the application, returns a string for the next navigation."""
    
    print("\nWelcome to StockApp 1.0")
    print("\n*****NEW FEATURES*******\n-Not applicable (first version)")
    print("\n   The purpose of StockApp is to provide a simple and approachable method to see your favorite market securities: \n\t-StockApp uses searchable Tickers, for your stock options\n\t-StockApp allows the addition to a Watchlist to keep track of stock changes\n\t-StockApp has advanced options of Alerts (email) for price limits\n\t-StockApp provides novel data and filtering options other services may not have")
    print("\n   The StockApp GUI uses a simple linux terminal to operate: \n\t-Follow the options provide on each page\n\t-Number options will preceed the given description of path\n\t-Input of tickers may also be avaiable")
    print("\n   These are the initial pages shown below: \n\t-Search Page is the go-to option for searchable tickers and adding to your Watchlist\n\t-Watchlist page will navigate to display of all recorded watchlist items\n\t-Documentation Page will provide further information of each page and its functionality\n\t-Advanced Options Page will have any under development/early release options.\n\t-Exit will ensure you are exited from StockApp")
    
    print("\nPick an Option")
    print("1 - Search by Ticker")
    print("2 - List current Watchlist")
    print("3 - Documentation")
    print("4 - Advanced Options")
    print("5 - Exit")
    
    inputVar = input("\nPut option here!: ")
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "search"
            elif inputVar == '2':
                return "watchlist"
            elif inputVar == '3':
                return "document"
            elif inputVar == '4':
                return "advance"
            elif inputVar == '5':
                return "exit"
            else:
                InputVar = input("Invalid option, please follow the instructions and put corresponding digit")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit")
        
    return inputVar
    
    

def search_page()->str:
    """Seach page for the application, returns a string for the next navigation."""
    print("\nSearch by Ticker")
    print("\n   Tickers are 3-4 alphabetical characters that are shorthand for the stocks respective company.  Visit https://www.nasdaq.com/ to associate your favorite company to its respective ticker. Note: due to early development, there are only 5 stocks avaiable: MSFT, AAPL, AMD, INTC, TSLA.  ")
    print("\n   Please follow the instructions provide: \n\t-Either put in a numerical option provided below\n\tOr input a ticker for the stock you want to view")
    
    
    print("\nPick an Option")
    print("1 - Home Page")
    print("2 - List current Watchlist")
    print("3 - Documentation")
    print("4 - Advanced Options")
    print("5 - Exit")
    print("Type in the Ticker")
    
    inputVar = input("\nPut option here!: ")
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "home"
            elif inputVar == '2':
                return "watchlist"
            elif inputVar == '3':
                return "document"
            elif inputVar == '4':
                return "advance"
            elif inputVar == '5':
                return "exit"
            else:
                inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            if not ticker_check(inputVar):
                inputVar = input("Invalid Ticker, please select another ticker or option: ")
                continue
            return ticker_info(inputVar)
            
    return inputVar

def ticker_check(ticker: str)-> bool:
    """Checks if ticker is in the list of available stocks.  Takes in the ticker symbol and returns bool"""
    with open('stockfile.json', 'r')  as openfile:
        stock = json.load(openfile)
    if ticker in stock.keys():
        return True
    else:
        return False
    

def ticker_info(ticker: str)->str:
    """Fetches ticker info from JSON file.  Takes in ticker symbol and returns next navigation"""
    with open('stockfile.json', 'r')  as openfile:
        stock = json.load(openfile)
        
    print("\nTicker: " + ticker)
    print("Company: " + stock[ticker]["Company"])
    print("Stock Price: " + str(stock[ticker]["Price"]))
    print("Description: " + stock[ticker]["Description"])
    
    print("\nPick an Option")
    print("Input another ticker, type in ticker")
    print("1 - Add current ticker to Watchlist")
    print("2 - Remove current ticker from Watchlist")
    print("3 - Exit to Search Page")
    print("4 - Exit to Watchlist")
    
    inputVar = input("\nPut option here!: ")
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                watchlist_add(stock, ticker)
                return "search"
            elif inputVar == '3':
                return "search"
            elif inputVar == '4':
                return "watchlist"
            elif inputVar == '2':
                watchlist_delete(ticker)
                return "search"
            else:
                inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
    return inputVar
    
def watchlist_add(stock: dict, ticker: str)->None:
    """Adds stock/ticker to a watchlist.  Inputs a stock list and ticker and returns NONE"""
    if os.path.exists("watchlist.json"):
        with open("watchlist.json", 'r') as infile:
            stockTemp = json.load(infile)
        
        if ticker in stockTemp.keys():
            print("Ticker is already in Watchlist")
            return
        
        stockTemp[ticker] = stock[ticker]
    else:
        stockTemp = {
            ticker : stock[ticker]
        }
    json_object = json.dumps(stockTemp)   
    with open ("watchlist.json", "w") as outfile:
        outfile.write(json_object)
        
def watchlist_delete(ticker)->None:
    """Same as watchlist_add but for delete.  Only takes in ticker"""
    if os.path.exists("watchlist.json"):
        with open("watchlist.json", 'r') as infile:
            stockTemp = json.load(infile)
        
        if ticker not in stockTemp.keys():
            print("Ticker is not in Watchlist.")
            return
        
        stockTemp.pop(ticker)
    else:
        return 
    
    json_object = json.dumps(stockTemp)   
    with open ("watchlist.json", "w") as outfile:
        outfile.write(json_object)
    
def watchlist_page()->str:
    """Watchlist page for the application, returns a string for the next navigation."""
    print("\nHere is your current Watchlist")
    print("\n   You may want to add a few stocks and monitor them thoroughout your time with StockApp.  This is where your Watchlist is provided.  To add stocks to the Watchlist, navigate to the search page, select your desired stock, and then use the add option to the Watchlist. ")
    print("\n   Select an option below to navigate")
    print()
    if os.path.exists("watchlist.json"):
        if os.path.getsize("watchlist.json") == 0:
            print("Watchlist does not exist.  Add to Watchlist before proceeding.")
    else:
        print("Watchlist does not exist.  Add to Watchlist before proceeding.")
        
    with open("watchlist.json", "r") as infile:
        stock = json.load(infile)
        
        print("\nTicker".ljust(10) +
              "Company".ljust(30)+
              "Price".ljust(10))
        print("----------------------------------------------")
        
    for k in stock.keys():
        print(k.ljust(10) +
        str(stock[k]["Company"]).ljust(30) +
        str(stock[k]["Price"]).ljust(10))
        

    print("\nPick an Option")
    print("1 - Home Page")
    print("2 - Exit")
    print("3 - Search by Ticker")
    print("4 - Advanced Options")
    
    inputVar = input("\nPut option here!: ")
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "home"
            elif inputVar == '2':
                return "exit"
            elif inputVar == '3':
                return "search"
            elif inputVar == '4':
                return "advance"
            else:
                inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
            
    return inputVar
    
def doc_page()->str:
    """Document page for the application, returns a string for the next navigation."""
    print("\nDocumentation Menu")
    print("\n   The documentation menu is your location to learn about and understand the functionality of each of the pages to a higher degree.  It is the central location for these documentation pages.")
    print("\n   Select an option for the page you want to view below.\n\tNavigate to the Home or Exit StockApp.  \n\t-Documentation regarding pages")
    
    
    print("\nPick an Option")
    print("1 - Home Page")
    print("2 - Exit")
    print("3 - Documentation on the Search Page")
    print("4 - Documentation on the Documentation Page")
    print("5 - Documentation on the Watchlist page")
    print("6 - Documentation on Email Alerts (not implemented yet)")
    
    inputVar = input("\nPut option here!: ")
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "home"
            elif inputVar == '2':
                return "exit"
            elif inputVar == '3':
                clear_prompt()
                return document_search()
            elif inputVar == '4':
                clear_prompt()
                return document_document()
            elif inputVar == '5':
                clear_prompt()
                return document_watchlist()
            elif inputVar == '6':
                clear_prompt()
                return document_email()
            else:
                inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
            
    return inputVar

def document_search()->str:
    """Documentation on search page for the application, returns a string for the next navigation."""
    print("Information on the Search functionality.  Due to the early stages and insufficient microservices development.  This is current a JSON file with set information about a stock.\n")
    
    print("\nPick an Option")
    print("1 - Documentation")
    print("2 - Search Page")
    print("3 - Home Page")
    print("4 - Exit")
    
    inputVar = input("\nPut option here! ")
    
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "document"
            elif inputVar == '2':
                return "search"
            elif inputVar == '3':
                return "home"
            elif inputVar == '4':
                return "exit"
            else:
                InputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
                
            
    

    
def document_document()->str:
    """Documentation on document page for the application, returns a string for the next navigation."""
    print("Information on the document functionality\n")
    print("The document functionality attempts to provide you with more detail information about each service provided by StockApp.  ")
    
    print("\nPick an Option")
    print("1 - Documentation")
    print("2 - Home Page")
    print("3 - Exit")
    
    inputVar = input("\nPut option here!: ")
    
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "document"
            elif inputVar == '2':
                return "home"
            elif inputVar == '3':
                return "exit"
            else:
                InputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
            
def document_watchlist()->str:
    """Documentation on watchlist page for the application, returns a string for the next navigation."""
    print("Information on the watchlist functionality\n")
    print("The watchlist functionality attempts to provide an easy and filtered options towards your favorite or intesting stock options.")
    
    print("\nPick an Option")
    print("1 - Documentation")
    print("2 - Watchlist page")
    print("3 - Home Page")
    print("4 - Exit")
    
    inputVar = input("\nPut option here!: ")
    
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "document"
            elif inputVar == '3':
                return "home"
            elif inputVar == '4':
                return "exit"
            elif inputVar == '2':
                return "watchlist"
            else:
                InputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
    
def document_email()->str:
    """Documentation on email page for the application, returns a string for the next navigation."""
    print("The following is for information on the email alert system implemented by the application StockApp.  This system is to enable the user to add an email address and a limit, a notification will be sent when the price for the security exceeds the alert price.  Note:  This feature is not yet implemented.\n")
    
    print("\nPick an Option")
    print("1 - Documentation")
    print("2 - Home Page")
    print("3 - Exit")
    
    inputVar = input("\nPut option here!: ")
    
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "document"
            elif inputVar == '2':
                return "home"
            elif inputVar == '3':
                return "exit"
            else:
                InputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
            inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")

def adv_page()->str:
    """Advanced menu page for the application, returns a string for the next navigation."""
    print("\nAdvanced Menu")
    print("\n   This is the page that has all experimental or relatively advanced options related to StockApp.  The documentation or functionality may prove to be incomplete, difficult, or not intended. ")
    print("\n   Proceed with your own risk.  These features are not yet implemented. \n\t-Navigate to Home or Exit StockApp\n\t-Select an advanced function.")

    print("\nPick an Option")
    print("1 - Home Page")
    print("2 - Exit")
    print("3 - Email Alerts (not implemented)")
    print("4 - Price Alerts (not implemented)")
    
    inputVar = input("\nPut option here!: ")
    while(1):
        if inputVar.isdigit():
            if inputVar == '1':
                return "home"
            elif inputVar == '2':
                return "exit"
            elif inputVar == '3':
                inputVar = input("Invalid option, feature is not yet available.  Please pick another option: ")
            elif inputVar == '4':
                inputVar = input("Invalid option, feature is not yet available.  Please pick another option: ")
            else:
                inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
        else:
                inputVar = input("Invalid option, please follow the instructions and put corresponding digit: ")
    return inputVar

def stock_app()->None:
    """Main function that handles navigation requests between the pages."""
    clear_prompt()
    navVal = home_page()
    while(1):
        clear_prompt()
        if navVal == "home":
            navVal = home_page()
        elif navVal == "search":
            navVal = search_page()
        elif navVal == "document":
            navVal = doc_page()
        elif navVal == "watchlist":
            navVal = watchlist_page()
        elif navVal == "advance":
            navVal = adv_page()
        elif navVal == "exit":
            print("Program is exiting, thank you using stockApp")
            exit(1)
        
        

def main():
    stock_app()
    
if __name__ == '__main__':
    main()