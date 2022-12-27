from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from .models import Secretaria, Medico, Paciente, HojaAtencion


class SecretariaForm(forms.Form):
    Rut = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
        ]
    )


    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = '__all__'

    Rut = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
        ]
    )



    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'

class Especialidades(forms.Form):
    name = forms.CharField(max_length=50)
    class Meta:
        model = Medico
        fields = '__all__'


#medico


class MedicoForm(forms.Form):
    Rut = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
        ]
    )


    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'

class MedicoForm(forms.ModelForm):
        class Meta:
            model = Medico
            fields = '__all__'

        Rut = forms.CharField(
            validators=[
                validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
                validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
            ]
        )
        Nombres = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                       message='La primera letra debe ser mayúscula y no debe tener números'),
                        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
                        ]
        )

        Apellido_Paterno = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                       message='La primera letra debe ser mayúscula y no debe tener números'),
                        validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                        validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
                        ]
        )
        Apellido_Materno = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                       message='La primera letra debe ser mayúscula y no debe tener números'),
                        validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                        validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
                        ]
        )
        Rut.widget.attrs['class'] = 'form-control'
        Nombres.widget.attrs['class'] = 'form-control'
        Apellido_Paterno.widget.attrs['class'] = 'form-control'
        Apellido_Materno.widget.attrs['class'] = 'form-control'

       #paciente
class PacienteForm(forms.Form):
    Rut = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
        ]
    )

    Genero = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El Género debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El Género debe tener máximo 25 caracteres'),

                    ]
    )

    Fecha_Nacimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'))

    Direccion = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='La dirección debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La dirección debe tener máximo 50 caracteres'),

                    ]
    )

    Comuna = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='La comuna debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='La comuna debe tener máximo 25 caracteres'),

                    ]
    )

    Telefono = forms.CharField(
        validators=[
            RegexValidator(regex='^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
                           message='Debe contener sólo números ej: +56912345678'),
            validators.MinLengthValidator(12, message='El teléfono debe tener mínimo 12 caracteres'),
            validators.MaxLengthValidator(15, message='El teléfono debe tener máximo 15 caracteres'),
            ]
    )
    Contacto_de_Emergencia = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
        ]
    )

    Telefono_de_Emergencia = forms.CharField(
        validators=[
            RegexValidator(regex='^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
                           message='Debe contener sólo números ej: +56912345678'),
            validators.MinLengthValidator(12, message='El teléfono debe tener mínimo 12 caracteres'),
            validators.MaxLengthValidator(15, message='El teléfono debe tener máximo 15 caracteres'),
            ]
    )

    Nacionalidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='La nacionalidad debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='La nacionalidad debe tener máximo 25 caracteres'),

                    ]
    )

    Sistema_de_Salud = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El Sistema de Salud debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El Sistema de Salud debe tener máximo 25 caracteres'),

                    ]
    )
# 2do
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

    Rut = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
                    ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
                    ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El apellido debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener máximo 25 caracteres'),
                    ]
    )

    Genero = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El Género debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El Género debe tener máximo 25 caracteres'),

                    ]
    )

    Fecha_Nacimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'))

    Direccion = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='La dirección debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La dirección debe tener máximo 50 caracteres'),

                    ]
    )

    Comuna = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='La comuna debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='La comuna debe tener máximo 25 caracteres'),

                    ]
    )

    Telefono = forms.CharField(
        validators=[
            RegexValidator(regex='^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
                           message='Debe contener sólo números e: +56912345678'),
            validators.MinLengthValidator(12, message='El teléfono debe tener mínimo 12 caracteres'),
            validators.MaxLengthValidator(15, message='El teléfono debe tener máximo 15 caracteres'),
            ]
    )

    Contacto_de_Emergencia = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
        validators.MinLengthValidator(3, message='El nombre debe tener mínimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener máximo 50 caracteres'),
        ]
    )


    Telefono_de_Emergencia = forms.CharField(
        validators=[
            RegexValidator(regex='^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
                           message='Debe contener sólo números e: +56912345678'),
            validators.MinLengthValidator(12, message='El teléfono debe tener mínimo 12 caracteres'),
            validators.MaxLengthValidator(15, message='El teléfono debe tener máximo 15 caracteres'),
            ]
    )

    Nacionalidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='La nacionalidad debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='La nacionalidad debe tener máximo 25 caracteres'),

                    ]
    )

    Sistema_de_Salud = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El Sistema de Salud debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El Sistema de Salud debe tener máximo 25 caracteres'),

                    ]
    )

    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'
    Genero.widget.attrs['class'] = 'form-control'
    Fecha_Nacimiento.widget.attrs['class'] = 'form-control'
    Direccion.widget.attrs['class'] = 'form-control'
    Comuna.widget.attrs['class'] = 'form-control'
    Telefono.widget.attrs['class'] = 'form-control'
    Contacto_de_Emergencia.widget.attrs['class'] = 'form-control'
    Telefono_de_Emergencia.widget.attrs['class'] = 'form-control'
    Nacionalidad.widget.attrs['class'] = 'form-control'
    Sistema_de_Salud.widget.attrs['class'] = 'form-control'


#hoja atencion

class HojaForm(forms.Form):
    Rut_Paciente = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Profesional_que_Atendio = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='Debe ingresar como mínimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='Debe ingresar como máximo 50 caracteres'),
                    ]
    )
    Fecha_Atencion = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'))
    Anamnesis = forms.CharField(widget=forms.Textarea())
    Medicamentos_Recetados = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='Debe ingresar como mínimo 3 caracteres'),
                    validators.MaxLengthValidator(250, message='Debe ingresar como máximo 250 caracteres'),
                    ]
    )
    Examenes_Solicitados = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='Debe ingresar como mínimo 3 caracteres'),
                    validators.MaxLengthValidator(250, message='Debe ingresar como máximo 250 caracteres'),

                    ]
    )

    Alergias = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='Debe ingresar como mínimo 3 caracteres'),
                    validators.MaxLengthValidator(125, message='Debe ingresar como máximo 125 caracteres'),

                    ]
    )

    Historial_de_Enfermedades= forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='Debe ingresar como mínimo 3 caracteres'),
                    validators.MaxLengthValidator(500, message='Debe ingresar como máximo 500 caracteres'),

                    ]
    )

    Medicamentos_que_toma = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(250, message='El campo debe tener máximo 250 caracteres'),

                    ]
    )

    Diagnostico = forms.CharField(widget=forms.Textarea())

    Observaciones = forms.CharField(widget=forms.Textarea())


class HojaForm(forms.ModelForm):
    class Meta:
        model = HojaAtencion
        fields = '__all__'

    Rut_Paciente = forms.CharField(
        validators=[
            validators.MinLengthValidator(9, message='El Rut debe tener mínimo 9 caracteres'),
            validators.MaxLengthValidator(11, message='El Rut debe tener máximo 11 caracteres'),
        ]
    )
    Profesional_que_Atendio = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-zÀ-ÿ\u00f1\u00d1]+(\s*[A-Za-zÀ-ÿ\u00f1\u00d1]*)*[A-Za-zÀ-ÿ\u00f1\u00d1]+$',
                                   message='La primera letra debe ser mayúscula y no debe tener números'),
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener máximo 50 caracteres'),
                    ]
    )
    Fecha_Atencion = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'))

    Anamnesis = forms.CharField(widget=forms.Textarea())

    Medicamentos_Recetados = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(250, message='El campo debe tener máximo 250 caracteres'),
                    ]
    )
    Examenes_Solicitados = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(250, message='El campo debe tener máximo 250 caracteres'),
                    ]
    )
    Alergias = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(125, message='El campo debe tener máximo 125 caracteres'),
                    ]
    )
    Historial_de_Enfermedades = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(500, message='El campo debe tener máximo 500 caracteres'),

                    ]
    )

    Medicamentos_que_toma = forms.CharField(
        validators=[
                    validators.MinLengthValidator(3, message='El campo debe tener mínimo 3 caracteres'),
                    validators.MaxLengthValidator(250, message='El campo debe tener máximo 250 caracteres'),

                    ]
    )

    Diagnostico = forms.CharField(widget=forms.Textarea())

    Observaciones = forms.CharField(widget=forms.Textarea())

    Rut_Paciente.widget.attrs['class'] = 'form-control'
    Profesional_que_Atendio.widget.attrs['class'] = 'form-control'
    Fecha_Atencion.widget.attrs['class'] = 'form-control'
    Medicamentos_Recetados.widget.attrs['class'] = 'form-control'
    Anamnesis.widget.attrs['class'] = 'form-control'
    Examenes_Solicitados.widget.attrs['class'] = 'form-control'
    Alergias.widget.attrs['class'] = 'form-control'
    Historial_de_Enfermedades.widget.attrs['class'] = 'form-control'
    Medicamentos_que_toma.widget.attrs['class'] = 'form-control'
    Diagnostico.widget.attrs['class'] = 'form-control'
    Observaciones.widget.attrs['class'] = 'form-control'




