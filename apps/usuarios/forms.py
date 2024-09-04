from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Insira o usuário de login'
            }
        ),
    )
    senha_login=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite seu nome de usuário'
            }
        )
    )
    email_cadastro=forms.EmailField(label='Email', required=True, max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite seu email',
            }
        )
    )
    senha_cadastro_1=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Digite sua senha',
            }
        )
    )
    senha_cadastro_2=forms.CharField(
        label='Confirme a senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Confirme sua senha',
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome de usuário não pode conter espaços')
            else:
                return nome
            
    def clean_senha_cadastro_2(self):
        senha_1 = self.cleaned_data.get('senha_cadastro_1')
        senha_2 = self.cleaned_data.get('senha_cadastro_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não são iguais')
            else:
                return senha_2
