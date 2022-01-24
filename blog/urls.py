from django.urls import path
from .views import PostFeedbackList,PostList, PostCreate, PostDetailView,PostUpdate,PostFeedback
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/new/', PostCreate.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/feedback/', views.PostFeedback, name='feedback'),
    path('post/feedback/list', views.PostFeedbackList.as_view(), name='feedbackList'),

]
