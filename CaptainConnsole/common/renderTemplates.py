from django.shortcuts import render


def renderTemplate(request, template, context=None):
    commonParams = {'isLoggedIn': True, 'current_user_id': request.user.id}
    if context is None:
        context = {}
    context.update(commonParams)
    return render(request=request, template_name=template, context=context)
