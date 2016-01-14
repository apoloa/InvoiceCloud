# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from google.appengine.api import mail

from users.forms import LoginForm
from users.forms import RegisterForm
from users.models import UsersNonce
from django.core.exceptions import ObjectDoesNotExist

MAIL = 'a@a.com'

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect("invoices_home")


def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append("Nombre de Usuario o contraseña incorrectos")
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'invoices_home')
                    return redirect(url)
                else:
                    error_messages.append("El usuario no está activo")
    else:
        form = LoginForm()
    context = {
        'errors': error_messages,
        'login_form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    '''
    Función que permite el registro de un usuario
    :param request: Request enviado por el cliente
    :return: renderizado del template con la inforamción del contexto
    '''
    error_messages = []
    if request.method == 'POST':  # Si es una petición POST
        form = RegisterForm(request.POST)  # Llenamos el formu
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')
            user = User(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()
            if user is None:
                error_messages.append("Nombre de Usuario o contraseña incorrectos")
            else:
                userNonce = UsersNonce()
                userNonce.Owner = user
                userNonce.Code = user.id
                userNonce.save()
                message = mail.EmailMessage(sender="pvsa92@gmail.com",
                                            subject="Cuenta creada")
                message.to = email
                message.body = "Cuenta creada accede a https://invoicecloud-1143.appspot.com/ac/" + str(
                    user.id) + " \n \n Para la activación del usuario" + "\n\n\n Gracias \n El equipo de InvoiceCloud"
                message.send()
                context = {
                    'username': username
                }
                return render(request, 'users/register.html', context)
    else:  # Si es una petición GET
        form = RegisterForm()  # Creamos el formulario vació, generará los campos y los permitirá añadir de forma dinamica
        # al template
    context = {
        'errors': error_messages,
        'register_form': form
    }
    return render(request, 'users/register.html', context)


def activate_account(request, id):
    try:
        element = UsersNonce.objects.get(Code=id)
        context = {
            'user': element.Owner.username
        }
        element.Owner.is_active = True
        element.Owner.save()
        element.delete()
        return render(request, 'users/account.html', context)
    except ObjectDoesNotExist:
        context = {
            'error': "La petición no es correcta"
        }

    return render(request, 'users/account.html', context)


@login_required()
def view_data(request):
    if request.user.is_authenticated():
        context = {
            'user': request.user
        }
    else:
        context = {
            'error': "Se debe iniciar sessión para ver los datos personales"
        }
    return render(request, 'users/view_user.html', context)