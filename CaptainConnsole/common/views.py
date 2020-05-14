def sort_items(sort_by, info):
    if sort_by == "alphabet":
        info = info.order_by('name')
    elif sort_by == "lowest":
        info = info.order_by('price')
    elif sort_by == "highest":
        info = info.order_by('-price')
    return info

def filter_by_category(category, info):
    if category != "":
        for id in category.split(','):
            info = info.filter(category_id=int(id))
        print("hellurrr")
        print(category)
        print(info)
    return info