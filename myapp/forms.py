from django import forms
from .models import RomModel, TopicModel
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']





class RomModelForm(forms.ModelForm):
    """Form definition for RomModel."""
    write_topic = forms.CharField(max_length=100, required=False, label="Create new topic")
    topic = forms.ModelChoiceField(queryset=TopicModel.objects.all(), required=False, label="Select existing topic")

    class Meta:
        model = RomModel
        fields = ('write_topic', 'topic', 'name', 'description')

    def clean(self):
        cleaned_data = super().clean()
        write_topic = cleaned_data.get('write_topic')
        topic = cleaned_data.get('topic')

        # Ensure at least one of write_topic or topic is provided
        if not write_topic and not topic:
            raise forms.ValidationError("Please either select an existing topic or enter a new topic.")
        
        return cleaned_data
