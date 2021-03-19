from django.urls import path
from rest_framework.routers import DefaultRouter

from demo.views import Demo1, Demo2, Demo3, Demo4, Demo5

router = DefaultRouter()
router.register('demo3', Demo3, basename="/")
router.register('demo4', Demo4, basename="/")
router.register('demo5', Demo5, basename="/")

urlpatterns = [
    path('demo1/', Demo1.as_view()),
    path('demo2/', Demo2.as_view()),
]

urlpatterns += router.urls
