"""Posts views"""
#Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView,DetailView
from django.urls import reverse_lazy


#Forms
from posts.forms import PostForm

#render recibe un reques, recibe el template y un context
#from datetime import datetime

#Model
from posts.models import Post


#solo podemos acceder a un feed si tenemos una sesion activa
#y solo se ejecuta login_required si hay una sesion activa

@login_required
def list_posts(request):
	posts= Post.objects.all().order_by('-created')
	return render(request,'posts/feed.html',{'posts':posts})


class PostsFeedView(LoginRequiredMixin, ListView):
	"""Return all published posts"""
	template_name='posts/feed.html'
	model = Post
	ordering = ('-created')
	paginate_by=30 #X elementos de la paginacion
	context_object_name='posts' #nombre del query en el context

class PostDetailView(LoginRequiredMixin,DetailView):
	""" return post details"""

	template_name='posts/detail.html'
	queryset=Post.objects.all()
	context_object_name='post'


#def list_posts(request):
#	"""List existing posts"""
#	content = []
#	for post in posts:
#		content.append("""
#			<p><strong>{name}</strong></p>
#			<p><small>{user} - <i>{timestamp}</i></small></p>
#			<figure><img src="{picture}"/></figure>			
#			""".format(**post))
#	return HttpResponse('<br>'.join(content))


class CreatePostView(LoginRequiredMixin,CreateView):
	"""Create new post"""
	template_name='posts/new.html'
	form_class=PostForm
	success_url= reverse_lazy('posts:feed') #busca y evalua la url en este momento con reverse_lazy

	# agregamos otros datos al contexto: perfil y usuario
	def get_context_data(self, **kwargs):
		"""Add user and profile to context """
		context=super().get_context_data(**kwargs) #el contexto hubiera sido el contexto si no hubiera sobre-escrito la clase
		context['user']=self.request.user
		context['profile']=self.request.user.profile
		return context

#@login_required
#def create_post(request):
	"""create new post view"""
#	if request.method =='POST':
#		form = PostForm(request.POST, request.FILES) #tiene un formulario que le envia los datos
#		if form.is_valid():
#			form.save()
#			return redirect('posts:feed')
#	else:
#		form = PostForm()

#	return render(
#		request=request,
#		template_name = 'posts/new.html',
#		context = {
#			'user':request.user,
#			'profile':request.user.profile
#		}
#	)