from django.urls import path
from .views import  * #Posts
from rest_framework.routers import DefaultRouter

app_name = "blog_api"

urlpatterns = [
    path("post/<str:pk>/", PostDetail.as_view(), name="detailpost"),
    path("search/", PostListDetailFilter.as_view(), name="search"),
    path("", PostList.as_view(), name="listpost"),

    path("admin/create/", CreatePost.as_view(), name="createpost"),
    path("admin/edit/postdetail/<int:pk>/", AdminPostDetail.as_view(), name="admindetailpost"),
    path("admin/edit/<int:pk>/", EditPost.as_view(), name="editpost"),
]

# router = DefaultRouter()
# router.register("", Posts, basename="post")

# urlpatterns = router.urls