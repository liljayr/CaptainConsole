from django.shortcuts import redirect
from common.renderTemplates import renderTemplate
from user.forms.registration import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return renderTemplate(request, 'user/register.html', {
        'form': RegistrationForm()
    })
