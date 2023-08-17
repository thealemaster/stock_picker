
def calculate_profit (stockList) :

        lowPrice = stockList[0]
        maxProfit = 0
        
        # if our minimum value is positioned less than the maximum value, our work is pretty much done

        if stockList.index(max(stockList)) >= stockList.index(min(stockList)):
                maxProfit =  max(stockList) - min(stockList)
        else:
                #otherwise, it's time to do some work
                
                for index in range(len(stockList)):
                        if stockList[index] < lowPrice:
                                lowPrice = stockList[index]
                        elif stockList[index] - lowPrice > maxProfit:
                                maxProfit = stockList[index] - lowPrice

        if maxProfit == 0:
                print ("There is no solution in this dataset")
                
        return maxProfit


