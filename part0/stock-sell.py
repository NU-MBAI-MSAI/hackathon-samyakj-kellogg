##
## Best time to buy and sell stock (```stocktrading.py```)

# You are given a list ```prices``` where ```prices[i]``` is the price of a given stock on the ```i```th day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Write a function ```maxProfit(prices)``` that calculates the maximum profit you can achieve from this transaction. If you cannot achieve any profit, the return value should be ```0```.

 

# Example:
# ```
# Argument: prices = [7,1,5,3,6,4]

# Return value: 5
# ```
# Explanation: Buy on day ```2``` (```price = 1```) and sell on day ```5``` (```price = 6```), ```profit = 6-1 = 5```.
# Note that buying on day ```2``` and selling on day ```1``` is not allowed because you must buy before you sell.

# Another example:

# ```
# Argument: prices = [7,6,4,3,1]
# Return value: 0
# ```
# Explanation: In this case, no transactions are done and the max ```profit = 0```.
 
 
# * Add code that tests your function. Aim for at least 5 tests that test different scenarios (both black-box and clear-box testing).  

def stock_sell(argument):
    low = argument[0]
    diff = 0
    # traverse the array,
    # keep lowest integer so far, stored.
    # keep calculating stock sell diff so far.
    # if diff more than existing diff, then store this new diff.
    
    for i in argument:
        if i>0:
            if low > i:
                low = i
            if i - low > diff:
                diff = i-low
            
    return diff
        
print (stock_sell([7,6,5,3,2,9]))
print (stock_sell([7,2,5,9.24,2,9]))
print (stock_sell([0,0,-2,3]))
print (stock_sell([6,5,3,10000000000,2,9]))
print (stock_sell([1,2,5,9,90]))
