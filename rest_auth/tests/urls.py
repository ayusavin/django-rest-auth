from django.urls import include, path, re_path
from django.views.generic import TemplateView
from . import django_urls

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter

from rest_framework.decorators import api_view

from rest_auth.urls import urlpatterns
from rest_auth.registration.views import (
    SocialLoginView, SocialConnectView, SocialAccountListView,
    SocialAccountDisconnectView
)
from rest_auth.social_serializers import (
    TwitterLoginSerializer, TwitterConnectSerializer
)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    adapter_class = TwitterOAuthAdapter
    serializer_class = TwitterLoginSerializer


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class TwitterConnect(SocialConnectView):
    adapter_class = TwitterOAuthAdapter
    serializer_class = TwitterConnectSerializer


class TwitterLoginSerializerFoo(TwitterLoginSerializer):
    pass


@api_view(['POST'])
def twitter_login_view(request):
    serializer = TwitterLoginSerializerFoo(
        data={'access_token': '11223344', 'token_secret': '55667788'},
        context={'request': request}
    )
    serializer.is_valid(raise_exception=True)


class TwitterLoginNoAdapter(SocialLoginView):
    serializer_class = TwitterLoginSerializer


urlpatterns += [
    path('rest-registration/', include('rest_auth.registration.urls')),
    path('test-admin/', include(django_urls)),
    path('account-email-verification-sent/', TemplateView.as_view(),
        name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
    path('social-login/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('social-login/twitter/', TwitterLogin.as_view(), name='tw_login'),
    path('social-login/twitter-no-view/', twitter_login_view, name='tw_login_no_view'),
    path('social-login/twitter-no-adapter/', TwitterLoginNoAdapter.as_view(), name='tw_login_no_adapter'),
    path('social-login/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('social-login/twitter/connect/', TwitterConnect.as_view(), name='tw_connect'),
    path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    path('socialaccounts/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'),
    path('accounts/', include('allauth.socialaccount.urls'))
]
