# Fanancial calculator
# investment and bond.

# investment optoin is calculate by:= (A*L*R)/100
# bond_price option is calculate by:= (A*m)*(t)
import math

investment_option = ("a*L*R/100")
bond_option = ("a*m*t")
print(investment_option)
print(bond_option)
#type of calculation for diffrences option


print("please select your option choice!")
user_option = input(" please select investment or bond:")
if user_option == "investment":
    type_of_interest = input("what type of interrest would you like to use?: ")
    if type_of_interest == "simple interest":
        p = int(input("what is your principal amount?:"))
        r= int(input("how long are you going to invest in ?:"))/100
        t = int(input("what is the rate of interest?:"))
        X = p*(1+r*t)
        print(X)
    elif type_of_interest == "compound interest":
        p = int(input("how much are goint to invest?:"))
        r = float(input("what is your rate of interrest?:"))
        t = int(input("for how many years are you going to invest?:"))
        A = p * math.pow((1 + r /100),t)
        print(A)
elif user_option == "bond": 
        p = int(input("what is the present value of the hourse?:"))
        i = float(input("what is the interst rate?:"))/100/12
        n = int(input("for how many months are you going to repay:"))
        repayment = (i *p)/(1 -(1 + i)**(-n))
        
        print(repayment)
    







