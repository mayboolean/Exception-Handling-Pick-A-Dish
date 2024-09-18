def select_dish(foods, selected_food):
    print(f"Ah, {foods[selected_food]}! An excellent choice!")

def your_menu(foods):
    try:
        index = 1
        for dish in foods:
            print(f"{index}. {dish}")
            index += 1
        
        is_valid = False
        while not is_valid:
            selected_choice = int(input("Your order number? "))
            
            if 1 <= selected_choice <= len(foods):
                select_dish(foods, selected_choice - 1)
                is_valid = True
            else: 
                print("Try again")
                
    except IndexError as error:
        print(f"{error} was entered.")
        print("Next time try entering something on the menu!")
    except ValueError as error:
        print(f"{error} was entered.")
        print("Choose a valid menu number to order on the menu!")

menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")