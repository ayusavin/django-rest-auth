# Moved in Django 1.8 from django to tests/auth_tests/urls.py

from django.urls import path, re_path
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.urls import urlpatterns


# special urls for auth test cases
urlpatterns += [
    path('logout/custom_query/', views.logout, dict(redirect_field_name='follow')),
    path('logout/next_page/', views.logout, dict(next_page='/somewhere/')),
    path('logout/next_page/named/', views.logout, dict(next_page='password_reset')),
    path('password_reset_from_email/', views.password_reset, dict(from_email='staffmember@example.com')),
    path('password_reset/custom_redirect/', views.password_reset, dict(post_reset_redirect='/custom/')),
    path('password_reset/custom_redirect/named/', views.password_reset, dict(post_reset_redirect='password_reset')),
    path('password_reset/html_email_template/', views.password_reset,
        dict(html_email_template_name='registration/html_password_reset_email.html')),
    re_path(r'^reset/custom/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm,
        dict(post_reset_redirect='/custom/')),
    re_path(r'^reset/custom/named/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm,
        dict(post_reset_redirect='password_reset')),
    path('password_change/custom/', views.password_change, dict(post_change_redirect='/custom/')),
    path('password_change/custom/named/', views.password_change, dict(post_change_redirect='password_reset')),
    path('admin_password_reset/', views.password_reset, dict(is_admin_site=True)),
    path('login_required/', login_required(views.password_reset)),
    path('login_required_login_url/', login_required(views.password_reset, login_url='/somewhere/')),
]
