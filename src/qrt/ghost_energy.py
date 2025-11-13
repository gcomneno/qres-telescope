from __future__ import annotations

from typing import Dict, List

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
