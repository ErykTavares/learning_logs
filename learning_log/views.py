from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def check_owner(request, topic):
    """Verifica se o usuario logado é o dono do assunto da pagina atual"""
    if topic.owner != request.user:
        raise Http404


def index(request):
    """pagina inicial"""
    return render(request, "learning_log\\index.html")

@login_required
def topics(request):
    """onde fica todos os topicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {"topics" : topics}
    return render(request, "learning_log\\topics.html", context)

@login_required
def topic(request, topic_id):
    """assunto especifico"""
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic" : topic, "entries": entries}
    return render(request, "learning_log\\topic.html", context)

@login_required
def new_topic(request):
    """criação de novos assuntos """
    if request.method != "POST": 
        # se nenhum dado for submetido criara um formulario em branco
        form = TopicForm()
    else:# se os dados forem subemetidos, processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
        return HttpResponseRedirect(reverse("learning_log:topics"))
    context = {"form":form}
    return render(request, "learning_log\\new_topic.html", context)

@login_required
def new_entry(request, topic_id):
    """criação de novas entrada"""
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)
    if request.method != "POST":
        #nenhum dado submetido, cria um formulario em branco
        form = EntryForm()
    else:
        #se os dados forem submetidos, processa os dados forem
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_log:topic", args=[topic_id]))
    context = {"topic": topic, "form": form}
    return render(request, "learning_log\\new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada ja existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_owner(request, topic)
    if request.method != "POST":
        #prenche o formulario com a entrada atual 
        form = EntryForm(instance= entry)
    else:#dados do post submetidos
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_log:topic", args=[topic.id]))
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_log\edit_entry.html", context)
