from django.shortcuts import render

def index(request):
    return render(request, 'quiz/index.html', {})


def ans(request, offset):
    if request.method == 'POST':
        project = Project.objects.get(title=offset)
        answer1 = request.POST.get('answer1', '')
        answer2 = request.POST.get('answer2', '')
        answer3 = request.POST.get('answer3', '')
        answer4 = request.POST.get('answer4', '')
        answer5 = request.POST.get('answer5', '')
        answer6 = request.POST.get('answer6', '')
        answer7 = request.POST.get('answer7', '')
        answer8 = request.POST.get('answer8', '')
        answer9 = request.POST.get('answer9', '')
        answer10 = request.POST.get('answer10', '')
        obj = Cost(answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, answer6=answer6, answer7=answer7, answer8=answer8, answer9=answer9, answer10=answer10)
        obj.save()
        return HttpResponseRedirect('/')