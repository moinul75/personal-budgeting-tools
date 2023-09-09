from django import forms
from .models import User  # Import your user model if it's different

class SignupForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Email'}),
        required=True
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}),
        required=True
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Address'}),
        required=True
    )
    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone'}),
        required=True
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}),
        required=True
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Confirm Password'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'phone']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use.")
        return username
