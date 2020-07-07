# Problem : If you had deposited a coin on the cryptocurrency exchange
# that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?
coin = 100000
profit = 0.07
income = 0

for a in range(7):
    gain = coin*profit
    income += gain

total_income = coin + income
print(
    f"Toplam kancınız: {income}$'dır. Toplam bakiyeniz: {total_income}$'dır.")
print(
    f"Your interest income is: {income}$. And your Total income is: {total_income}$.")
