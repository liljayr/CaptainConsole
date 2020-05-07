from renderTemplates import renderTemplate

def index(request):
    return renderTemplate(request, 'about_us/index.html')
