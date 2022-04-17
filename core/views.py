from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist


from core.models import News, NewsCategory, SetupSettings, Wiki


def index(request):
    ss = SetupSettings.objects.all()[:9]
    wikis = Wiki.objects.all()[:3]
    news = News.objects.all()[:7]
    template_name = "index.html"
    context = {"ss": ss, "wikis": wikis, "news": news}
    return render(request, template_name, context)


def news(request):
    news = News.objects.all()
    template_name = "news_cat.html"
    paginator = Paginator(news, 12)

    page_num = request.GET.get("page")
    tags = paginator.get_page(page_num)
    context = {"news": news, "tags": tags}
    return render(request, template_name, context)


def news_filter(request, slug):
    tags = get_object_or_404(NewsCategory, slug=slug)
    news = News.objects.filter(tags=tags)
    paginator = Paginator(news, 12)

    page_num = request.GET.get("page")
    tags = paginator.get_page(page_num)
    template_name = "news_cat.html"
    context = {"news": news, "tags": tags}
    return render(request, template_name, context)


def setup(request):
    setups = SetupSettings.objects.all()
    paginator = Paginator(setups, 20)

    page_num = request.GET.get("page")
    players_cat = paginator.get_page(page_num)

    obj = "Streamers and Esports"
    template_name = "players_cat.html"
    context = {"players_cat": players_cat, "obj": obj}
    return render(request, template_name, context)


def setup_filter(request, slug, url_type):
    obj = get_object_or_404(Wiki, Q(slug=slug) & (Q(page_type=3) | Q(page_type=4)))
    url_type = obj.page_type
    players_cat = SetupSettings.objects.filter(Q(game=obj) | Q(team=obj)).distinct()[
        0:16
    ]
    paginator = Paginator(players_cat, 20)

    page_num = request.GET.get("page")
    players_cat = paginator.get_page(page_num)
    template_name = "players_cat.html"
    context = {"players_cat": players_cat, "obj": obj, "url_type": url_type}
    return render(request, template_name, context)


def setup_single(request, slug):
    obj = get_object_or_404(SetupSettings, slug=slug)
    if obj.game.title == "Counter-Strike: Global Offensive":  # type: ignore
        game = "CS:GO"
    else:
        game = obj.game.title  # type: ignore

    if obj.is_pro:
        teammates = SetupSettings.objects.filter(
            Q(team=obj.team) & Q(game=obj.game)
        ).exclude(title=obj.title)
    else:
        teammates = obj.related.all()  # type: ignore

    try:
        wiki = Wiki.objects.get(title=obj.title)
    except ObjectDoesNotExist:
        wiki = None

    template_name = "player_setup.html"
    context = {"obj": obj, "teammates": teammates, "game": game, "wiki": wiki}
    return render(request, template_name, context)
