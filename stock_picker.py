
def calculate_profit (stockList) :

        print (stockList)
        print (max(stockList) - min(stockList))

        if stockList.index(max(stockList)) == 0:
                return 0

        if stockList.index(max(stockList)) == 1:
                return max(stockList) - stockList[0]

        if stockList.index(max(stockList)) == 2:
                if stockList[0] <= stockList[1]:
                        return max(stockList) - stockList[0]
                else:
                        return max(stockList) - stockList[1]

        return max(stockList) - min (stockList)

