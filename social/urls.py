from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView
from .views import AddDislike, AddLike, AddFollower, RemoveFollower, UserSearch, ListFollowers, AddCommentLike, AddCommentDislike, CommentReplyView
from .views import PostNotification, FollowNotification, RemoveNotification

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('profile/<int:pk>/followers', ListFollowers.as_view(), name='followers-list'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/reply/<int:pk>', CommentReplyView.as_view(), name='comment-reply'),
    path('notification/<int:notification_pk>/post/<int:object_pk>', PostNotification.as_view(), name='post-notification'),
    path('notification/<int:notification_pk>/follow/<int:object_pk>', FollowNotification.as_view(), name='follow-notification'),
    path('notification/delete/<int:notification_pk>', RemoveNotification.as_view(), name='notification-delete')


]