from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login_user"),
    path('logout/',views.logout_user, name="logout_user"),

    #products urls
    path("products/", views.UserDashboardTemplateView.as_view(), name="products"),
    path("create_product/", views.createProduct, name="create_product"),
    path("update_product/<str:pk>", views.updateProduct, name="update_product"),
    path("delete_product/<str:pk>", views.deleteProduct, name="delete_product"),

    path("nutrition/", views.nutrition, name="nutrition"),
]