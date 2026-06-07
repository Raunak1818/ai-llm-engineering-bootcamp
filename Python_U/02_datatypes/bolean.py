is_boiling = True
stri_count = 5
total_actions = stri_count +is_boiling      #upcasting
print(f"TOtal action: {total_actions}")


milk_resent = 0 #no milk
print(f"Is there milk? {bool(milk_resent)}")


water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"can serve chai? {can_serve}")