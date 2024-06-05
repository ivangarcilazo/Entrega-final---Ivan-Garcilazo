from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppKinda.forms import *
from AppKinda.models import *
from django.views.generic import TemplateView,ListView,DetailView
from AppAccount.models import *

class AboutMeView(TemplateView):
    template_name='AppKinda/about_me.html'
    
class IndexView(ListView):
    model=CarPosts
    template_name='AppKinda/index.html'
    context_object_name='posts'

class PostDetailView(DetailView):
    model=CarPosts
    template_name='AppKinda/post_detail.html'
    context_object_name='post'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['promoted_products'] = CarPosts.objects.order_by('?')[:5]
        context['comments'] = CommentPost.objects.filter(post=self.object)
        return context

def search_car(request):
    
    if request.GET['search_value']:
        search_value = request.GET['search_value']
        cars = CarPosts.objects.filter(title__icontains=search_value)
        
        return render(request, 'AppKinda/index.html', {'posts':cars}) 
    else:
        cars = CarPosts.objects.all()
    
    return render(request, 'AppKinda/index.html', {'posts':cars, 'message_search':'No se envío ningún valor'})


@login_required
def addComment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        post_id = request.POST.get('post_id')
        user = request.user
        
        if len(comment_text) > 10:
            post = CarPosts.objects.get(id=post_id)
            comment = CommentPost(user=user, comment=comment_text, post=post)
            comment.save()
            return redirect('detalle_publicacion', pk=post_id)
    
    return redirect('Inicio')

def custom_404(request, exception):
    return render(request, '404.html', status=404)    
        