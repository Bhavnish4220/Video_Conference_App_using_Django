from django.urls import path
from . import views
from .views import save_session_duration
from django.conf import settings
from django.conf.urls.static import static
from .views import downloadFile
urlpatterns = [
    path('save-session-duration/', save_session_duration, name='save_session_duration'),
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.join_room, name='join_room'),
    path('file/',views.file_sharing, name='file_sharing'),
    path('<str:id>/',views.downloadFile, name='downloadFile'),
    # path('attendance/', views.attendance_view, name='attendance_view'),
    # path('attendance/',views.attendance_report_view, name='attendance_report'),
    
    path('',views.index, name='index'),

]