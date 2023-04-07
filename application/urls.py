from . import views
# from application.views import category_list
from django.urls import path, include 
from .views import *
urlpatterns = [
    path('', views.review_table, ),
    path('review_table', views.review_table, ),
    
    # ==============
    path('api/category', CategoryList.as_view(), name='category-list'),
    path('api/category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('api/category/<int:category_id>/products/', CategoryProductList.as_view(), name='category-products'),
   
    # creates a new product in a specified category.
    # path('category/<int:category_id>/add', views.ProductCreateView.as_view(), name='product-create'),
    # ===============
    # Lists all products
    path('api/products/', views.ProductList.as_view()),
    # Retrieves details of a product
    path('api/products/<int:pk>/', views.ProductDetail.as_view()),
    # ===============
    # Lists all reviews of a product
    path('api/products/<int:product_id>/reviews/', ProductReviewList.as_view(), name='product-review-list'),
    #Retrieves the details of a single review
    path('api/reviews/<int:pk>/', ProductReviewDetail.as_view(), name='product-review-detail'),
    # ===============
    #Deletes all products in a category
    path('DELETE/api/category/<int:pk>/products/', CategoryProductsDeleteView.as_view(), name='category-products-delete'),
    # add keyword to category
    path('api/category/<int:category_id>/edit/', CategoryEditView.as_view(), name='category-edit'),
    
    # delete all keywords in a category
    path('api/category/<int:category_id>/delete_keywords/', views.CategoryDeleteKeywordsView.as_view(), name='category_delete_keywords'),

    # delete one keywords in a category
    # path('api/category/<int:category_id>/delete_one_keyword/', views.CategoryDeleteOneKeywordView.as_view())

# =========================
    # create a new setup
    path('api/setup/create/', SetupCreateView.as_view(), name='setup-create'),

    # create a new keywords and adjectives for a setup
    path('api/setup/<int:setup_id>/keyword/create/', KeywordCreateView.as_view(), name='keyword-create'),

    #List of setups
    path('api/setups/list/', SetupListView.as_view(), name='setup-list'),
    
    # Amazon Rating Average
    path('api/review_average_rating/', ReviewAverageRating.as_view(), name='review_average_rating'),

    # Amazon Total Review Count
    path('api/reviews/count/', ReviewCount.as_view(), name='review-count'),

    # List of Amazon Reviews
    path('api/reviews/', ReviewList.as_view(), name='review-list'),



]

