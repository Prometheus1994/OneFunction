print("Enter the number of interval:")
Number = int(input())
Quality = "Major" if Number//2%2 else "Perfect"
Total_of_tones = Number-(Number//4+2)*.5
print("The interval {} needs a {} total of tones to be {}".format(Number,Total_of_tones,Quality))
