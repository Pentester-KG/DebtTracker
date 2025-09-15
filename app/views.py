from django.shortcuts import get_object_or_404
from django.views import generic
from . models import Debt


class DebtorsListView(generic.ListView):
    template_name = "debts/list.html"
    context_object_name = "debtors"
    model =Debt

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class DebtorDetailView(generic.DetailView):
    template_name = "debts/detail.html"
    context_object_name = "debtor"
    model = Debt

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs.get("pk"))


class DebtCreateView(generic.CreateView):
    template_name = "debts/create.html"
    model = Debt
    fields = ['debtor_name', 'amount', 'description']
    success_url = "/api/debts/"


class DebtUpdateView(generic.UpdateView):
    template_name = "debts/update.html"
    model = Debt
    fields = ['debtor_name', 'amount', 'description']
    success_url = "/"


class DebtDeleteView(generic.DeleteView):
    template_name = "debts/delete.html"
    model = Debt
    success_url = "/"



