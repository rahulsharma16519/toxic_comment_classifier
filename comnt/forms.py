from django import forms
from comnt.models import Comments

class CommentsForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('uname', 'inp_comment')
