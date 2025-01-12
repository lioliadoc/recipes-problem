def most_varied(recipes):
    chefs_hash_map = {}
    list_of_chefs = []
    for _, chef, ingridients in recipes:
        if chef not in  chefs_hash_map:
            chefs_hash_map[chef] = set(ingridients)
        else:
            for ingridient in ingridients:
                chefs_hash_map[chef].add(ingridient)
    
    max_set = 0        
    for count_ingrid in chefs_hash_map.values():
        if len(count_ingrid) > max_set:
            max_set = len(count_ingrid)

    second_max_set = 0

    for ing_set in chefs_hash_map.values():
        current_size = len(ing_set)
        if current_size > second_max_set and current_size < max_set:
            second_max_set = current_size
        
    
    for key, value in chefs_hash_map.items():
        if len(value) == max_set:
            ingr_tuple = (key, sorted(list(value)))
            list_of_chefs.append(ingr_tuple)

    for key, value in chefs_hash_map.items():
        if len(value) == second_max_set:
            ingr_tuple = (key, sorted(list(value)))
            list_of_chefs.append(ingr_tuple)
    
    return(list_of_chefs)



recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
assert most_varied(recipes_1) == [
    ("Xinting", ["Beef", "Carrot", "Chicken Stock", "Onion", "Peas", "Tomato"]),
    ("Amy", ["Cheese", "Chicken Cream", "Pepper", "Tater tots"])
]

recipes_2 = [
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
assert most_varied(recipes_2) == [
    ("Sam", ["Beef", "Cheese", "Tortilla"]),
    ("Hallie", ["Oil", "Potato"])
]

print("All test cases passed!")
print("Finished early? Discuss time & space complexity.")