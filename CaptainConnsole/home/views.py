from django.shortcuts import render

from common.renderTemplates import renderTemplate

games = [
    {'img': 'https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/virtual_console_nintendo_3ds_7/SI_3DSVC_SuperMarioBros.jpg'},
    {'img': 'https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_7/SI_N64_DonkeyKong64_image1600w.jpg'},
    {'img': 'https://www.oldest.org/wp-content/uploads/2017/12/PlayStation_Console.jpg'}
]

#commonParams = {'isLoggedIn': True}

def index(request):
    return render(request, 'home/index.html', {'games': games})


#def renderTemplate(request, template, params):
#   params.update(commonParams)
#   return render(request, template, params)