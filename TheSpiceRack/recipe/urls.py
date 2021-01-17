from django.urls import path

from . import views
urlpatterns = [
    path('<int:recipe_id>/', views.view_recipe, name='recipe_view'),
    path('add/', views.add_recipe, name='recipe_add'),
    path('submit/', views.submit_recipe, name='recipe_submit'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='recipe_edit'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='recipe_delete'),
    path('save/<int:recipe_id>/', views.save_recipe, name='recipe_save'),
]