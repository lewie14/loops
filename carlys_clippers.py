hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

total_price = 0

for price in prices:
	total_price = total_price + price

print(total_price)


average_price = total_price/len(hairstyles)

print("Average Price: <" + str(average_price) +">")


#that average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices = [(price -5) for price in prices]
print(new_prices)


total_revenue = 0

for i in range(len(hairstyles)-1):
	total_revenue += prices[i] * last_week[i]
	print(total_revenue)

print("Total Revenue: <" +str(total_revenue) +">")

average_daily_revenue = total_revenue/7
print("Average Daily Revenue: <" +str(average_daily_revenue) +">")


#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)-1) if new_prices[i] < 30]
print(cuts_under_30)


