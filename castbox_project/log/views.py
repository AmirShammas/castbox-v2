from django.utils.decorators import method_decorator
from permissions.permissions import superuser_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Log


@method_decorator(superuser_required, name='dispatch')
class LogListView(LoginRequiredMixin, ListView):
    model = Log
    context_object_name = "log_list"
    template_name = "logs/log_list.html"
    login_url = "login"

    def get_queryset(self):
        return Log.objects.all()
