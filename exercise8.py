def vokon_zählen(x):
    x_lower = x.lower()
    x_lower_list = list(x_lower)
    vokalen = "aeiou"
    
    v = [] # Hier speichern wir die Vokalen
    k = [] # Hier speichern wir alle Buchstaben
    
    for b in x_lower_list:
        # Hier prüfen wir ob b eine Buchstabe ist
        if b.isalpha():
            k.append(b)
        # Hier prüfen wir ob b eine Vokale ist
        if b in vokalen:
            v.append(b)
    
    return f"Im String '{x}' gibt es {len(v)} Vokalen und {len(k)-len(v)} Konsonanten."

print(vokon_zählen("Berlin I love you!"))
    
    
