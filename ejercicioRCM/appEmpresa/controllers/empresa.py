from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from appEmpresa.models import Empresa
from appEmpresa.models import Contacto
from appEmpresa.models import Relaciones

from django.contrib import messages

def empresa(request):
	listado = Empresa.objects.order_by('id')
	context = {'empresas' : listado}
	return render(request, 'appEmpresa/empresas/mantenedor_empresas.html', context)

def formulario_crear_empresa(request):
	listado = Empresa.objects.all()
	context = {'empresas' : listado}
	return render(request, 'appEmpresa/empresas/formulario_crear_empresa.html', context)

def crearEmpresas(request):
	if request.method == "POST":
		objeto_empresa = Empresa()
		objeto_empresa.RUT_EMPRESA = request.POST["txt_rut"] 
		objeto_empresa.NOMBRE_EMPRESA = request.POST["txt_nombre"] 
		objeto_empresa.DIRECCIÓN = request.POST["txt_direccion"] 
		objeto_empresa.REGION = request.POST["txt_region"]
		objeto_empresa.PROVINCIA = request.POST["txt_provincia"]
		objeto_empresa.COMUNA = request.POST["txt_comuna"]
		get_exists = Empresa.objects.filter(RUT_EMPRESA = objeto_empresa.RUT_EMPRESA)
		if get_exists:
			messages.error(request, 'La empresa que desea agregar ya existe')
			return HttpResponseRedirect('/appEmpresa/formulario_crear_empresa/')
		else:
			objeto_empresa.save()
			messages.success(request, '¡Empresa creada con éxito!')
			return HttpResponseRedirect('/appEmpresa/formulario_crear_empresa/')
	else:
		return HttpResponse("No se permite otro metodo de envío")

def editar_empresa(request, empresa_id):
	empresas = Empresa.objects.get(id=empresa_id)
	contactos = Contacto.objects.all()
	relaciones = Relaciones.objects.filter(ID_EMPRESA = empresa_id)
	context = { 'empresas': empresas, 'contactos': contactos, 'relaciones': relaciones }
	return render(request, 'appEmpresa/empresas/editar_empresa.html', context)

def actualizar_empresa(request):
	if request.method == "POST":
		objeto_empresa = Empresa.objects.get(id = request.POST["id_empresa"])
		objeto_empresa.RUT_EMPRESA = request.POST["txt_rut"] 
		objeto_empresa.NOMBRE_EMPRESA = request.POST["txt_nombre"] 
		objeto_empresa.DIRECCIÓN = request.POST["txt_direccion"] 
		objeto_empresa.REGION = request.POST["txt_region"]
		objeto_empresa.PROVINCIA = request.POST["txt_provincia"]
		objeto_empresa.COMUNA = request.POST["txt_comuna"]
		objeto_empresa.save()
		return HttpResponseRedirect("/appEmpresa/empresa/")
	else:
		return HttpResponse("No se permite otro metodo de envío")

def empresa_eliminar_cargar(request, empresa_id):
	empresas = Empresa.objects.get(id = empresa_id)
	context = { 'empresas' : empresas }
	return render(request, 'appEmpresa/empresas/eliminar_empresa.html', context)

def empresa_eliminar_confirmar(request):
    
	id_empresa = request.POST["id_empresa"]
	empresas = Empresa.objects.get(id = id_empresa)
	try:
		empresas.delete()
	except Exception as e:
		return HttpResponse("No se puede eliminar la empresa")
	return HttpResponseRedirect("/appEmpresa/empresa/")

def agregarContactoEmpresa(request):
	if request.method == "POST":
		objeto_relaciones = Relaciones()
		objeto_relaciones.ID_EMPRESA = request.POST["id_empresa_contact"] 
		objeto_contacto = Contacto.objects.get(id=request.POST["sel_contacto"])
		objeto_relaciones.ID_CONTACTO = objeto_contacto.id
		get_exists = Relaciones.objects.filter(ID_EMPRESA = objeto_relaciones.ID_EMPRESA, ID_CONTACTO = objeto_contacto.id)
		if get_exists:
			messages.error(request, 'El contacto que desea agregar ya se encuentra vinculado a la empresa')
			return HttpResponseRedirect('/appEmpresa/editar_empresa/'+ objeto_relaciones.ID_EMPRESA +'/')
		else:
			objeto_relaciones.save()
			messages.success(request, '¡Contacto vinculado con éxito!')
			return HttpResponseRedirect('/appEmpresa/editar_empresa/'+ objeto_relaciones.ID_EMPRESA +'/')
	else:
		return HttpResponse("No se permite otro metodo de envío")


def empresa_eliminar_contacto(request, relacion_id):
	relaciones = Relaciones.objects.get(id = relacion_id)
	context = { 'relaciones' : relaciones }
	return render(request, 'appEmpresa/empresas/eliminar_contacto_empresa.html', context)


def empresa_eliminar_contacto_confirmar(request):
    
	id_relacion = request.POST["id_relacion"]
	relaciones = Relaciones.objects.get(id = id_relacion)
	try:
		relaciones.delete()
	except Exception as e:
		return HttpResponse("No se puede eliminar el contacto")
	return HttpResponseRedirect("/appEmpresa/empresa/")
