from django.shortcuts import redirect, get_object_or_404, render

# Create your views here.
from .models import Team
from students.forms import StudentForm
from students.models import Student

def team_list(request):
	teams = Team.objects.all()

	return render(request, "teams/team_list.html", {
		"teams":teams
	})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
           student = form.save(commit=False)
           student.team = team
           student.save()

           return redirect("team_detail", team_id=team.id)

    else:
        form = StudentForm()

    return render(request, 'teams/team_detail.html', {
	"team": team,
	"form": form,
    })

def student_edit(request, team_id, student_id):
    team = get_object_or_404(Team, id=team_id)

    student = get_object_or_404(
        Student,
        id=student_id,
        team=team
    )

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            return redirect(
                "team_detail",
                team_id=team.id
            )

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "teams/student_edit.html",
        {
            "team": team,
            "student": student,
            "form": form,
        }
    )

def student_delete(request, team_id, student_id):
    team = get_object_or_404(Team, id=team_id)
   
    student = get_object_or_404(
        Student,
        id=student_id,
        team=team
    )

    if request.method == "POST":
       student.delete()

       return redirect(
           "team_detail",
           team_id=team.id
       )

    return render(
        request,
        "teams/student_delete.html",
       {
            "team":team,
            "student":student,
       }
    )
def student_add(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.team = team
            student.save()

            return redirect(
                "team_detail",
                team_id=team.id
            )

    else:
        form = StudentForm()

    return render(
        request,
        "teams/student_add.html",
        {
            "team": team,
            "form": form,
        }
    )