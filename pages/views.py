from django.shortcuts import render

context = {"root": "http://hyunhoj84.pythonanywhere.com/"}
#context = {"root": "http://127.0.0.1:8000/"}

# Create your views here.
def home(request):
    return render(request, "home.html", context )

def about(request):
    return render(request, "about.html", context)

def resources(request):
    return render(request, "resources.html", context)

def basic(request):
    return render(request, "basic-index.html", context)

def cover(request):
    return render(request, "cover-index.html", context)

def comp(request): 
    return render(request, "comp-index.html", context)

def chord_triad(request):
    return render(request, 'chord-triad.html', context)

def chord_seven(request):
    return render(request, 'chord-seven.html', context)

def chord_inversion(request):
    return render(request, 'chord-inversion.html', context)

def chord_more(request):
    return render(request, 'chord-more.html', context)

def tech_intro(request):
    return render(request, 'tech-intro.html', context)

def tech_scale(request):
    return render(request, 'tech-scale.html', context)

def tech_arpeggio(request):
    return render(request, 'tech-arpeggio.html', context)

def tech_tremolo(request):
    return render(request, 'tech-tremolo.html', context)

def ear_intro(request):
    return render(request, 'ear-intro.html', context)

def ear_key(request):
    return render(request, 'ear-key.html', context)

def ear_interval(request):
    return render(request, 'ear-interval.html', context)

def ear_chord(request):
    return render(request, 'ear-chord.html', context)

def root_left(request):
    return render(request, 'root-left.html', context)

def root_inversion(request):
    return render(request, 'root-inversion.html', context)

def root_alternate(request):
    return render(request, 'root-alternate.html', context)

def root_arpeggio(request):
    return render(request, 'root-arpeggio.html', context)

def left_arpeggio(request):
    return render(request, 'left-arpeggio.html', context)

def left_alternate(request):
    return render(request, 'left-alternate.html', context)

def left_basstranscribe_key(request):
    return render(request, 'left-basstranscribe-key.html', context)

def transcribe_interval(request):
    return render(request, 'transcribe-interval.html', context)

def transcribe_chord(request):
    return render(request, 'transcribe-chord.html', context)

def melody_ornament(request):
    return render(request, 'melody-ornament.html', context)

def melody_3(request):
    return render(request, 'melody-3.html', context)

def melody_6(request):
    return render(request, 'melody-6.html', context)

def lh_bass(request):
    return render(request, 'lh-bass.html', context)

def lh_leap(request):
    return render(request, 'lh-leap.html', context)

def lh_arpeggio(request):
    return render(request, 'lh-arpeggio.html', context)

def three4_basic(request):
    return render(request, 'three4-basic.html', context)

def three4_waltz(request):
    return render(request, 'three4-waltz.html', context)
