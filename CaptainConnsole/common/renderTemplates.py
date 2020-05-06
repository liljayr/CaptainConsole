from django.shortcuts import render

commonParams = {'isLoggedIn': True}
def renderTemplate(request, template, params=None):
    if params is None:
        params = {}
    params.update(commonParams)
    return render(request, template, params)