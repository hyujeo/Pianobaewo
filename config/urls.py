"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('resources/', resources),
    path('basic/', basic),
    path('cover/', cover),
    path('comp/', comp),

    path('chord-triad/', chord_triad),
    path('chord-seven/', chord_seven),
    path('chord-inversion/', chord_inversion),
    path('chord-more/', chord_more),
    path('tech-intro/', tech_intro),
    path('tech-scale/', tech_scale),
    path('tech-arpeggio/', tech_arpeggio),
    path('tech-tremolo/', tech_tremolo),
    path('ear-intro/', ear_intro),
    path('ear-key/', ear_key),
    path('ear-interval/', ear_interval),
    path('ear-chord/', ear_chord),
    path('root-left/', root_left),
    path('root-inversion/', root_inversion),
    path('root-alternate/', root_alternate),
    path('root-arpeggio/', root_arpeggio),
    path('left-arpeggio/', left_arpeggio),
    path('left-alternate/', left_alternate),
    path('left-bass/', left_bass),
    path('transcribe-key/', transcribe_key),
    path('transcribe-interval/', transcribe_interval),
    path('transcribe-chord/', transcribe_chord),
    path('melody-ornament/', melody_ornament),
    path('melody-3/', melody_3),
    path('melody-6/', melody_6),
    path('lh-bass/', lh_bass),
    path('lh-leap/', lh_leap),
    path('lh-arpeggio/', lh_arpeggio),
    path('three4-basic/', three4_basic),
    path('three4-waltz/', three4_waltz),
]
