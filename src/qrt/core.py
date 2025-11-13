from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Tuple

Vector = Tuple[int, ...]


@dataclass(frozen=True)
class Lens:
    """
    Rappresenta una lente modulare: un insieme di moduli positivi.

    Esempio:
        Lens((6, 8, 9))
    """

    moduli: Tuple[int, ...]

    def __post_init__(self) -> None:
        if not self.moduli:
            raise ValueError("Lens richiede almeno un modulo.")
        if any(m <= 0 for m in self.moduli):
            raise ValueError("Tutti i moduli devono essere interi positivi.")

    def spectrum_of(self, n: int) -> Vector:
        """Restituisce il vettore dei residui di n rispetto ai moduli della lente."""
        return tuple(n % m for m in self.moduli)


@dataclass
class SpectralMap:
    """
    Mappa numeri -> vettori di residui rispetto a una Lens.
    """

    lens: Lens
    mapping: Dict[int, Vector] = field(default_factory=dict)

    def build_from_range(self, start: int, end: int) -> None:
        """
        Costruisce la mappa per tutti i numeri nell'intervallo [start, end].
        Sovrascrive eventuali dati precedenti.
        """
        if end < start:
            raise ValueError("end deve essere >= start.")
        self.mapping.clear()
        for n in range(start, end + 1):
            self.mapping[n] = self.lens.spectrum_of(n)

    def build_from_sequence(self, seq: Iterable[int]) -> None:
        """
        Costruisce la mappa a partire da una sequenza arbitraria di numeri.
        """
        self.mapping.clear()
        for n in seq:
            nn = int(n)
            self.mapping[nn] = self.lens.spectrum_of(nn)
