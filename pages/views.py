from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from .models import Page
from .forms import PageForm

# Se crea un mixin para implemntarlo en cada clase
# y hacer que se permitan gestiones mientras
# sea miembro del staff
# object es la clase base de todos los objetos python

class StaffRequiredMixin(object):
    
        
    # Eso que se hizo anteriormente se puede realizar mediante
    # un decorador, es decir, nos ayuda a disminuir el código
    @method_decorator(staff_member_required)

    def dispatch(self, request, *args, **kwargs):
        """if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))"""
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

# class PageCreate(StaffRequiredMixin, CreateView): Estructura con Mixin
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm

    """def get_success_url(self):
        return reverse('pages:pages')"""

    success_url = reverse_lazy('pages:pages')
    

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    
    template_name_suffix = '_update_form'
    
    # Si la idea es ver el mismo formulario con los datos actualizados
    # Se debe redefinir el método get_success y de ahí sí tomar el id_page

    def get_success_url(self):
        return reverse('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

    