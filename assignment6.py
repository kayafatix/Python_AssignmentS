"""
#TASK-1
sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

total_profit = (sales["sell_value"]-sales["cost_value"])*sales["inventory"]
print(f"The total profit is: {total_profit}$, \nand rounded is: {round(total_profit,2)}$")
"""
#TASK-2
desired_output = round(float(input("Please ENTER the amount: ")),2)
#desired_output = round(desired_output,2)
print(desired_output,"$")

