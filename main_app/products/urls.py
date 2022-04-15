from django.urls import path
from . import views

urlpatterns = [
    #user authentication
    path("", views.login_user, name="login_user"),
    path('logout/',views.logout_user, name="logout_user"),

    #products urls
    path("products/", views.products, name="products"),
    path("create_product/", views.createProduct, name="create_product"),
    path("update_product/<str:pk>", views.updateProduct, name="update_product"),
    path("delete_product/<str:pk>", views.deleteProduct, name="delete_product"),

    #nutrition urls
    path("nutritions/", views.NutritionsDashboardTemplateView.as_view(), name="nutritions"),
    path("create_nutrition/", views.createNutrition, name="create_nutrition"),
    path("update_nutrition/<str:pk>", views.updateNutrition, name="update_nutrition"),
    path("delete_nutrition/<str:pk>", views.deleteNutrition, name="delete_nutrition"),
]