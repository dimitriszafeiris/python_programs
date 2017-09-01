#Trip cost
def hotel_cost(nights):
    return 80*nights
    
def plane_ride_cost(city):
    if city == "Athens":
        return 55
    elif city == "NY":
        return 520
    elif city == "Los Angeles":
        return 452 
    elif city == "Paris":
        return 275

def rental_car_cost(days):
    cost = days*40
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)+spending_money


total_cost=trip_cost("Athens",10,1000)
print ("Total cost of the trip will be:", total_cost)