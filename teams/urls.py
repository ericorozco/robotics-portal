from django.urls import path
from . import views

urlpatterns = [
    path("", views.team_list, name="team_list"),
    path("<int:team_id>/", views.team_detail, name="team_detail"),
    path("<int:team_id>/student/add/", views.student_add, name="student_add"),
    path(
        "<int:team_id>/student/<int:student_id>/edit/",
        views.student_edit,
        name="student_edit",
    ),
    path(
        "<int:team_id>/student/<int:student_id>/delete/",
        views.student_delete,
        name="student_delete",
    ),
]