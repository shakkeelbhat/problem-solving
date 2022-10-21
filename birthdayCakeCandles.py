#candles=[4,4,1,2,1,5,5,5,9]     since higher number is 9 and it occurs once::return 1
#candles=[4,4,3,3,3,6,6]    since higher number is 6 and it comes 2 times once::return 2

def birthdayCakeCandles(candles):
    count=1
    def resetCount():
        count=1
        return count
    
    max=candles[0]
    for i in range(1,len(candles)):
        if candles[i] <max:
            continue
        elif candles[i]==max:
            count +=1
        else:
            count=resetCount()
            max=candles[i]
            
    return count
            
