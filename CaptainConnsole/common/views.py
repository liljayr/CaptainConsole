from account.models import Favorite, SearchHistory


def sort_items(sort_by, info):
    if sort_by == "alphabet":
        info = info.order_by('name')
    elif sort_by == "lowest":
        info = info.order_by('price')
    elif sort_by == "highest":
        info = info.order_by('-price')
    return info

def add_favorite(id, hidden, prod_id):
    if hidden == 'games':
        favorite = Favorite(user_id=id, game_id=prod_id)
        favorite.save()
    elif hidden == 'consoles':
        favorite = Favorite(user_id=id, console_id=prod_id)
        favorite.save()

def search_history(id, hidden, search):
    history = SearchHistory(user=id, category=hidden, value=search)
    history.save()

def filter_by_category(category, info):
    if category != "":
        for id in category.split(','):
            info = info.filter(category_id=int(id))
    return info