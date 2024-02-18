from django.shortcuts import render, redirect
from .models import Site
from .forms import SiteForm

def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'contacts/liste_sites.html', {'sites': sites})

def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()
    return render(request, 'contacts/ajouter_site.html', {'form': form})

def modifier_site(request, site_id):
    site = Site.objects.get(id=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm(instance=site)
    return render(request, 'contacts/modifier_site.html', {'form': form, 'site': site})

def supprimer_site(request, site_id):
    site = Site.objects.get(id=site_id)
    site.delete()
    return redirect('liste_sites')

def index(request):
    return render(request, 'contacts/index.html')

def connexion(request):
    return render(request, 'contacts/connexion.html')

def inscription(request):
    return render(request, 'contacts/inscription.html')


def contact(request):
    return render(request, 'contacts/contact.html')