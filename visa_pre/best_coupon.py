x=int(input().strip())
amount_percent_discount=x-(x*0.10)
amount_flat_discount=x-100
final_amount=min(amount_percent_discount,amount_flat_discount)
print(int(final_amount))
