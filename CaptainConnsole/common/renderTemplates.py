from django.shortcuts import render

commonParams = {'isLoggedIn': True}


def renderTemplate(request, template, context=None):
    if context is None:
        context = {}
    context.update(commonParams)
    return render(request=request, template_name=template, context=context)
