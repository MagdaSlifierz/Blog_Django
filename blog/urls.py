from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView,UpdatePostView, DeletePostView, AddCategoryView, CategoryViewPost, CategoryViewList, LikeView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'), 
    path('category/<str:cat>', CategoryViewPost, name='category_post'),
    path('category_list', CategoryViewList, name='category_list' ),
    path('like/<int:pk>', LikeView, name='like_post'),

]