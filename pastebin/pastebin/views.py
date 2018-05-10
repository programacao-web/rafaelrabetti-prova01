from django.shortcuts import render, get_object_or_404
from .models import Paste
from .forms import PasteForm


def index(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = PasteForm()
    ctx = {'form': form}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    paste = get_object_or_404(Paste , pk=id)
    ctx = {"paste": paste}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    pastes = Paste.objects.filter(language=language)
    ctx = {'pastes': [pastes]}
    return render(request, 'pastebin/paste-language.jinja2', ctx)