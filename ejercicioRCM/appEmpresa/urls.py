from django.urls import path

from .controllers import users
from .controllers import contacto
from .controllers import empresa
from .controllers import comuna

urlpatterns = [
    path('', users.index, name='index'),
#------------------------------------------------------------------------------------------------------------------------

    #ex /appEmpresa/iniciar_sesion/
	path('iniciar_sesion/', users.iniciar_sesion, name='iniciar_sesion'),
	#path(r'$',loging,{'template_name':'formulario_iniciar_sesion'},name='loging'),

	# ex: /appEmpresa/iniciarSesion/
	path('iniciarSesion/', users.iniciarSesion, name='iniciarSesion'),

	# ex: /appEmpresa/crear_usuario/
	path('crear_usuario/', users.crear_usuario, name='crear_usuario'),      			

	# ex: /appEmpresa/crear_usuario/
	path('crearUsuario/', users.crearUsuario, name='crearUsuario'),  

	path('logout/', users.logout, name='logout'),

#------------------------------------------------------------------------------------------------------------------------

	# ex: /appEmpresa/contacto/
	path('contacto/', contacto.contacto, name='contacto'), 

	# ex: /appEmpresa/empresa/
	path('empresa/', empresa.empresa, name='empresa'), 

	# ex: /appEmpresa/comuna/
	# path('comuna/', comuna.comuna, name='comuna'), 

#------------------------------------------------------------------------------------------------------------------------

	# ex: /appEmpresa/formulario_crear_contactos/
	path('formulario_crear_contacto/', contacto.formulario_crear_contacto, name='formulario_crear_contacto'),  

	# ex: /appEmpresa/crearContactos/
	path('appEmpresa/crearContactos/', contacto.crearContactos, name='crearContactos'),  

	#ex /appEmpresa/contactos/editar/2
	path('editar_contacto/<int:contacto_id>/', contacto.editar_contacto, name='editar_contacto'),

	#ex /appEmpresa/contactos/actualizar/
	path('actualizar_contacto/', contacto.actualizar_contacto, name='actualizar_contacto'),

	# ex: /appEmpresa/contactos/eliminar/cargar/3
	path('contacto/eliminar/cargar/<int:contacto_id>', contacto.contacto_eliminar_cargar, name='contacto_eliminar_cargar'),

	# ex: /appEmpresa/contactos/eliminar/confirmar
	path('contacto/eliminar/confirmar/', contacto.contacto_eliminar_confirmar, name='contacto_eliminar_confirmar'),

#------------------------------------------------------------------------------------------------------------------------

    # ex: /appEmpresa/formulario_crear_empresa/
	path('formulario_crear_empresa/', empresa.formulario_crear_empresa, name='formulario_crear_empresa'),  

	# ex: /appEmpresa/crearEmpresas/
	path('appEmpresa/crearEmpresas/', empresa.crearEmpresas, name='crearEmpresas'),  

	#ex /appEmpresa/empresa/editar/2
	path('editar_empresa/<int:empresa_id>/', empresa.editar_empresa, name='editar_empresa'),

	#ex /appEmpresa/empresa/actualizar/
	path('actualizar_empresa/', empresa.actualizar_empresa, name='actualizar_empresa'),

	# ex: /appEmpresa/empresas/eliminar/cargar/3
	path('empresa/eliminar/cargar/<int:empresa_id>', empresa.empresa_eliminar_cargar, name='empresa_eliminar_cargar'),

	# ex: /appEmpresa/empresas/eliminar/confirmar
	path('empresa/eliminar/confirmar/', empresa.empresa_eliminar_confirmar, name='empresa_eliminar_confirmar'),

	# ex: /appEmpresa/agregarContactoEmpresa/
	path('agregarContactoEmpresa/', empresa.agregarContactoEmpresa, name='agregarContactoEmpresa'),  

	# ex: /appEmpresa/empresas/eliminar/contacto/3
	path('empresa/eliminar/contacto/<int:relacion_id>', empresa.empresa_eliminar_contacto, name='empresa_eliminar_contacto'),

	# ex: /appEmpresa/empresas/eliminar/contacto/confirmar
	path('empresa/eliminar/contacto/confirmar/', empresa.empresa_eliminar_contacto_confirmar, name='empresa_eliminar_contacto_confirmar'),

#------------------------------------------------------------------------------------------------------------------------


]