# put your python code here
# put your python code here# put your python code here
days = int(input())
food_per_day = int(input())
oneway_flight = int(input())
one_hight_hotel = int(input())

required_sum = (food_per_day * days) + oneway_flight * 2 + (one_hight_hotel * (days - 1))
print(required_sum)
