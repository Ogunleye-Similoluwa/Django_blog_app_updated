from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, PostCreateView, PostListView, PostDelete, PostUpdate, Register
from django.urls import path

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('post/', PostCreateView.as_view(), name="create"),
    path('list/', PostListView.as_view(), name="list"),
    path('update/<int:pk>', PostUpdate.as_view(), name="update"),
    path('delete/<int:pk>', PostDelete.as_view(), name="delete"),
    path('signup/', Register.as_view(), name="signup")
]
