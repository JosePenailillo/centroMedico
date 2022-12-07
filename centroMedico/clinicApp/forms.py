from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from .models import Secretaria, Medico, Paciente, HojaAtencion


class SecretariaForm(forms.Form):
    rut = forms.CharField()
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


    rut.widget.attrs['class'] = 'form-control'
    nombres.widget.attrs['class'] = 'form-control'
    apellido_p.widget.attrs['class'] = 'form-control'
    apellido_m.widget.attrs['class'] = 'form-control'

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = '__all__'

    rut = forms.CharField()
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



    rut.widget.attrs['class'] = 'form-control'
    nombres.widget.attrs['class'] = 'form-control'
    apellido_p.widget.attrs['class'] = 'form-control'
    apellido_m.widget.attrs['class'] = 'form-control'

class Especialidades(forms.Form):
    name = forms.CharField(max_length=50)
    class Meta:
        model = Medico
        fields = '__all__'


#medico


class MedicoForm(forms.Form):
    rut = forms.CharField()
    nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    apellido_p = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    apellido_m = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )

    especialidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='La especialidad debe contener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La especialidad debe contener maximo 15 caracteres'),
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

        rut = forms.CharField()
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
                        validators.MinLengthValidator(3, message='La especialidad debe contener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='La especialdad debe contener maximo 15 caracteres'),
                        ]
        )
        rut.widget.attrs['class'] = 'form-control'
        nombres.widget.attrs['class'] = 'form-control'
        apellido_p.widget.attrs['class'] = 'form-control'
        apellido_m.widget.attrs['class'] = 'form-control'
        especialidad.widget.attrs['class'] = 'form-control'

       #paciente
class PacienteForm(forms.Form):
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

    gender = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El gender debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El gender debe tener maximo 15 caracteres'),

                    ]
    )

    dateB = forms.DateTimeField(
        validators=[]
    )

    address = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El adress debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El adress debe tener maximo 15 caracteres'),

                    ]
    )

    Comuna = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='La comuna debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La comuna debe tener maximo 15 caracteres'),

                    ]
    )

    phone = forms.IntegerField()
    emergencyContact = forms.IntegerField()

    emergencyPhone = forms.IntegerField()


    country = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El country debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El country debe tener maximo 15 caracteres'),

                    ]
    )

    health = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El  campo salud tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo salud debe tener maximo 15 caracteres'),

                    ]
    )
# 2do
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
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

    gender = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El gender debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El gender debe tener maximo 15 caracteres'),

                    ]
    )

    dateB = forms.DateTimeField(
        validators=[]
    )

    address = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El adress debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El adress debe tener maximo 15 caracteres'),

                    ]
    )

    Comuna = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='La comuna debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La comuna debe tener maximo 15 caracteres'),

                    ]
    )

    phone = forms.IntegerField()


    emergencyContact = forms.IntegerField()


    emergencyPhone = forms.IntegerField()


    country = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El country debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El country debe tener maximo 15 caracteres'),

                    ]
    )

    health = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El health debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El health debe tener maximo 15 caracteres'),

                    ]
    )

    rut.widget.attrs['class'] = 'form-control'
    nombres.widget.attrs['class'] = 'form-control'
    apellido_p.widget.attrs['class'] = 'form-control'
    apellido_m.widget.attrs['class'] = 'form-control'
    gender.widget.attrs['class'] = 'form-control'
    dateB.widget.attrs['class'] = 'form-control'
    address.widget.attrs['class'] = 'form-control'
    Comuna.widget.attrs['class'] = 'form-control'
    phone.widget.attrs['class'] = 'form-control'
    emergencyContact.widget.attrs['class'] = 'form-control'
    emergencyPhone.widget.attrs['class'] = 'form-control'
    country.widget.attrs['class'] = 'form-control'
    health.widget.attrs['class'] = 'form-control'


#hoja atencion

class HojaForm(forms.Form):
    rutPaciente = forms.CharField()
    profesionalAtendio = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )

    anamnesisAnterior = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    medicamentosRecetados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    examenesSolicitados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    alergias = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    historialEnfermedades= forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    medicamentosQueToma = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    diagnosticoObtenido = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    observaciones = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )


class HojaForm(forms.ModelForm):
    class Meta:
        model = HojaAtencion
        fields = '__all__'

    rutPaciente = forms.CharField()
    profesionalAtendio  = forms.CharField()
    anamnesisAnterior = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )

    medicamentosRecetados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    examenesSolicitados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    alergias = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    historialEnfermedades = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    medicamentosQueToma = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    diagnosticoObtenido = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    observaciones = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    rutPaciente.widget.attrs['class'] = 'form-control'
    profesionalAtendio.widget.attrs['class'] = 'form-control'
    medicamentosRecetados.widget.attrs['class'] = 'form-control'
    anamnesisAnterior.widget.attrs['class'] = 'form-control'
    examenesSolicitados.widget.attrs['class'] = 'form-control'
    alergias.widget.attrs['class'] = 'form-control'
    historialEnfermedades.widget.attrs['class'] = 'form-control'
    medicamentosQueToma.widget.attrs['class'] = 'form-control'
    diagnosticoObtenido.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'




