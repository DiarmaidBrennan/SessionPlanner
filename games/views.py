from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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

