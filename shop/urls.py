from django.urls import path
from shop.views import (
    ProductListView,
    ProductDetailView,
    Order,
    contact,
    by_rubric,
    about,
    SearchResultView,
    ServiceWorkerView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact', contact, name='contact'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('rubrics/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('about/', about, name='about'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('sw.js',
        ServiceWorkerView.as_view(),
        name=ServiceWorkerView.name,
    ),
]