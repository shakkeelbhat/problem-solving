#converts time in 12 hour format to military time
#'06:40:03AM'-->'06:40:03'
#'12:40:03AM'-->'00:40:03'
#'12:40:03PM'-->'12:40:03'
#'13:40:03AM'-->'01:40:03'
#'11:40:03PM'-->'23:40:03'

def timeConversion(s):
    slen=len(s)
    am_pm=s[8:]
    ha=int(s[:2])
    rem=s[2:8]
    time=''
    if am_pm=='AM':
        print('Morning')
        if ha==12:
            time='00'+rem
        else:
            time='0'+str(ha)+rem
            print(len(time))
    elif am_pm=='PM':
        print('Evening')
        if ha==12:
            time=str(ha)+rem
        else:
            time=str(ha+12)+rem
            
    return time
    
