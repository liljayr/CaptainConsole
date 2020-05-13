from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   #favorite_candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
   #profile_image = models.Charfield(max_length=9999)

#   1. búa til migration á Profile til að búa til gagnagrunns-töflu
        # makemigrations
        # migrate

#   2. búa til view fyrir profile töflu inn í user/views.py
#        def profile(request):
#           profile = Profile.objects.filter(user=request.user).first()
            #-> (ég hef aðgang að innskráðum notanda í gegnum request.user)
#           if request.method == 'POST':  (breyta eða bæta við profile)
#               form = ProfileForm(instance=profile, data=request.POST)
#               if form._is_valid():
#                  profile = form.save(commit=False)
#                       (ekki búin að bæta þessu profile modeli við í gagnagrunninn,
#                       þetta er tímabundið profile object. Gert því profile þarf
#                       að innihalda foreign key relation á userinn sem ég er ekki búin
#                       að setja.)
#                  profile.user = request.user
#                  profile.save()
#                  return redirect('profile')
#           return render(request, 'user/profile.html', {
#               'form': ProfileForm(instance=profile)

#   3. búa til profile.html í templates/user
#         {% extends "base.html" %}
#         {% block content%}
#               <form class="form form-horizontal" method="post">
#                   {% csrf_token %}
#                   {{form}}
#                   <input type="submit" class"btn btn-primary" value="Update" />
#               </form>
#         {% endblock %}

#   4. bæta við nýrri python skrá í user/forms sem heitir: profile_form.py
#       from django.forms import ModelForm, widgets
#       from user.models import Profile
#       class ProfileForm(ModelForm)
#           class Meta:
#               model = ProfileForm
#               exclude = [ 'id' , 'user ] (->'user' ætti alltaf að vera bundinn við..
#                                            ..þann user sem er innskráður)
#
#
#               widgets = {
#                   'favorite_candy': widgets.Select(attrs={'class' : 'form-control'},
#                   'profile_image' : widgets.TextInput(attrs={'class' : 'form-control'}
#               }

#   5. stilla upp path-i fyrir profile í user/urls.py
#       path('profile', views.profile, name='profile')

#  6. Undir settings breyta:
#       LOGIN_REDIRECT_URL = /user/profile

#  7. Bæta við link á base.html / navigation.html
#       <li><a href="{% url 'profile' %}>Profile</a></li>