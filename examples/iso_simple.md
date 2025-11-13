# Esempio semplice: Isoforma Hunter
Cerchiamo isoforme nell'intervallo [0, 200] con la lente M = {6, 8, 9}.

```bash
python3 -m qrt iso --start 0 --end 200 --mods 6 8 9 --min-cluster 2
````

#### Output tipico:
[ISO 1] vector=(2, 0, 8) size=4
   examples: 8, 80, 152, 224

[ISO 2] vector=(4, 4, 4) size=3
   examples: 4, 76, 148

#### Interpretazione:
Numeri molto diversi (8, 80, 152, 224) collassano nella stessa isoforma:
il loro vettore residui è identico sotto la lente (6, 8, 9).

---

# Esempio semplice: Ghost Energy Scanner
Cerchiamo cluster di ghost energy nell\'intervallo [0, 200] con la lente M = {7, 10, 12}.

```bash
python3 -m qrt ghost --start 0 --end 200 --mods 7 10 12 --min-cluster 3
````

#### Output tipico:
[GHOST 1] energy=12 size=4
   examples: 4, 16, 28, 41
   spectra: 4:(4, 4, 4), 16:(2, 6, 4), 28:(0, 8, 4), 41:(6, 1, 5)

#### Interpretazione:
I vettori residui sono diversi, ma la somma (energia) è sempre 12.
Questo è un esempio di invariante modulare nascosto (ghost energy).

---
