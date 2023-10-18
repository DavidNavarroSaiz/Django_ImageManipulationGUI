from django import forms
from django.forms import ModelForm
from .models import Image, ThresholdData

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image2analysis',)

class ThresholdForm(ModelForm):
    
    class Meta:
        model = ThresholdData
        fields = ('upperThres', 'lowerThres', )
        widgets = {
            'upperThres': forms.TextInput(attrs={'onChange': 'form.submit();',
                                                        'type':'range', 'min': 0, 'max': 255, 'step': 1}
                                                ),
            'lowerThres': forms.TextInput(attrs={'onChange': 'form.submit();',
                                                        'type':'range', 'min': 0, 'max': 255, 'step': 1, 'value':0}
                                                ),
        }


class HSVRangeForm(forms.Form):
    hu = forms.CharField(
            label = 'Hue Top',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'range', 'min': 0, 'max': 180, 'step': 1, 
                        ':value': 'huValue', 'v-on:input':"huValue = $event.target.value",
                        }
                )
            )
    huBox = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'number', 'min': 0, 'max': 180, 'step': 1,
                        ':value': 'huValue', 'v-on:input':"huValue = $event.target.value",
                        }
                )
        )
    hl = forms.CharField(
            label = 'Hue Bottom',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'range', 'min': 0, 'max': 180, 'step': 1, 
                        ':value': 'hlValue', 'v-on:input':"hlValue = $event.target.value",
                        }
                )
            )

    hlBox = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'number', 'min': 0, 'max': 180, 'step': 1,
                        ':value': 'hlValue', 'v-on:input':"hlValue = $event.target.value",
                        }
                )
        )

    su = forms.CharField(
            label = 'Saturation Top',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'range', 'min': 0, 'max': 255, 'step': 1,  
                        ':value': 'suValue', 'v-on:input':"suValue = $event.target.value",
                        }
                )
            )

    suBox = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'number', 'min': 0, 'max': 180, 'step': 1,
                        ':value': 'suValue', 'v-on:input':"suValue = $event.target.value",
                        }
                )
        )

    sl = forms.CharField(
            label = 'Saturation Bottom',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'range', 'min': 0, 'max': 255, 'step': 1, 
                        ':value': 'slValue', 'v-on:input':"slValue = $event.target.value",
                        }
                )
            )
    
    slBox = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'number', 'min': 0, 'max': 180, 'step': 1,
                        ':value': 'slValue', 'v-on:input':"slValue = $event.target.value",
                        }
                )
        )

    vu = forms.CharField(
            label = 'Value Top',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'range', 'min': 0, 'max': 255, 'step': 1, 
                        ':value': 'vuValue', 'v-on:input':"vuValue = $event.target.value",
                        }
                )
            )

    vuBox = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'number', 'min': 0, 'max': 180, 'step': 1,
                        ':value': 'vuValue', 'v-on:input':"vuValue = $event.target.value",
                        }
                )
        )
    
    vl = forms.CharField(
            label = 'Value Bottom',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'range', 'min': 0, 'max': 255, 'step': 1, 
                        ':value': 'vlValue', 'v-on:input':"vlValue = $event.target.value",
                        }
                )
            )

    vlBox = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={'onChange': 'form.submit();', 'type':'number', 'min': 0, 'max': 180, 'step': 1,
                        ':value': 'vlValue', 'v-on:input':"vlValue = $event.target.value",
                        }
                )
        )