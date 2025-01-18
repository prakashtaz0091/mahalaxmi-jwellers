from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(
        
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'johndoe@gmail.com',
            }    
        ))
    
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your message'
        }
    ))
    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )
    
    gender = forms.ChoiceField(choices=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    ), widget=forms.RadioSelect(
        # attrs={
        #     'class': 'form-control'
        # }
    ))
    
    skills = forms.MultipleChoiceField(choices=(
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript', 'JavaScript'),
    ), widget=forms.CheckboxSelectMultiple(
        
    ))
    
    resume = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    date_time = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }
    ))
                               
                               
                               