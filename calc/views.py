from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "calc/home.html")


def support(request):
    return render(request, "calc/support.html")


def calculate(request):

    try:
        weight = int(request.GET.get('weight'))
        reps = int(request.GET.get('reps'))
        system = request.GET.get('kg_or_lbs')

        answer = {
            "Max by Eppley formula: ": round((weight * reps) / 30 + weight, 1),
            "Max by Brzycki formula: ": round(weight * (36/(37 - reps)), 1),
            "Max by Lander formula: ": round((100*weight)/(101.3 - 2.67123 * reps), 1),
            "Max by Conner formula: ": round(weight * (1 + 0.025*reps), 1)
        }

        context = {
            "answer": answer,
            "system": system,
            "result": True,
            "error": False
        }
        return render(request, "calc/home.html", context=context)
    except:
        context = {
            "result": False,
            "error": True
        }
        return render(request, "calc/home.html", context=context)
