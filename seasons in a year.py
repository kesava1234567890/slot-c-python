month=input("enter the month eg.jan,feb,mar etc:")
day=int(input("enter the day:"))
    
if month in ('jan','feb','mar'):
    season='spring'
elif month in ('apr','may','jun'):
    season='summer'
elif month in ('jul','aug','sep'):
    season='fall'
elif month in ('oct','nov','dec'):
    season='winter'
    
if(month=='jan')and (day>1):
    season='spring'
elif(month=='apr')and (day>15):
    season='summer'
elif(month=='jul')and (day>12):
    season='fall'
elif(month=='oct')and (day>1):
    season='winter'
print("season is",season)
