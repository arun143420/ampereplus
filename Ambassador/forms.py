from Ambassador.models import Ambassador
from django import forms


class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = Ambassador
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AmbassadorForm, self).__init__(*args, **kwargs)
        self.fields['college_address'].widget.attrs. \
            update({

            'class': 'single-input',
            'placeholder': 'e:g New delhi, DTU',

        })

        self.fields['motive'].widget.attrs. \
            update({

            'class': 'single-textarea',
            'placeholder': 'Write few lines to explain your motive for becoming campus ambassador',

        })

        self.fields['skills'].widget.attrs. \
            update({

            'class': 'single-input',

            'placeholder': 'e:g JAVA, Python, C, Data Analysis...',

        })

        self.fields['college_name'].widget.attrs. \
            update({

            'class': 'single-input',

            'placeholder': 'e:g MIET',

        })

        self.fields['college_year'].widget.attrs. \
            update({

            'class': 'single-input',

            'placeholder': 'example@example.com',

        })

        self.fields['responsibility'].widget.attrs. \
            update({

            'class':  'single-textarea',

            'placeholder': 'Write few lines about any responisbility realted work you have done in your college. ',

        })






