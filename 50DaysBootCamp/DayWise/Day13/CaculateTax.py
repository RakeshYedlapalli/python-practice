def calculateTax():
    price = (float)(input("Enter the tax :"))
    vat = (float)(input("Enter the VAT:"))
    print(type(price))
    return (price * (vat)/100) + (price)

result = calculateTax()
print("Price of the item including Tax is >",result)

    