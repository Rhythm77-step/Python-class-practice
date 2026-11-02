#Smart traffic light action using nested if-else
#Reading string inputs
"""
time_of_day=input("Enter time of day (Peak/Off-Peak):").strip()
traffic_density=input("Enter traffic density(High,Medium,Low):").strip()
emergency=input("Emergency vehicle detected?(Yes/No):").strip()
#Strictly nested decisiom logic
if emergency.lower()=="yes":
    action="Turn GREEN immediately"
else:
    if time_of_day.lower()=="peak":
        if traffic_density.lower()=="high":
            action="Extend GREEN light duration"
        elif traffic_density.lower()=="medium":
            action="Normal GREEN light duration"
        else:
            action="Reduce GREEEN light duration"
    else:
        #off peak hours behaviour
        action="Normal GREEN light duration"
print(f"Traffic light Action: {action}")
"""
#Smart Airline system with capped discount
#Taking inputs 
age=int(input("Age:"))
travel_class=input("Travel Class:").strip().lower()
frequent_flyer=input("Frequent flyer:").strip().lower()
destination=input("Destination:").strip().lower()
base_price=float(input("Base price:"))
booking_charges=float(input("Booking Charges:"))
#Rule evaluation
if (age<12 and travel_class=="economy") or (frequent_flyer=="yes" and travel_class=="economy"):
    discount=1*booking_charges
elif age >=60 or (travel_class=="first" and destination !="delhi"):
    discount=0.60*base_price
elif travel_class=="business"  and destination=="mumbai":
    discount=(0.10*base_price)+(0.50*booking_charges)
elif frequent_flyer=="yes" and destination=="delhi":
    discount=0.80*booking_charges
else:
    discount=0.10*booking_charges
#Apply ceiling cap: Discount cannot exceed Base price
if discount> base_price:
    discount=base_price
final_ticket_price=base_price +booking_charges-discount
print(f"Discount Applied:{discount:.1f}")
print(f"Final ticket price:{final_ticket_price:.1f}")
















