from common.renderTemplates import renderTemplate


def index(request):
    return renderTemplate(request, 'games/index.html')

## games = [
##    {'name': 'Super Mario Bros', 'price': 40.99, 'image': 'SI_3DSVC_SuperMarioBros.jpg'},
##    {'name': 'Tetris', 'price': 15.99, 'image': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Ftetris&psig=AOvVaw3kKNo_X5fOVvXxzAjOMAv2&ust=1588780555759000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNiPp_iKnekCFQAAAAAdAAAAABAD'}
## ]
