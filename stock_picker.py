
def calculate_profit (stockList) :

        print (stockList)
        print (max(stockList) - min(stockList))

        if stockList.index(max(stockList)) == 0:
                return 0
        
        return max(stockList) - min (stockList)

