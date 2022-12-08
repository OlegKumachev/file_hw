from pprint import pprint

with open('recipes.txt', encoding='utf-8') as cook:
    cook_book = {}
    for line in cook:
        dish_name = line.strip()
        cout_ingr = int(cook.readline())
        dish_list = []
        for i in range(cout_ingr):
            ing = cook.readline().strip()
            ingredient_name, quantity, measure = ing.split(' | ')
            dish_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        cook.readline()
        cook_book[dish_name] = dish_list




def get_shop_list_by_dishes(dishes, person_count ):
    market_dict ={}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                one_list = {}
                if  ing['ingredient_name'] in market_dict:
                    one_list['measure'] = ing['measure']
                    one_list ['quantity']  = (int(ing['quantity']) + int(ing['quantity'])) * person_count
                    market_dict.update({ing['ingredient_name']: one_list})
                else:
                    one_list['measure'] = ing['measure']
                    one_list['quantity'] = int(ing['quantity']) * person_count
                    market_dict.update({ing['ingredient_name']: one_list})

    return market_dict


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 8))
