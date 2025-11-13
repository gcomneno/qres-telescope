from __future__ import annotations

from typing import Dict, List

from .core import Vector


def find_isoforms(
    spectral_map: Dict[int, Vector],
    min_size: int = 2,
) -> List[dict]:
    """
    Trova cluster di numeri che condividono lo stesso vettore residui.

    Args:
        spectral_map: dizionario n -> vettore residui.
        min_size: dimensione minima del cluster (almeno 2).

    Returns:
        Lista di cluster, ciascuno con:
        {
            "vector": (..),
            "numbers": [..],
            "size": int,
        }
    """
    if min_size < 2:
        min_size = 2

    buckets: Dict[Vector, List[int]] = {}

    for n, vec in spectral_map.items():
        buckets.setdefault(vec, []).append(n)

    clusters: List[dict] = []
    for vec, nums in buckets.items():
        if len(nums) >= min_size:
            nums_sorted = sorted(nums)
            clusters.append(
                {
                    "vector": vec,
                    "numbers": nums_sorted,
                    "size": len(nums_sorted),
                }
            )

    clusters.sort(key=lambda c: c["size"], reverse=True)
    return clusters
