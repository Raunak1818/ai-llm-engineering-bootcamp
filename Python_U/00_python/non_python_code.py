def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_clean_cup():
        bring_wash_cup()
    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    pour("water")
    stir("cup")
    serve("chai")

make_chai()



# This is just to understand 😊