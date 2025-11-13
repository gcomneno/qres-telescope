from __future__ import annotations

import argparse
from typing import List

from .core import Lens, SpectralMap
from .ghost_energy import find_sum_invariants
from .isoforms import find_isoforms
from .viz_ascii import print_ghosts, print_isoforms


def _parse_mods(mods: List[str]) -> List[int]:
    if not mods:
        raise ValueError("Devi specificare almeno un modulo con --mods.")
    try:
        return [int(m) for m in mods]
    except ValueError as exc:
        raise ValueError("Tutti i moduli devono essere interi.") from exc


def _build_spectral_map_from_args(args: argparse.Namespace) -> SpectralMap:
    moduli = _parse_mods(args.mods)
    lens = Lens(tuple(moduli))
    smap = SpectralMap(lens)
    smap.build_from_range(args.start, args.end)
    return smap


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="qrt",
        description="Quantum-Residue Telescope - Analizzatore di pattern modulari.",
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    def add_common_arguments(p: argparse.ArgumentParser) -> None:
        p.add_argument(
            "--start",
            type=int,
            required=True,
            help="Valore iniziale (incluso) del range.",
        )
        p.add_argument(
            "--end",
            type=int,
            required=True,
            help="Valore finale (incluso) del range.",
        )
        p.add_argument(
            "--mods",
            nargs="+",
            required=True,
            help="Lista di moduli (es. --mods 6 8 9).",
        )

    # subcomando iso
    iso_parser = subparsers.add_parser(
        "iso",
        help="Cerca isoforme: numeri con lo stesso vettore residui.",
    )
    add_common_arguments(iso_parser)
    iso_parser.add_argument(
        "--min-cluster",
        type=int,
        default=2,
        help="Dimensione minima del cluster (default: 2).",
    )

    # subcomando ghost
    ghost_parser = subparsers.add_parser(
        "ghost",
        help="Cerca cluster di ghost energy (somma dei residui costante).",
    )
    add_common_arguments(ghost_parser)
    ghost_parser.add_argument(
        "--min-cluster",
        type=int,
        default=3,
        help="Dimensione minima del cluster (default: 3).",
    )

    args = parser.parse_args(argv)

    smap = _build_spectral_map_from_args(args)

    if args.mode == "iso":
        clusters = find_isoforms(smap.mapping, min_size=args.min_cluster)
        print_isoforms(clusters)
    elif args.mode == "ghost":
        clusters = find_sum_invariants(smap.mapping, min_cluster=args.min_cluster)
        print_ghosts(clusters)
    else:
        parser.error(f"Modalità sconosciuta: {args.mode}")
