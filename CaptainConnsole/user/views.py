from django.shortcuts import redirect
from account.forms.account_form import EditImageForm
from account.models import ProfileImage
from common.renderTemplates import renderTemplate
from user.forms.registration import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        #image = ProfileImage.objects.all().filter(user=id).first()
        if form.is_valid():
            user = form.save()
            profile_image = ProfileImage(image=request.POST['image'], user=user)
            profile_image.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            #ProfileImage.img_form = EditImageForm(data=request.POST, instance=image)
            return redirect('login')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return renderTemplate(request, "user/register.html", {"form": form})

    form = RegistrationForm
    return renderTemplate(request, 'user/register.html', {'form': form})
