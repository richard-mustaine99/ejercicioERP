from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from appEmpresa.models import Empresa
from appEmpresa.models import Contacto

from django.contrib import messages

def contacto(request):
	listado = Contacto.objects.order_by('id')
	context = {'contactos' : listado}
	return render(request, 'appEmpresa/contactos/mantenedor_contactos.html', context)

def formulario_crear_contacto(request):
	listado = Contacto.objects.all()
	context = {'contactos' : listado}
	return render(request, 'appEmpresa/contactos/formulario_crear_contacto.html', context)

def crearContactos(request):
	if request.method == "POST":
		objeto_contacto = Contacto()
		objeto_contacto.RUT_CONTACTO = request.POST["txt_rut"] 
		objeto_contacto.NOM_CONTACTO = request.POST["txt_nombre"] 
		objeto_contacto.APELLP_CONTACTO = request.POST["txt_apellido_p"] 
		objeto_contacto.APELLM_CONTACTO = request.POST["txt_apellido_m"] 
		objeto_contacto.TELEFONO = request.POST["txt_telefono"] 
		objeto_contacto.EMAIL = request.POST["txt_email"] 
		objeto_contacto.DIRECCIÓN = request.POST["txt_direccion"] 
		objeto_contacto.REGION = request.POST["txt_region"]
		objeto_contacto.PROVINCIA = request.POST["txt_provincia"]
		objeto_contacto.COMUNA = request.POST["txt_comuna"]
		get_exists = Contacto.objects.filter(RUT_CONTACTO = objeto_contacto.RUT_CONTACTO)
		if get_exists:
			messages.error(request, 'El contacto que desea agregar ya existe')
			return HttpResponseRedirect('/appEmpresa/formulario_crear_contacto/')
		else:
			objeto_contacto.save()
			messages.success(request, 'Contacto creado con éxito!')
			return HttpResponseRedirect('/appEmpresa/formulario_crear_contacto/')
		return HttpResponseRedirect("/appEmpresa/contacto/")
	else:
		return HttpResponse("No se permite otro metodo de envío")

def editar_contacto(request, contacto_id):
	contactos = Contacto.objects.get(id=contacto_id)
	context = { 'contactos': contactos }
	return render(request, 'appEmpresa/contactos/editar_contacto.html', context)

def actualizar_contacto(request):
	if request.method == "POST":
		objeto_contacto = Contacto.objects.get(id = request.POST["id_contacto"])
		objeto_contacto.RUT_CONTACTO = request.POST["txt_rut"] 
		objeto_contacto.NOM_CONTACTO = request.POST["txt_nombre"] 
		objeto_contacto.APELLP_CONTACTO = request.POST["txt_apellido_p"] 
		objeto_contacto.APELLM_CONTACTO = request.POST["txt_apellido_m"] 
		objeto_contacto.TELEFONO = request.POST["txt_telefono"] 
		objeto_contacto.EMAIL = request.POST["txt_email"] 
		objeto_contacto.DIRECCIÓN = request.POST["txt_direccion"] 
		objeto_contacto.REGION = request.POST["txt_region"]
		objeto_contacto.PROVINCIA = request.POST["txt_provincia"]
		objeto_contacto.COMUNA = request.POST["txt_comuna"]
		objeto_contacto.save()
		return HttpResponseRedirect("/appEmpresa/contacto/")
	else:
		return HttpResponse("No se permite otro metodo de envío")

def contacto_eliminar_cargar(request, contacto_id):
	contactos = Contacto.objects.get(id = contacto_id)
	context = { 'contactos' : contactos }
	return render(request, 'appEmpresa/contactos/eliminar_contacto.html', context)

def contacto_eliminar_confirmar(request):
    
	id_contacto = request.POST["id_contacto"]
	contactos = Contacto.objects.get(id = id_contacto)
	try:
		contactos.delete()
	except Exception as e:
		return HttpResponse("No se puede eliminar un contacto si hay un fiado asociado a este")
	return HttpResponseRedirect("/appEmpresa/contacto/")
