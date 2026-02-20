from django.urls import path
from . import views

urlpatterns = [
    path("documents", views.documents, name="documents"),
    path("mood-selection", views.mood_selection, name="mood-selection"),
    path("general-correction", views.general_correction, name="quick-correction"),
    path('detailed-correction', views.detailed_correction, name="detailed_editing"),
    path( "api/general-correction/", views.general_correction_endpoint, name="general-correction-endpoint"),
    path("api/save-document/", views.save_document_endpoint, name="save-db"),
    path("api/detailed-correction/", views.detailed_correction_endpoint, name="detailed-correction-endpoint"),
    path("api/save-detailed-document/", views.save_detailed_document_endpoint, name="save-detailed-document"),

]