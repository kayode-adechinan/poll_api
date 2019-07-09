from django.urls import path
from poll import views

app_name = 'poll'
urlpatterns = [
    path('polls/', views.PollList.as_view(), name='poll_list'),
    path('polls/<int:pk>/', views.PollDetail.as_view(), name='poll_detail'),

    path('choices/', views.ChoiceList.as_view(), name='choice_list'),
    path('choices/<int:pk>/', views.ChoiceDetail.as_view(), name='choice_detail'),

    path('votes/', views.VoteList.as_view(), name='vote_list'),
    path('votes/<int:pk>/', views.VoteDetail.as_view(), name='vote_detail'),

    path("users/", views.UserCreate.as_view(), name="user_create"),
    path("login/", views.LoginView.as_view(), name="login"),

]
