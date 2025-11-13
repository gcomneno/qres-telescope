from __future__ import annotations

from typing import List


def print_isoforms(clusters: List[dict], max_clusters: int = 10) -> None:
    """
    Stampa leggibile dei cluster di isoforme.
    """
    if not clusters:
        print("Nessuna isoforma trovata.")
        return

    for idx, c in enumerate(clusters[:max_clusters], start=1):
        vec = c["vector"]
        nums = c["numbers"]
        size = c["size"]
        print(f"[ISO {idx}] vector={vec} size={size}")
        preview = ", ".join(str(n) for n in nums[:10])
        print(f"   examples: {preview}")
        if len(nums) > 10:
            print(f"   ... (+{len(nums) - 10} altri)")
        print()


def print_ghosts(clusters: List[dict], max_clusters: int = 10) -> None:
    """
    Stampa leggibile dei cluster di ghost energy.
    """
    if not clusters:
        print("Nessun cluster di ghost energy trovato.")
        return

    for idx, c in enumerate(clusters[:max_clusters], start=1):
        energy = c["energy"]
        nums = c["numbers"]
        size = c["size"]
        print(f"[GHOST {idx}] energy={energy} size={size}")
        preview = ", ".join(str(n) for n in nums[:10])
        print(f"   examples: {preview}")

        examples = c.get("examples")
        if examples:
            ex_str = ", ".join(f"{n}:{vec}" for n, vec in examples)
            print(f"   spectra: {ex_str}")

        if len(nums) > 10:
            print(f"   ... (+{len(nums) - 10} altri)")
        print()
