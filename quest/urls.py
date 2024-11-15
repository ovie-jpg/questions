from django.urls import path
from . import views


urlpatterns= [
    path('', views.home, name= "home"),
    path('complete/', views.complete, name= "complete"),
    path('results/', views.results, name= "results"),
    path('del-results/', views.del_results, name= "del-results"),
    path('upload/', views.SurveyUpload.as_view(), name= "upload"),
    path('update-quest/<int:pk>', views.SurveyUpdate.as_view(), name= "update-quest"),
    path('delete-quest/<int:pk>', views.SurveyDelete.as_view(), name= "delete-quest"),
    path('del-quests/', views.del_quests, name= "del-quests")
]