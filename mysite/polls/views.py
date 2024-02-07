from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone

from .forms import QuestionForm, ResponseForm
from .models import Question

def home(request):
    polls = Question.objects.all()
    context = {'polls': polls}
    return render(request, 'home.html', context)


def poll_detail(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    responses = poll.responses.order_by('-pub_date') 
    form = ResponseForm()
    return render(request, 'poll-detail.html', {'poll': poll, 'responses': responses, 'form': form})


def create_poll(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuestionForm()
    return render(request, 'create-poll.html', {'form': form})


def remove_poll(request):
    polls = Question.objects.all()
    context = {'polls': polls}
    return render(request, 'remove-poll.html', context)

def removePoll(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    poll.delete()
    polls = Question.objects.all()
    context = {'polls': polls}
    return render(request, 'remove-poll.html', context)

@require_POST
def add_reply(request, poll_id):
    form = ResponseForm(request.POST)
    if form.is_valid():
        new_response = form.save(commit=False)
        new_response.question_id = poll_id
        new_response.pub_date = timezone.now()  # set publication date to now
        new_response.save()
        return JsonResponse({'success': True, 'response_text': new_response.response_text, 'pub_date': new_response.pub_date.strftime("%B %d, %Y")})
    else:
        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

def search_results(request):
    query = request.GET.get('query', '')
    if query:
        questions = Question.objects.filter(question_text__icontains=query)
    else:
        questions = Question.objects.all()
    return render(request, 'search-results.html', {'questions': questions})
