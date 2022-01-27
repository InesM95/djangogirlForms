from django import forms
from .models import Post,Feedback
from .validators import validate_email
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



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
        validators=[validate_email],
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





