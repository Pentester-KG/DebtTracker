from django.urls import path

from . import views


urlpatterns = [
    path('api/debts/', views.DebtorsListView.as_view(), name='debt-list'),
    path('api/debts/<int:pk>/', views.DebtorDetailView.as_view(), name='debt-detail'),
    path('api/debts/create/', views.DebtCreateView.as_view(), name='debt-create'),
    path('api/debts/<int:pk>/update/', views.DebtUpdateView.as_view(), name='debt-update'),
    path('api/debts/<int:pk>/delete/', views.DebtDeleteView.as_view(), name='debt-delete'),

]
