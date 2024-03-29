pathlist = ["chord-triad", "chord-seven", "chord-inversion", "chord-more", 
            "tech-intro", "tech-scale", "tech-arpeggio", "tech-tremolo",
            "ear-intro", "ear-key", "ear-interval", "ear-chord",

            "root-left", "root-inversion", "root-alternate", "root-arpeggio",
            "left-arpeggio", "left-alternate", "left-bass",

            "transcribe-key", "transcribe-interval", "transcribe-chord",
            "melody-ornament", "melody-3", "melody-6",
            "lh-bass", "lh-leap", "lh-arpeggio",
]

print("\n\n\nURL\n")
for path in pathlist:
    upath = path.replace("-", "_")
    print("    path('"+path+"/', "+upath+"),")

print("\n\n\nVIEWS\n")
for path in pathlist:
    upath = path.replace("-", "_")
    print("def "+upath+"(request):\n    return render(request, '"+path+".html', context)")
    print()
