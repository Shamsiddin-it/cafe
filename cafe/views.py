from django.views.generic import ListView, TemplateView, CreateView, DeleteView, DetailView, UpdateView
from .models import Category, Dish, Staf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout ,authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

class HomeView(TemplateView):
    template_name = "home.html"



class DishCreateView(PermissionRequiredMixin, CreateView):
    model = Dish
    template_name = "dish_create.html"
    fields = ['image', 'name', 'description', 'category', 'weight', 'price']
    success_url = reverse_lazy('dish_list')
    permission_required = 'cafe.add_dish'
    permission_denied_message = "You dont have permission"


class DishListView(ListView):
    model = Dish
    template_name = "dish_list.html"
    context_object_name = 'dishes'

    
    
class DishDetailView(DetailView):
    model = Dish
    template_name = "dish_detail.html"
    context_object_name = 'dish'

class DishUpdateView(PermissionRequiredMixin, UpdateView):
    model = Dish
    template_name = "dish_update.html"
    fields = ['image', 'name', 'description', 'category', 'weight', 'price']
    success_url = reverse_lazy('dish_list')
    permission_required = 'cafe.change_dish'
    permission_denied_message = 'you dont have permission'

class DishDeleteView(PermissionRequiredMixin, DeleteView):
    model = Dish
    template_name = "dish_delete.html"
    success_url = reverse_lazy('menu')
    permission_required = 'cafe.del_dish'
    permission_denied_message = 'you dont have permission'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish_category"] = Dish.objects.filter(category = self.kwargs['pk'])
        return context

class MenuView(ListView):
    model = Category
    template_name = "menu.html"
    context_object_name = 'categorys'



