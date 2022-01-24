from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.reviews, name='reviews'),
#     path('product_review/', views.product_review, name='product_review'),
# ]

urlpatterns = [
    path('add_review/<int:product_id>/', views.add_review, name="add_review"),
    # path('', views.product_review, name='product_review'),
    # path('add/', views.add_reviews, name='add_reviews'),
    # path('update/<int:review_id>/',
    #      views.update_reviews, name='update_reviews'),
    # path('remove/<int:review_id>/',
    #      views.remove_review, name='remove_review'),
]