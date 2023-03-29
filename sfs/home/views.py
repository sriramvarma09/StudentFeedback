from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "home/home.html")


def cse_1(request):
    return render(request, "home/cse/cse_1.html")


def cse_2(request):
    return render(request, "home/cse/cse_2.html")


def cse_3(request):
    return render(request, "home/cse/cse_3.html")


def cse_4(request):
    return render(request, "home/cse/cse_4.html")


def csit_1(request):
    return render(request, "home/csit/csit_1.html")


def csit_2(request):
    return render(request, "home/csit/csit_2.html")


def csit_3(request):
    return render(request, "home/csit/csit_3.html")


def csit_4(request):
    return render(request, "home/csit/csit_4.html")


def csse_1(request):
    return render(request, "home/csse/csse_1.html")


def csse_2(request):
    return render(request, "home/csse/csse_2.html")


def csse_3(request):
    return render(request, "home/csse/csse_3.html")


def csse_4(request):
    return render(request, "home/csse/csse_4.html")


def ece_1(request):
    return render(request, "home/ece/ece_1.html")


def ece_2(request):
    return render(request, "home/ece/ece_2.html")


def ece_3(request):
    return render(request, "home/ece/ece_3.html")


def ece_4(request):
    return render(request, "home/ece/ece_4.html")


def eee_1(request):
    return render(request, "home/eee/eee_1.html")


def eee_2(request):
    return render(request, "home/eee/eee_2.html")


def eee_3(request):
    return render(request, "home/eee/eee_3.html")


def eee_4(request):
    return render(request, "home/eee/eee_4.html")


def mech_1(request):
    return render(request, "home/mech/mech_1.html")


def mech_2(request):
    return render(request, "home/mech/mech_2.html")


def mech_3(request):
    return render(request, "home/mech/mech_3.html")


def mech_4(request):
    return render(request, "home/mech/mech_4.html")


def subject_1(request):
    return render(request, "subjects/subject_1.html")


def subject_2(request):
    return render(request, "subjects/subject_2.html")


def subject_3(request):
    return render(request, "subjects/subject_3.html")


def subject_4(request):
    return render(request, "subjects/subject_4.html")


def subject_5(request):
    return render(request, "subjects/subject_5.html")


def thanku(request):
    return render(request, "subjects/tnq.html")


def details(request):
    q1 = request.POST["agreement1"]
    q2 = request.POST["agreement2"]
    q3 = request.POST["agreement3"]
    q4 = request.POST["agreement4"]
    q5 = request.POST["agreement5"]
    q6 = request.POST["agreement6"]
    q7 = request.POST["agreement7"]
    q8 = request.POST["agreement8"]
    q9 = request.POST["agreement9"]
    q10 = request.POST["agreement10"]
    q11 = request.POST["agreement11"]
    dic = {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "q4": q4,
    }
    return render(request, "null.html", dic)
