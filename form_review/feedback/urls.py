from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedBackView.as_view()),
    path('done', views.done),
    path('<int:id_feedback>', views.update_feedback),
]