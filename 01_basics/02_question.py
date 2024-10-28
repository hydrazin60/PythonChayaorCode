RsAdult =  12 #(age >18)
RsChild = 8 
Discount = 2 #wednesday
day =  "Wednesday"

viewerAge = int(input("How old are you? "))
numberOfTickets = int(input("How many tickets are you buying? "))

if(day=="Wednesday"):
    if(viewerAge < 13):
        totalCost = (RsChild * numberOfTickets)
    else:
        totalCost = (RsAdult * numberOfTickets)
else:
    if(viewerAge < 13):
        totalCost = (RsChild * numberOfTickets) - Discount
    else:
        totalCost = (RsAdult * numberOfTickets) - Discount

print("Your total cost is for ", numberOfTickets  ," tickets is ", totalCost,"$") 


