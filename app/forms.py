from django import forms
from .models import Institute


class InstituteRegForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(InstituteRegForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ["name",
                                "email",
                                "password",
                                "password_confirm",
                                "contact_person",
                                "address",
                                "area",
                                "city",
                                "phone"]
    
    class Meta:
        model = Institute
        exclude = ('id', 'is_active')
        widgets = {
        'password': forms.PasswordInput(),
    }

    def clean(self):
    	if Institute.objects.filter(name=self.cleaned_data.get('name')).exists():
    		raise forms.ValidationError("%s is already registered with us" % self.cleaned_data['name'])
    	if Institute.objects.filter(email=self.cleaned_data.get('email')).exists():
    		raise forms.ValidationError("%s is already registered with us" % self.cleaned_data['email'])
    	if Institute.objects.filter(phone=self.cleaned_data.get('phone')).exists():
    		raise forms.ValidationError("%s is already registered with us" % self.cleaned_data['phone'])
        if "password" in self.cleaned_data and "password_confirm" in self.cleaned_data:
            if self.cleaned_data["password"] != self.cleaned_data["password_confirm"]:
                raise forms.ValidationError("You must type the same password each time.")
        return self.cleaned_data