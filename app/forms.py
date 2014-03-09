from django import forms
from .models import Institute


class InstituteRegForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, help_text='Required minimum 6 characters')

    def __init__(self, *args, **kwargs):
        super(InstituteRegForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ["name",
                                "email",
                                "password",
                                "confirm_password",
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


    def clean_name(self):
    	if Institute.objects.filter(name=self.cleaned_data.get('name')).exists():
    		raise forms.ValidationError("Institute name already exists")
    	return self.cleaned_data['name']

    def clean_email(self):
    	if Institute.objects.filter(email=self.cleaned_data.get('email')).exists():
    		raise forms.ValidationError("%s is already registered with us" % self.cleaned_data['email'])
    	return self.cleaned_data['email']

    def clean(self):
    	if "password" in self.cleaned_data and "confirm_password" in self.cleaned_data:
            if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
                raise forms.ValidationError("You must type the same password each time.")
        return self.cleaned_data
