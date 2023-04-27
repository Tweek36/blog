from django import forms
from .models import Blog, Coment

class FeedbackForm(forms.Form):
    internet_choices = (('1', 'Every day'),
                          ('2', 'Several times a day'),
                          ('3', 'Several times a week'),
                          ('4', 'Several times a month')
                          )
    name = forms.CharField(min_length=2, max_length=100)
    name.widget.attrs.update({'class': 'form__input',
                              'placeholder': 'Name'})
    city = forms.CharField(min_length=2, max_length=100)
    city.widget.attrs.update({'class': 'form__input',
                              'placeholder': 'City'})
    job = forms.CharField(min_length=2, max_length=100)
    job.widget.attrs.update({'class': 'form__input',
                              'placeholder': 'Job'})
    gender = forms.ChoiceField(choices=[('1', 'Male'), ('2', 'Female')],
                               widget=forms.RadioSelect, 
                               initial=1)
    gender.widget.attrs.update({'class': 'form__radio'})
    internet = forms.ChoiceField(label='How often do you use the Internet?',
                                 choices=internet_choices)
    internet.widget.attrs.update({'class': 'form__select'})
    email = forms.EmailField(min_length=7)
    email.widget.attrs.update({'class': 'form__input',
                               'placeholder':'example@mail.com'})
    notice = forms.BooleanField(label='Receive news by email?', required=False)
    notice.widget.attrs.update({'class': 'form__checkbox'})
    message = forms.CharField(label='About yourself',
                              widget=forms.Textarea(attrs={'rows':12,
                                                           'cols':20,
                                                           'class': 'form__textarea'}))

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", 'img', 'description', 'content')

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('coment', )