#Part one

#Create two dictionaries to represent information about two pets.

Pepper = {"type of pet" : "dog", "color" : "black and tan", "nickname": "bubs", "owners name" : "Kay"};
Kittylicious = {"type of pet" : "cat", "color" : "black", "nickname" : "kit", "owners name" : "Christina"};

#Iterate over each dictionary, printing each key-value pair on one line

for key, value in Pepper.items():
    print(key, ' : ', value)

for key, value in Kittylicious.items():
    print(key, ' : ', value)

#Part two

#Add 3 dictionaries to represent cities around the world

england = {'Capital': 'London'}
france = {'Capital': 'Paris'}
belgium = {'Capital': 'Brussels'}

#Add Information to each dictionary

england["population"] = "53.01 million"
england["interesting fact"] = " "
england["top language spoken by locals"] = " "

france["population"] = "66.9 million"
france["interesting fact"] = " "
france["top language spoken by locals"] = " "

belgium["population"] = "11.35 million"
belgium["interesting fact"] = " "
belgium["top language spoken by locals"] = " "

#Print out key-value pairs

for key, value in england.items():
    	print(key),print(value)

for key, value in france.items():
    	print(key),print(value)

for key, value in belgium.items():
    	print(key),print(value)

#Part three

#Add a dictionary to your program that replicates a user's pizza order. 

pizza_order = { "customer's name": "Jerry", "pizza size ordered": " Large", "type of crust" : "cheesy-crust", "toppings" : "garlic, basil, and olives"}

#Print customers order

print("Thank you for your order, ", pizza_order.get("customer's name"),
	"You have ordered a", pizza_order.get("pizza size ordered"), pizza_order.get("type of crust")," pizza with the following toppings:",
	pizza_order.get("toppings"));
