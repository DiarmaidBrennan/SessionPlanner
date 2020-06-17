from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


from .models import SportsSession

"""

@todo:	add permissions to sessionplanner
@todo:	filter on own sessions
@todo:  paginate session planner

"""

class IndexView(LoginRequiredMixin, generic.ListView):
    model = SportsSession
    template_name = 'sessionplanner/index.html'
    context_object_name = 'training_session'
    paginate_by = 10

    def get_queryset(self):
        """Return the last five published questions."""
        return SportsSession.objects.filter(owner=self.request.user)

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = SportsSession
    context_object_name = 'detail'
    template_name = 'sessionplanner/detail.html'
    
    
    def get_sections(self):
        return render (self.sections.all())