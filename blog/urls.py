from django.urls import path
from .views import PostFeedbackList,PostList, PostCreate, PostDetailView,PostUpdate,PostFeedback,PostDelete
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/new/', PostCreate.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/feedback/', PostFeedback.as_view(), name='feedback'),
    path('post/feedback/list/', PostFeedbackList.as_view(), name='feedbackList'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]
