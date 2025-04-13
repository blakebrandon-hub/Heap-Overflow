from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, QuestionForm, AnswerForm
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Question, Answer, Tag

def index(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'heap/index.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question).select_related('author')

    if request.method == 'POST':
        body = request.POST.get('answer_body')
        if body:
            Answer.objects.create(question=question, body=body, author=request.user)
            return redirect('question_detail', pk=pk)  # Correct URL name here
        # Redirect or render logic if needed

    return render(request, 'heap/question_detail.html', {'question': question, 'answers': answers})

def questions_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    questions = Question.objects.filter(tags=tag)
    return render(request, 'heap/questions_by_tag.html', {'tag': tag, 'questions': questions})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            form.save_m2m()  # Save the many-to-many data for tags
            return redirect('question_detail', pk=question.pk)  # Correct URL name here
        else:
            print('Failed to post')
    else:
        form = QuestionForm()

    # Pass all tags to the template for selection
    tags = Tag.objects.all()
    return render(request, 'heap/ask_question.html', {'form': form, 'tags': tags})

@login_required
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user  # Assuming you want to save the current user as the author of the answer
            answer.save()
            print('Form Saved')
            return redirect('question_detail', pk=pk)  # Correct URL name here
        else:
            print('Form Not Valid', form.errors)
    else:
        form = AnswerForm()
    
    return render(request, 'heap/question_detail.html', {'question': question, 'form': form})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'heap/tag_list.html', {'tags': tags})

def users(request):
	return HttpResponse("<h1>Hello World</h1>")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('index') 
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def delete_question(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, id=question_id)
        if question.author == request.user:
            question.delete()
            return redirect('index')  # Redirect to the desired page after deletion
    return redirect('question_detail', question_id=question.id)  # Redirect if unauthorized
