from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import GameForm

from .models import Game

class IndexView(LoginRequiredMixin, generic.ListView):
    model=Game
    template_name = 'games/index.html'
    context_object_name = 'name'
    paginate_by = 10
    

    def get_queryset(self):
        """Return the last five published questions."""
        return Game.objects.order_by('name')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Game
    template_name = 'games/detail.html'

    
def game_form(request):
    #if form is submitted
    if request.method == 'POST':
        #will handle the request later
        return render(request, 'games/index.html')
        pass
    else:
        #creating a new form
        form = GameForm()

    #returning form 
    return render(request, 'games/create.html', {'form':form})
    