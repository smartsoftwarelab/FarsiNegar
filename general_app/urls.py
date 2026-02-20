from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("about-us", views.about_us, name="about-us"),
    path("contact-us", views.contact_us, name="contact-us"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("sign-in", views.sign_in, name="sign-in"),
    path("refine-text-endpoint/", views.refine_text_endpoint, name="refine-text-endpoint"),
]