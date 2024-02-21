#Coffee shop receipt
"""Find the total price of items after tax."""

#Declare and assign variable tax
tax=0.06 

#Ask the user for the price of coffees and muffins
coffee=int(input("what is the price of a coffee?"))
what is the price of a coffee?5

muffin=int(input("what is the price of a muffin?"))
what is the price of a muffin?4 

bagel=int(input("what is the price of a bagel?"))
what is the price of a bagel?3

sandwich=int(input("what is the price of a sandwich?"))
what is the price of a sandwich?7

#Calculate and display the subtotal amount before tax
subtotal=coffee + muffin + bagel + sandwich

print("the subtotal is")
the subtotal is

print(subtotal)
19

print(taxamount)
0.54

#Calculate and display the tax amount
taxamount=subtotal*tax

print("sale tax is")
sale tax is

print(taxamount)
1.14

#Calculate and display the total amount
totalamount=subtotal + taxamount

print("your totalamount is")
your totalamount is

print(totalamount)
20.14

print("""**********************************
    ...: My Coffee and Muffin Shop
    ...: Number of coffees bought?
    ...: 1
    ...: Number of muffins bought?
    ...: 2
    ...: Number of bagels bought?
    ...: 1
    ...: Number of sandwiches bought?
    ...: 1
    ...: **********************************
    ...: 
    ...: **********************************
    ...: My Coffee and Muffin Shop Receipt
    ...: 1 Coffee at $5 each: $ 5.00
    ...: 2 Mufffins at $4 each: $ 8.00
    ...: 1 bagel at $3 each: $ 3.00
    ...: 1 sandwich at $7 each: $ 7.00
    ...: 6% tax: $1.38
    ...: -------
    ...: Total: $ 24.388
    ...: **********************************
    ...: Thank you for purchasing our food
    ...: Hope you enjoy it and have a wonderful day""")
**********************************
My Coffee and Muffin Shop
Number of coffees bought?
1
Number of muffins bought?
2
Number of bagels bought?
1
Number of sandwiches bought?
1
**********************************

**********************************
My Coffee and Muffin Shop Receipt
1 Coffee at $5 each: $ 5.00
2 Mufffins at $4 each: $ 8.00
1 bagel at $3 each: $ 3.00
1 sandwich at $7 each: $ 7.00
6% tax: $1.38
-------
Total: $ 24.388
**********************************
Thank you for purchasing our food
Hope you enjoy it and have a wonderful day
