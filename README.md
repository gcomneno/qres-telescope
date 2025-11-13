# 📘 Quantum-Residue Telescope (QRT)
**Analizzatore di pattern modulari: isoforme, invarianti e “fantasmi numerici”.**
Uno strumento per osservare i numeri attraverso lenti modulari multiple e rilevare strutture nascoste non visibili nel dominio naturale.

---

## 🔍 Cos’è
Il **Quantum-Residue Telescope (QRT)** è un prototipo di analisi matematica che:

* calcola lo *spettro residuo* di numeri su una lente modulare (insieme di moduli);
* rileva **isoforme**: numeri completamente diversi che diventano indistinguibili sotto una data lente;
* individua **invarianti nascosti** (“ghost energy”): quantità che rimangono costanti tra vettori di residui differenti;
* produce cluster, mappe, pattern e diagnosi utili per:
  - modellazione numerica,
  - test di hash non-criptografici,
  - analisi di generatori pseudo-casuali,
  - studio di sequenze numeriche e trasformazioni discreti.

È pensato come strumento da laboratorio: semplice, diretto, e matematicamente solido.

---

## 🧠 Concetti chiave

### **Lente modulare**
Un insieme di moduli:
`M = {m₁, m₂, …, mₖ}`

Ogni numero ( n ) viene proiettato nello spazio dei residui:
[
n \rightarrow (n \bmod m_1, n \bmod m_2, ..., n \bmod m_k)
]

---

### **Isoforme**
Numeri diversi che hanno **lo stesso vettore residui** sotto la lente.
Sono “ombre identiche” in uno spazio che non percepisce la differenza tra gli originali.

Esempio:

Con M = {6, 8, 9}
8, 80 e 152 hanno tutti il vettore **(2, 0, 8)**.

---

### **Ghost Energy**
Un invariante estratto dai residui che rimane costante per gruppi di numeri.
La forma base usata dal prototipo è:

[
E(n) = \sum_i (n \bmod m_i)
]

Numeri diversi → residui diversi → **energia uguale**.
Sono cluster più sottili rispetto alle isoforme.

---

## 📦 Installazione
Clona il repository:
```bash
git clone https://github.com/gcomneno/qres-telescope
cd qres-telescope
```

Esegui direttamente il modulo (non richiede dipendenze esterne):

```bash
python3 -m qrt --help
```

---

## 🚀 Quickstart

### 1️⃣ Isoforma Hunter
Trova numeri con **identico spettro residuo**.

```bash
python3 -m qrt iso --start 0 --end 200 --mods 6 8 9 --min-cluster 2
```

**Output tipico:**
```
[ISO 1] vector=(2, 0, 8) size=4
   examples: 8, 80, 152, 224

[ISO 2] vector=(4, 4, 4) size=3
   examples: 4, 76, 148
```

---

### 2️⃣ Ghost Energy Scanner
Raggruppa i numeri che hanno **stessa energia modulare** (somma dei residui).

```bash
python3 -m qrt ghost --start 0 --end 200 --mods 7 10 12 --min-cluster 3
```

**Output tipico:**
```
[GHOST 1] energy=12 size=4
   examples: 4, 16, 28, 41

[GHOST 2] energy=15 size=3
   examples: 9, 21, 33
```

---

## 🧪 Casi d’uso principali

### ✔ Analisi di sequenze numeriche
Cluster modulari di pattern ricorrenti, filtri, segnali “sterili”, isoforme attive.

### ✔ Valutazione di hash e permutazioni
Identificazione di collisioni strutturali, isotropia, zone “vuote” nello spettro.

### ✔ Test per PRNG e generatori custom
Risonanze modulari, ripetizioni, anomalie a basse frequenze.

### ✔ Esplorazione teorica
Studio di simmetrie residue, forme equivalenti, invarianti deboli o combinatori.

---

## 📁 Struttura del codice (prototipo)
```
src/qrt/
├─ core.py          # Lente e mappa residui
├─ isoforms.py      # Isoforma Hunter
├─ ghost_energy.py  # Ghost Energy Scanner
├─ viz_ascii.py     # Output leggibile
└─ cli.py           # Interfaccia CLI
```

---

## 🛠 Roadmap
* [ ] Supporto invarianti lineari generici (coeff a ∈ [-2..2])
* [ ] Esportazione JSON/TSV dei cluster
* [ ] Heatmap modulari (opzionale, via matplotlib)
* [ ] Modalità “sequence mode” (input da file)
* [ ] Ricerca automatica della miglior lente per un dato range

---

## 📄 Licenza
Rilasciato sotto licenza **MIT**.
