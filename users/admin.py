"""User admin classes"""

#DJango
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Model
from users.models import Profile
from django.contrib.auth.models import User
# Register your models here.

#decorador para registro de perfil
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile admin: de que manera presento los datos en el dashboard de admin"""
	list_display = ('pk','user','phone_number','biography','website', 'picture')
	#al presionar el telefono me lleve al detalle del perfil
	list_display_links = ('user','biography')

	#editar en la lista donde se muestra la informacion
	list_editable = ('phone_number','picture')

	#para agregar el campo busqueda en admin
	#NOTA: user es una relacion, no es un campo
	search_fields = ('user__email','user__username','user__first_name','user__last_name','phone_number')

	#agrego filtro por creados y modificados, resguardar el orden
	list_filter = ('created','modified','user__is_active','user__is_staff')

	fieldsets = (
		('Profile',{
			'fields': (('user','picture'),),
			}),
		('Extra info',{
			'fields': (
				('website','phone_number'),
				('biography')
				)
			}),
		('Metadata',{
			'fields':(('created','modified'),),
			})
		)

	readonly_fields = ('created','modified')


class ProfileInline(admin.StackedInline):
	"""Profile in-line admin for users"""
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
	""" Add profile admin to base user admin"""
	inlines = (ProfileInline,)
	list_display = (
		'username',
		'email',
		'first_name',
		'last_name',
		'is_active',
		'is_staff')

# no tenemos que registrar con un decorador
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
