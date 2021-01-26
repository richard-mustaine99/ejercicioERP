from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from appEmpresa.models import Contacto
from appEmpresa.models import Empresa
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.template.loader import get_template

#Revisar estos comandos para instalas los paquetes dentro del mismo proyecto
# https://stackoverflow.com/questions/15031694/installing-python-packages-from-local-file-system-folder-to-virtualenv-with-pip
# pip install  --no-index --find-links=file:///Users/victor/Downloads/pyfuzzy-0.1.0 pyfuzzy
# pip install mypackage --no-index --find-links file:///srv/pkg/mypackage
# pip uninstall nombre_paquete

# pip install xlwt
# pip install xlutils
# pip install xlrd
# pip install python-docx
# pip install xhtml2pdf
# pip install virtualenv

# Ambiente virtual:
# .\scripts\activate
# pip install -r requirements.txt
# https://j2logo.com/virtualenv-pip-librerias-python/
# https://www.w3schools.com/howto/howto_js_rangeslider.asp


#Mantenedores ----------------------------------------------------------------------------------------------------------------------
def index(request):
	contactos = Contacto.objects.all()
	empresas = Empresa.objects.all()
	context = { 'contactos': contactos, 'empresas': empresas }
	return render(request, 'appEmpresa/mantenedor.html', context)


#Iniciar/Cerrar sesion ----------------------------------------------------------------------------------------------------------------------
def iniciar_sesion(request):
    context = {}
    return render(request, 'appEmpresa/users/iniciar_sesion.html', context)

def iniciarSesion(request):
    usuario = request.POST["txt_usuario"]
    clave = request.POST["txt_clave"]

    user = authenticate(request, username=usuario, password=clave)


    if user is not None:
        #return HttpResponse("Autenticado!")
        login(request, user)
        return HttpResponseRedirect("/appEmpresa/")
    else:
        return HttpResponseRedirect("/appEmpresa/iniciar_sesion")


def logout(request):
    django_logout(request)
    return render(request, 'appEmpresa/users/iniciar_sesion.html')

#Crear Usuario ----------------------------------------------------------------------------------------------------------------------
def crear_usuario(request):
	context = { }
	return render(request, 'appEmpresa/users/crear_usuario.html', context)

def crearUsuario(request):
	usuario = request.POST["txt_usuario"]
	email = request.POST["txt_email"]
	clave = request.POST["txt_clave"]

	user = User.objects.create_user(usuario, email, clave)

	return HttpResponseRedirect("/appEmpresa/iniciar_sesion/")



