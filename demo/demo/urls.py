from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('signup/', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    path('email-verification/',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    path('login/', TemplateView.as_view(template_name="login.html"),
        name='login'),
    path('logout/', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    path('password-reset/',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    path('password-reset/confirm/',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    path('user-details/',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    path('password-change/',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),


    # this url is used to generate email content
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    re_path(r'^admin/', admin.site.urls),
    path('accounts/profile/', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    path('docs/', get_swagger_view(title='API Docs'), name='api_docs')
]
