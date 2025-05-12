from django import forms
from .models import Questions

import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

class UserForm(forms.Form, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"modal-form__input", 'placeholder': 'Имя'}), label='')
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={"class":"modal-form__input", 'placeholder': '+7(___)___-__-__'}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"modal-form__input", 'placeholder': 'Почта'}), label='')
    question = forms.CharField(widget=forms.Textarea(attrs={"class":"modal-form__input", 'placeholder': 'Вопрос', 'rows': 4}), label='')

    class Meta:
        model = Questions
        fields = ('name', 'phoneNumber', 'email', 'question')

# Запрос на проверку введеной капчи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def checkCaptcha(request, type):
    match type:
        case 'question':
            secret=os.getenv('YA_CAPTCHA')
    
    resp = requests.post(
       "https://smartcaptcha.yandexcloud.net/validate",
       data={           
          "secret": secret,
          "token": request.POST.get("smart-token"),
          "ip": get_client_ip(request)
       },
       timeout=1
    )
    
    server_output = resp.content.decode()
    if resp.status_code != 200:
       print(f"Allow access due to an error: code={resp.status_code}; message={server_output}", file=sys.stderr)
       return True
    return json.loads(server_output)["status"] == "ok"
