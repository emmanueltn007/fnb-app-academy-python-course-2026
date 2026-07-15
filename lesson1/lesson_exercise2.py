# Weight converter

weight = float(input("Weight: "))
conversion_metric = input("(K)g or (L)bs: ")

if conversion_metric.upper() == "K" or "k":
    converted_weight = weight / 0.45
    print(f"Weight in Lbs: {converted_weight}")
else:
    converted_weight = weight * 0.45
    print(f"Weight in Lbs: {converted_weight}")