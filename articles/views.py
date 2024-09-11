from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .form import Article_from, CommentForm
# Create your views here.

from .models import Article


def list_article(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def ajout_article(request):
    if request.method == "POST":
        Form = Article_from(request.POST, request.FILES)
        if Form.is_valid():
            article = Form.save(commit=False)  # On sauvegarde le formulaire
            article.user = request.user
            article.save()
            return redirect(reverse('list_articles'))
    else:
        Form = Article_from()
        context = {
            'Form': Form
        }

    return render(request, 'articles/ajout.html', context)


def modifier(request, id):
    # Récupérez l'objet Eleve à modifier
    articles = get_object_or_404(Article, id=id)
    M_Form = Article_from(request.POST, request.FILES, instance=articles)
    if request.method == 'POST':
        # Créez un formulaire pour la modification

        if M_Form.is_valid():
            M_Form.save()  # Sauvegardez les modifications
            print('Formulaire est validé')
            return redirect(list_article)
        else:
            print('Formulaire invalide')
    else:
        # Si la méthode HTTP est GET, affichez le formulaire de modification
        M_Form = Article_from(instance=articles)
    return render(request, 'articles/update.html', {"M_Form": M_Form})


def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    category = article.category
    article_en_relation = Article.objects.filter(category=category)[:5]
    return render(request, 'articles/detail.html', {'article': article, "aer": article_en_relation})

@login_required(login_url='/login/')
def delete_article(request, id):
    supprime = get_object_or_404(Article, pk=id)
    supprime.delete()

    return redirect(list_article)


@login_required(login_url='/login/')
def add_comment(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        Form = CommentForm(request.POST)
        if Form.is_valid():
            comment = Form.save(commit=False)
            comment.article = article
            comment.owner = request.user
            comment.save()
        else:
            context = {
                'article': article,
                'Form': Form
            }
            return render(request, 'articles/detail.html', context)
    return redirect('article_detail', article.id)

def category(request):
    if request.method == "POST":
        Form = Article_from(request.POST, request.FILES)
        if Form.is_valid():
            article = Form.save(commit=False)  # On sauvegarde le formulaire
            article.user = request.user
            article.save()
            return redirect(reverse('list_articles'))
    else:
        Form = Article_from()
        context = {
            'Form': Form
        }

    return render(request, 'articles/ajout.html', context)