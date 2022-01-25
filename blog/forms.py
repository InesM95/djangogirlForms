from django import forms
from .models import Post,Feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=80,
        required=True,
    )
    email = forms.EmailField(
        label="E-mail",
        max_length=80,
        required=True,
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}),
        label="FeedBack",
        required=True,
    )

    class Meta:
        model = Feedback
        fields = ("name", "email", "feedback",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-feedbackForm'
        self.helper.form_method = 'post'
        self.helper.form_action = "feedback"
        self.helper.add_input(Submit('submit', 'Submit'))


    def save(self):
        feedback = Feedback(
            name=self.cleaned_data["name"],
            email=self.cleaned_data["email"],
            feedback=self.cleaned_data["feedback"]
        )
        feedback.save()

    def clean_email(self):
        data = self.cleaned_data['email']
        print(data)
        domain = data.split('@')[1]
        domain_list = ["softcatalyst.com", ]
        if domain not in domain_list:
            raise forms.ValidationError("Email is invalid. The email should be a softcatalyst email")

        return data

