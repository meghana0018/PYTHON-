new_count=int(input("enter the number of new loaves purchased:"))
old_count=int(input("enter the number of old loaves purchased:"))
rate_old=(185-(0.6*185))*old_count
rate_new=185*new_count
print("regular price:Rs.185")
print("old loaves amount:Rs.",rate_old)
print("new loaves amount.Rs",rate_new)
print("total amount:Rs.",rate_old+rate_new)
