#convert seconds to day, hours, minutes and seconds
S = int(input("Enter the value of second:"))
Day = (((S/60)/60)/24)
print (f"total day for given seconds:{Day} ")
Hour = ((S/60)/60)
print (f"total day for given seconds:{Hour} ")
Minute = (S/60)
print (f"total day for given seconds:{Minute} ")

