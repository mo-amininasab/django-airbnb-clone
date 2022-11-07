from django import forms
from . import models


class LoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    email = self.cleaned_data.get('email')
    password = self.cleaned_data.get('password')
    try:
      user = models.User.objects.get(email=email)
      if user.check_password(password):
        return self.cleaned_data
      else:
        # don't raise an error. instead, add the error to a specific filed using the .add_error() method
        # raise forms.ValidationError('Password is wrong')
        self.add_error('password', forms.ValidationError('Password is wrong'))
    except models.User.DoesNotExist:
      # raise forms.ValidationError('User does not exist')
      self.add_error('email', forms.ValidationError('User does not exist'))