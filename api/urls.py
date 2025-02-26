from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeesViewset, basename='employee')
# router.register('blogss', views.BlogsViewsSet, basename='blogss')
# router.register('comments',views.CommentViewsSet,basename='comments')

urlpatterns = [
    # path('students',views.studentsView),
    # path('students/<int:pk>',views.studentDetailsViews),
    # path('employee',views.EmployeesView.as_view()),
    # path('employee/<int:pk>',views.EmployeedetailsViews.as_view()),
    path('',include(router.urls)),
    # path('blogss',views.BlogsViewsSet.as_view()),
    # path('comments',views.CommentViewsSet.as_view()),
]
 