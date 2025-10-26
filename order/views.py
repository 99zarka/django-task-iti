from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderForm

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'
    login_url = '/accounts/login/' # Redirect to login page if not authenticated

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'
    login_url = '/accounts/login/'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')
    login_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Decrease product quantity after successful order
        product = form.instance.product
        product.quantity -= form.instance.product_quantity
        product.save()
        return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')
    login_url = '/accounts/login/'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def form_valid(self, form):
        # Logic to handle quantity change during update
        original_order = Order.objects.get(pk=self.object.pk)
        original_quantity = original_order.product_quantity
        new_quantity = form.instance.product_quantity
        product = form.instance.product

        if original_quantity != new_quantity:
            quantity_difference = new_quantity - original_quantity
            if product.quantity < quantity_difference:
                form.add_error('product_quantity', f"Only {product.quantity} units of {product.name} are available.")
                return self.form_invalid(form)
            product.quantity -= quantity_difference
            product.save()
        return super().form_valid(form)

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
    login_url = '/accounts/login/'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def form_valid(self, form):
        # Increase product quantity when an order is deleted
        order = self.get_object()
        product = order.product
        product.quantity += order.product_quantity
        product.save()
        return super().form_valid(form)
