from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from .models import Secretaria, Medico


class SecretariaForm(forms.Form):
    rut = forms.IntegerField()
    nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    apellido_p = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    apellido_m = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )
    category = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )


    rut.widget.attrs['class'] = 'form-control'
    nombres.widget.attrs['class'] = 'form-control'
    apellido_p.widget.attrs['class'] = 'form-control'
    apellido_m.widget.attrs['class'] = 'form-control'
    category.widget.attrs['class'] = 'form-control'

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = '__all__'

    rut = forms.IntegerField()
    nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    apellido_p = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    apellido_m = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )
    category = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )


    rut.widget.attrs['class'] = 'form-control'
    nombres.widget.attrs['class'] = 'form-control'
    apellido_p.widget.attrs['class'] = 'form-control'
    apellido_m.widget.attrs['class'] = 'form-control'
    category.widget.attrs['class'] = 'form-control'

#medico


class MedicoForm(forms.Form):
    rut = forms.IntegerField()
    nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    apellido_p = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    apellido_m = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )
    especialidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )


    rut.widget.attrs['class'] = 'form-control'
    nombres.widget.attrs['class'] = 'form-control'
    apellido_p.widget.attrs['class'] = 'form-control'
    apellido_m.widget.attrs['class'] = 'form-control'
    especialidad.widget.attrs['class'] = 'form-control'

class MedicoForm(forms.ModelForm):
        class Meta:
            model = Medico
            fields = '__all__'

        rut = forms.IntegerField()
        nombres = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
                        ]
        )

        apellido_p = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                        ]
        )
        apellido_m = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                        ]
        )
        especialidad = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                        ]
        )