from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedBackView.as_view()),
    path('done', views.DoneView.as_view()),
    path('update/<int:pk>', views.FeedbackUpdateView.as_view()),
    path('list', views.AllFeedbacksView.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view()),
]