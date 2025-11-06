# Jaccard.py
# Contiene la función para calcular la similitud Jaccard entre conjuntos.

def jaccard(a: set, b: set) -> float:
    """Calcula la similitud Jaccard entre dos conjuntos."""
    return len(a & b) / len(a | b) if (a | b) else 1.0

if __name__ == "__main__":
    # Ejemplo de uso
    set1 = {'a', 'b', 'c', 'd'}
    set2 = {'a', 'b', 'e', 'f'}
    sim = jaccard(set1, set2)
    print(f"Similitud Jaccard entre {set1} y {set2}: {sim:.3f}")

