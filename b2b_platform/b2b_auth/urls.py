from django.urls import path

from .views import SignUpFormView, SignInFormView, SignOutView


app_name = 'b2b_auth'

urlpatterns = [

    path('sign-up', SignUpFormView.as_view(), name='sign_up'),
    path('sign-in', SignInFormView.as_view(), name='sign_in'),
    path('sign-out', SignOutView.as_view(), name='sign_out'),

]
