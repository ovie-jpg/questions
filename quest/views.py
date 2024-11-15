from django.shortcuts import render, redirect
from .models import Survey, Response
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

def home(request):
    surveys = Survey.objects.all()
    if request.method == 'POST':
        name_surv = request.POST.get('name_field')
        if name_surv:
            for survey in surveys:
                answer = request.POST.get(f'answer_{survey.id}')
                if answer:
                    response = Response.objects.create(name=name_surv, survey=survey.question, answer=answer)
                    response.save()
            return redirect('complete')
    context = {
        'surveys': surveys
    }
    return render(request, 'home.html', context)

def complete(request):
    return render(request, 'complete.html')

def results(request):
    surveys = Survey.objects.all()
    survey_results = []

    for survey in surveys:
        result = {
            'survey': survey,
            'opt_a': Response.objects.filter(answer=survey.option_a).count(),
            'opt_b': Response.objects.filter(answer=survey.option_b).count(),
            'opt_c': Response.objects.filter(answer=survey.option_c).count() if survey.option_c else None,
            'opt_d': Response.objects.filter(answer=survey.option_d).count() if survey.option_d else None,
            'opt_e': Response.objects.filter(answer=survey.option_e).count() if survey.option_e else None,
        }
        survey_results.append(result)

    context = {
        'surveys': surveys,
        'survey_results': survey_results,
    }
    return render(request, 'result.html', context)

def del_results(request):
    results= Response.objects.all()
    if results:
        results.delete()
    return redirect('results')

def del_quests(request):
    quests= Survey.objects.all()
    if quests:
        quests.delete()
    return redirect('results')

class SurveyUpload(CreateView):
    model= Survey
    template_name= 'upload.html'
    fields= '__all__'

class SurveyUpdate(UpdateView):
    model= Survey
    template_name= 'survey_update.html'
    fields= '__all__'

class SurveyDelete(DeleteView):
    model= Survey
    template_name= 'survey_confirm_delete.html'
    success_url= reverse_lazy('home')