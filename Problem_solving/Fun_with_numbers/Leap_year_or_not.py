#Time Complexity -- O(1)
def Is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

