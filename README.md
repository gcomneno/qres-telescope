# 📘 Quantum-Residue Telescope (QRT)

**Analizzatore di pattern modulari: isoforme, invarianti e “fantasmi numerici”.**  
Uno strumento per osservare i numeri attraverso lenti modulari multiple e rilevare strutture nascoste non visibili nel dominio naturale.

---

## 🔍 Cos’è

Il **Quantum-Residue Telescope (QRT)** è un prototipo di analisi matematica che:

- calcola lo *spettro residuo* di numeri su una lente modulare (insieme di moduli);
- rileva **isoforme**: numeri completamente diversi che diventano indistinguibili sotto una data lente;
- individua **invarianti nascosti** (“ghost energy”): quantità che rimangono costanti tra vettori di residui differenti;
- produce cluster, mappe, pattern e diagnosi utili per:
  - modellazione numerica,
  - test di hash non-criptografici,
  - analisi di generatori pseudo-casuali,
  - studio di sequenze numeriche e trasformazioni discrete.

È pensato come strumento da laboratorio: semplice, diretto, e matematicamente solido.

---

## 🧠 Concetti chiave

### Lente modulare

Un insieme di moduli:  
`M = {m₁, m₂, …, mₖ}`

Ogni numero \( n \) viene proiettato nello spazio dei residui:

\[
n \rightarrow (n \bmod m_1, n \bmod m_2, ..., n \bmod m_k)
\]

---

### Isoforme

Numeri diversi che hanno **lo stesso vettore residui** sotto la lente.  
Sono “ombre identiche” in uno spazio che non percepisce la differenza tra gli originali.

Esempio (M = {6, 8, 9}):

- 8, 80, 152, 224 hanno vettore residui **(2, 0, 8)** → stessa isoforma.

---

### Ghost Energy

Un invariante estratto dai residui che rimane costante per gruppi di numeri.  
La forma base usata dal prototipo è:

\[
E(n) = \sum_i (n \bmod m_i)
\]

Numeri diversi → residui diversi → **energia uguale**.  
Sono cluster più sottili rispetto alle isoforme.

---

## 📦 Installazione

### Clona il repository:
> git clone https://github.com/gcomneno/qres-telescope.git
> cd qres-telescope

### (Consigliato) Usa una venv:
> python3.13 -m venv .venv
> source .venv/bin/activate

### Installa il progetto in modalità editabile:
> python -m pip install --upgrade pip
> python -m pip install -e .

#### Richiede Python 3.9+ (testato anche con 3.13).

---

## 🚀 Usage / Examples

## 1️⃣ Isoforma Hunter – cluster di vettori identici
Cerca numeri con identico spettro residuo sotto una lente modulare.

Esempio: lente 
𝑀={6,8,9}

M={6,8,9} sull’intervallo [0, 200]:

> python -m qrt iso --start 0 --end 200 --mods 6 8 9 --min-cluster 2

#### Output tipico:
[ISO 1] vector=(0, 0, 0) size=3
   examples: 0, 72, 144

[ISO 5] vector=(4, 4, 4) size=3
   examples: 4, 76, 148

[ISO 9] vector=(2, 0, 8) size=3
   examples: 8, 80, 152

### Interpretazione:
vector=(4, 4, 4) identifica una isoforma: tutti i numeri del cluster
hanno lo stesso vettore residui (mod 6, 8, 9).

numeri lontani (es. 4, 76, 148) collassano nella stessa “ombra” modulare.

### Suggerimenti:
aumenta --end per vedere cluster più grandi:

> python -m qrt iso --start 0 --end 1000 --mods 6 8 9 --min-cluster 4

#### cambia la lente:
> python -m qrt iso --start 0 --end 300 --mods 5 7 11 --min-cluster 3

## 2️⃣ Ghost Energy Scanner – invarianti nascosti
Cerca gruppi di numeri che condividono la stessa energia modulare (somma dei residui), anche se i vettori sono diversi.

Esempio: lente 
𝑀={7,10,12}

M={7,10,12} sull’intervallo [0, 200]:

> python -m qrt ghost --start 0 --end 200 --mods 7 10 12 --min-cluster 3

### Output reale (estratto):
[GHOST 3] energy=12 size=15
   examples: 4, 16, 28, 41, 53, 65, 77, 90, 102, 114
   spectra: 4:(4, 4, 4), 16:(2, 6, 4), 28:(0, 8, 4), 41:(6, 1, 5), 53:(4, 3, 5), ...

[GHOST 1] energy=14 size=18
   examples: 7, 20, 32, 44, 48, 56, 81, 93, 97, 105
   spectra: 7:(0, 7, 7), 20:(6, 0, 8), 32:(4, 2, 8), 44:(2, 4, 8), ...

#### Interpretazione:
energy=12 significa che per tutti i numeri del cluster la somma dei residui
(mod 7, 10, 12) è 12, anche se i vettori sono diversi.

questo è un invariante modulare nascosto: un pattern che si conserva
mentre il dettaglio cambia.

### Suggerimenti:
alza --min-cluster per vedere solo invarianti “grossi”:

> python -m qrt ghost --start 0 --end 500 --mods 7 10 12 --min-cluster 10

### sperimenta con lenti miste:
> python -m qrt ghost --start 0 --end 300 --mods 6 9 14 --min-cluster 5

📁 Struttura del codice
src/qrt/
├─ core.py          # Lente e mappa residui
├─ isoforms.py      # Isoforma Hunter
├─ ghost_energy.py  # Ghost Energy Scanner
├─ viz_ascii.py     # Output leggibile
├─ cli.py           # Interfaccia CLI
└─ __main__.py      # Entry-point per `python -m qrt`

## 🛠 Roadmap
- Supporto invarianti lineari generici (coeff a ∈ [-2..2])
- Esportazione JSON/TSV dei cluster
- Heatmap modulari (opzionale, via matplotlib)
- Modalità “sequence mode” (input da file di numeri)
- Ricerca automatica della miglior lente per un dato range

## 📄 Licenza
Rilasciato sotto licenza MIT (vedi file LICENSE).
