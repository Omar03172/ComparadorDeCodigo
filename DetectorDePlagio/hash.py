import hashlib

import hashlib

def subtree_signature(node) -> str:
    """Crea una representación de texto de cada subárbol (orden-independiente)."""
    parts = [node.type]
    child_sigs = [subtree_signature(child) for child in node.children]
    child_sigs.sort()  # 🔹 ordena los subárboles
    parts.extend(child_sigs)
    return "(" + ",".join(parts) + ")"

def subtree_hashes(node) -> set:
    """Devuelve un conjunto de hashes MD5 insensibles al orden de los hijos."""
    sig = subtree_signature(node)
    h = hashlib.md5(sig.encode("utf-8")).hexdigest()
    hashes = {h}
    for child in node.children:
        hashes |= subtree_hashes(child)
    return hashes

if __name__ == "__main__":
    from Ast import get_ast_root

    file_path = "archivo1.txt"
    root, _ = get_ast_root(file_path)
    hashes = subtree_hashes(root)

    print(f"Subárboles únicos en {file_path}: {len(hashes)}")
    for h in hashes:
        print(h)