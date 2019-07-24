"""aqui se alojaran las vistas de Instagramclone
"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse
import json

#importamos la fecha, son utilidades
from datetime import datetime

#funcion de la vista Hello-World
def hello_world(request):

	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse('Oh, hi! Current server time is {now}'.format(
			now=str(now)
	))

def sort_integers(request):
	"""Return a Json response with sorted integers"""
	#import pdb; pdb.set_trace()
	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	data = {
		'status':'ok',
		'number': sorted_ints,
		'message': 'Integers sorted successfully'
	}
	#dump transforma un diccionario a un json
	return JsonResponse(data, safe = False)


def say_hi(request,name, age):
	""" Return a greeting"""
	if age <12:
		message= 'Sorry {}, you are not allowed here'.format(name)
	else:
		message= 'Hello, {}! Welcome to Instagramclone'.format(name)
	return HttpResponse(message)

