def giveMeFinalAmountAfterDiscountApplied():
    priceOfProduct = input("Enter the price of the product:")
    discountInPercentage = 15
    priceOfProductInFloat = (float)(priceOfProduct)
    discountApplied = (priceOfProductInFloat*(discountInPercentage/100))
    print("Appleid discount amount is ->" , discountApplied)
    finalPriceOfProduct = priceOfProductInFloat-discountApplied
    print("Final price is -> " , finalPriceOfProduct)
    return finalPriceOfProduct

giveMeFinalAmountAfterDiscountApplied()