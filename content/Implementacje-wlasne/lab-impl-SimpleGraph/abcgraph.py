# Python 3.12+

from abc import ABC, abstractmethod
from typing import Hashable, Iterable, Tuple

class BaseGraph(ABC):
    """
    Abstrakcyjna klasa bazowa reprezentująca graf.
    Zapewnia podstawowy interfejs, który powinien być
    zaimplementowany w klasach pochodnych w zależności od typu grafu.
    """

    def __init__(self, allow_loops: bool = False, allow_multiple_edges: bool = False, is_directed: bool = False) -> None:
        """
        :param allow_loops: Czy graf może zawierać pętle (krawędzie z wierzchołka do samego siebie)? Domyślnie False.
        :param allow_multiple_edges: Czy graf może być multigrafem (wiele krawędzi między tymi samymi wierzchołkami)? Domyślnie False.
        """
        self._allow_loops = allow_loops
        self._allow_multiple_edges = allow_multiple_edges
        self._is_directed = is_directed

    @property
    def allow_loops(self) -> bool:
        return self._allow_loops

    @property
    def allow_multiple_edges(self) -> bool:
        return self._allow_multiple_edges

    @property
    def is_directed(self) -> bool:
        return self._is_directed

    @abstractmethod
    def add_node(self, node: Hashable) -> None:
        """
        Dodaje wierzchołek do grafu.
        :param node: Unikalny identyfikator wierzchołka (np. liczba, string itp.),
                     pod warunkiem, że jest "hashowalny" (Hashable).
        """
        pass

    @abstractmethod
    def add_edge(self, u: Hashable, v: Hashable, weight: float|None = None) -> None:
        """
        Dodaje krawędź do grafu (ważoną lub nieważoną).
        :param u: Wierzchołek źródłowy
        :param v: Wierzchołek docelowy
        :param weight: Waga krawędzi (None lub konkretna liczba)
        """
        pass

    @abstractmethod
    def remove_node(self, node: Hashable) -> None:
        """
        Usuwa wierzchołek z grafu (oraz wszystkie jego powiązane krawędzie).
        :param node: Identyfikator wierzchołka do usunięcia
        """
        pass

    @abstractmethod
    def remove_edge(self, u: Hashable, v: Hashable) -> None:
        """
        Usuwa krawędź między dwoma wierzchołkami.
        Może wymagać dodatkowych parametrów w przypadku multigrafów
        (np. identyfikatora krawędzi) lub grafów ważonych
        (usuwanie krawędzi tylko o określonej wadze).
        """
        pass

    @abstractmethod
    def has_node(self, node: Hashable) -> bool:
        """
        Sprawdza, czy dany wierzchołek należy do grafu.
        :param node: Identyfikator wierzchołka
        :return: True lub False
        """
        pass

    @abstractmethod
    def has_edge(self, u: Hashable, v: Hashable) -> bool:
        """
        Sprawdza, czy między wierzchołkami u i v istnieje krawędź.
        :return: True lub False
        """
        pass

    @abstractmethod
    def neighbors(self, node: Hashable) -> Iterable[Hashable]:
        """
        Zwraca obiekt iterowalny z sąsiadami danego wierzchołka.
        Dla grafu skierowanego mogą to być wierzchołki, do których
        można dojść krawędzią wychodzącą z node (lub przyjąć inną konwencję).
        Dla grafu nieskierowanego powinny to być wszystkie wierzchołki
        połączone z node, niezależnie od kierunku.
        Zwracany obiekt iterowalny nie powinien zawierać duplikatów,
        a kolejność sąsiadów nie jest gwarantowana.
        """
        pass

    
    @property
    @abstractmethod
    def nodes(self) -> Iterable[Hashable]:
        """
        Zwraca obiekt iterowalny zawierający wszystkie wierzchołki w grafie.
        Kolejność zwracanych wierzchołków nie jest gwarantowana.
        Obiekt iterowalny nie powinien umożliwiać modyfikacji struktury grafu.
        """
        pass

    
    @property
    @abstractmethod
    def edges(self) -> Iterable[Tuple[Hashable, Hashable, float|None]]:
        """
        Zwraca obiekt iterowalny zawierający wszystkie krawędzie w grafie.
        Każda krawędź może być reprezentowana np. jako krotka (u, v, waga).
        Obiekt iterowalny powinien być niemutowalny, aby nie pozwalać na
        modyfikację struktury grafu przez zwrócony obiekt.
        """
        pass

    def __contains__(self, node: Hashable) -> bool:
        """
        Umożliwia składnię: `if node in graph: ...`
        """
        return self.has_node(node)
