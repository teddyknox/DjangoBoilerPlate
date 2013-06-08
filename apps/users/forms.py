from django.forms import ModelForm
from users.models import UserProfile

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)
		fields = ('name', 'email',)

