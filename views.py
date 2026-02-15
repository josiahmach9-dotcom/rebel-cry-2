from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Article, Devotional


class HomePageView(TemplateView):
    template_name = "index.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Rebel Cry Ministries"
        context["year"] = 2026
        return context
    
class ApologeticsPageView(TemplateView):
    template_name = "apologetics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Apologetics - Rebel Cry Ministries"
        context["year"] = 2026

        # Read querystring and produce `results` for the template
        query = self.request.GET.get("q", "").strip()
        results = Article.objects.all()
        if query:
            results = results.filter(content__icontains=query)
            if not results.exists():
                results = Article.objects.filter(title__icontains=query)

        context["results"] = results
        context["query"] = query
        return context
    
    
class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Us - Rebel Cry Ministries"
        context["year"] = 2026
        return context


class DevotionalPageView(TemplateView):
    template_name = "devotional.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Devotional - Rebel Cry Ministries"
        context["year"] = 2026
        
        # Get all devotionals for display
        devotionals = Devotional.objects.all().order_by('-published_at')
        context["devotionals"] = devotionals
        
        return context

    
class PrivacyPolicyPageVeiw(TemplateView):
    template_name = "policy.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Privacy Policy - Rebel Cry Ministries"
        context["year"] = 2026
        return context
