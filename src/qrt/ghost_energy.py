from __future__ import annotations

from functools import reduce
from itertools import product
from math import gcd
from typing import Dict, List, Tuple

from .core import Vector


def energy_sum(vec: Vector) -> int:
    """
    Energia base: somma dei componenti del vettore residui.
    """
    return sum(vec)


def find_sum_invariants(
    spectral_map: Dict[int, Vector],
    min_cluster: int = 3,
) -> List[dict]:
    """
    Raggruppa i numeri per energia E = somma(residui) e restituisce i cluster.

    Args:
        spectral_map: dizionario n -> vettore residui.
        min_cluster: dimensione minima del cluster (>=2).

    Returns:
        Lista di cluster, ciascuno con:
        {
            "energy": int,
            "numbers": [..],
            "size": int,
            "examples": [(n, vec), ...]  # fino a 10 esempi
        }
    """
    if min_cluster < 2:
        min_cluster = 2

    buckets: Dict[int, List[int]] = {}
    vectors: Dict[int, Vector] = {}

    for n, vec in spectral_map.items():
        e = energy_sum(vec)
        buckets.setdefault(e, []).append(n)
        vectors[n] = vec

    clusters: List[dict] = []
    for energy, nums in buckets.items():
        if len(nums) >= min_cluster:
            nums_sorted = sorted(nums)
            clusters.append(
                {
                    "energy": energy,
                    "numbers": nums_sorted,
                    "size": len(nums_sorted),
                    "examples": [(n, vectors[n]) for n in nums_sorted[:10]],
                }
            )

    clusters.sort(key=lambda c: c["size"], reverse=True)
    return clusters


# ===========================
#  Invarianti lineari
# ===========================

CoeffVector = Tuple[int, ...]


def _normalize_coeffs(coeffs: CoeffVector) -> CoeffVector:
    """
    Normalizza un vettore di coefficienti per evitare duplicati banali.

    - divide per il MCD dei coefficienti (se > 1)
    - forza il primo coefficiente non nullo a essere positivo
    """
    # Se sono tutti zero, non ha senso
    if all(c == 0 for c in coeffs):
        return coeffs

    # Riduzione per il MCD
    non_zero = [abs(c) for c in coeffs if c != 0]
    g = reduce(gcd, non_zero) if non_zero else 1
    if g > 1:
        coeffs = tuple(c // g for c in coeffs)

    # Forza il primo coeff non nullo ad essere positivo
    for c in coeffs:
        if c < 0:
            coeffs = tuple(-x for x in coeffs)
            break
        if c > 0:
            break

    return coeffs


def _linear_energy(vec: Vector, coeffs: CoeffVector) -> int:
    """Calcola L(vec) = a1*r1 + ... + ak*rk."""
    return sum(a * r for a, r in zip(coeffs, vec))


def search_linear_invariants(
    spectral_map: Dict[int, Vector],
    max_coeff: int = 2,
    min_cluster: int = 5,
) -> List[dict]:
    """
    Cerca invarianti lineari della forma:

        L(vec) = a1*r1 + ... + ak*rk = costante

    dove ai ∈ [-max_coeff .. max_coeff], non tutti zero, normalizzati
    per evitare duplicati banali (scalamenti e segni).

    Args:
        spectral_map: dizionario n -> vettore residui.
        max_coeff: valore massimo in modulo dei coefficienti (>=1).
        min_cluster: dimensione minima del cluster per considerare
                     interessante un invariante.

    Returns:
        Lista di cluster di invarianti lineari, ciascuno del tipo:
        {
            "coeffs": (a1, ..., ak),
            "value": v,
            "numbers": [...],
            "size": int,
            "examples": [(n, vec), ...]
        }
    """
    if not spectral_map:
        return []

    if max_coeff < 1:
        max_coeff = 1

    if min_cluster < 2:
        min_cluster = 2

    # Recupera dimensione del vettore
    sample_vec = next(iter(spectral_map.values()))
    dim = len(sample_vec)

    # Per evitare esplosioni combinatorie: se i moduli sono tantissimi,
    # la ricerca diventa pesante. Mettiamo un limite soft.
    if dim > 6:
        raise ValueError(
            f"Ricerca lineare su dimensione={dim} non supportata (troppi moduli)."
        )

    # Prepara le vector list per iterazioni più veloci
    items = list(spectral_map.items())  # [(n, vec), ...]

    coeff_range = range(-max_coeff, max_coeff + 1)
    seen_coeffs: set[CoeffVector] = set()
    results: List[dict] = []

    # Genera tutte le combinazioni di coefficienti
    for raw_coeffs in product(coeff_range, repeat=dim):
        # Salta il vettore nullo
        if all(c == 0 for c in raw_coeffs):
            continue

        norm = _normalize_coeffs(tuple(raw_coeffs))
        # Se coefficiente già considerato (equivalente), salta
        if norm in seen_coeffs:
            continue
        seen_coeffs.add(norm)

        # Raggruppa per valore L(vec)
        buckets: Dict[int, List[int]] = {}
        vectors: Dict[int, Vector] = {}
        for n, vec in items:
            val = _linear_energy(vec, norm)
            buckets.setdefault(val, []).append(n)
            vectors[n] = vec

        # Estrai solo i gruppi "interessanti"
        for value, nums in buckets.items():
            if len(nums) >= min_cluster:
                nums_sorted = sorted(nums)
                results.append(
                    {
                        "coeffs": norm,
                        "value": value,
                        "numbers": nums_sorted,
                        "size": len(nums_sorted),
                        "examples": [(n, vectors[n]) for n in nums_sorted[:10]],
                    }
                )

    # Ordina tutti gli invarianti trovati per dimensione del cluster
    results.sort(key=lambda c: c["size"], reverse=True)
    return results
