from renderTemplates import renderTemplate

def index(request):
    return renderTemplate(request, 'games/index.html')
