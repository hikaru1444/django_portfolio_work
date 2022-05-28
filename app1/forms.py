from django import forms
from app1.models import Works
import datetime


class TopForm(forms.Form):
    name = forms.CharField(label='名前')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput, required=False)


class WorksForm(forms.Form):
    dt_now = datetime.datetime.now()
    name = forms.CharField(label='名前')
    date = forms.DateField(label='日付', widget=forms.DateInput(attrs={"type": "date"}))
    in_time = forms.TimeField(label='出勤時間',
                              widget=forms.TimeInput(attrs={"type": "time"}, format='%H:%M:%S'))
    out_time = forms.TimeField(label='退勤時間',
                               widget=forms.TimeInput(attrs={"type": "time"}, format='%H:%M:%S'))
    rest_time = forms.TimeField(label='休憩時間',
                                widget=forms.TimeInput(attrs={"type": "time"}, format='%H:%M:%S'))
    other = forms.CharField(label='備考', required=False)
