from hash import subtree_hashes
from Ast import get_ast_root, print_tree_with_lexemes
from Jaccard import jaccard
from normalize import normalize_variables  # ✅ importar normalizador

def main(file1, file2):
    # === 1️⃣ Normalización ===
    with open(file1, "r", encoding="utf-8") as f1:
        code1 = f1.read()
    with open(file2, "r", encoding="utf-8") as f2:
        code2 = f2.read()

    code1_norm = normalize_variables(code1)
    code2_norm = normalize_variables(code2)

    print("\n🧩 === Etapa 1: NORMALIZACIÓN DE CÓDIGO ===")
    print(f"\n--- Código original ({file1}) ---\n{code1}")
    print(f"\n--- Código normalizado ({file1}) ---\n{code1_norm}")
    print("\n" + "="*80)
    print(f"\n--- Código original ({file2}) ---\n{code2}")
    print(f"\n--- Código normalizado ({file2}) ---\n{code2_norm}")
    print("\n" + "="*80)

    # Guardar temporalmente el código normalizado para Tree-sitter
    tmp1 = "tmp_norm1.cpp"
    tmp2 = "tmp_norm2.cpp"
    with open(tmp1, "w", encoding="utf-8") as f:
        f.write(code1_norm)
    with open(tmp2, "w", encoding="utf-8") as f:
        f.write(code2_norm)

    # === 2️⃣ Generación de AST ===
    root1, code_bytes1 = get_ast_root(tmp1)
    root2, code_bytes2 = get_ast_root(tmp2)

    print("\n🌳 === Etapa 2: ÁRBOLES SINTÁCTICOS (AST) ===")
    print(f"\n--- AST de {file1} ---\n")
    print_tree_with_lexemes(root1, code_bytes1)
    print("\n" + "="*80)
    print(f"\n--- AST de {file2} ---\n")
    print_tree_with_lexemes(root2, code_bytes2)
    print("\n" + "="*80)

    # === 3️⃣ Hashes de subárboles ===
    hashes1 = subtree_hashes(root1)
    hashes2 = subtree_hashes(root2)

    print("\n🔑 === Etapa 3: HASHES DE SUBÁRBOLES ===")
    print(f"\n--- Hashes de {file1} (total {len(hashes1)}) ---")
    for h in list(hashes1)[:10]:
        print("  ", h)
    if len(hashes1) > 10:
        print("  ...")

    print(f"\n--- Hashes de {file2} (total {len(hashes2)}) ---")
    for h in list(hashes2)[:10]:
        print("  ", h)
    if len(hashes2) > 10:
        print("  ...")
    print("\n" + "="*80)

    # === 4️⃣ Cálculo de similitud ===
    sim = jaccard(hashes1, hashes2)

    print("\n📊 === Etapa 4: COMPARACIÓN DE SIMILITUD ===")
    print(f"Archivo A: {file1}")
    print(f"Archivo B: {file2}")
    print(f"Subárboles A: {len(hashes1)}, B: {len(hashes2)}")
    print(f"Similitud estructural (Jaccard): {sim:.3f}")

    if sim >= 0.9:
        print("🚩 Muy alta similitud → probable plagio")
    elif sim >= 0.7:
        print("⚠️ Similitud considerable → revisar manualmente")
    else:
        print("✅ Baja similitud")

# === Ejecución principal ===
if __name__ == "__main__":
    archivo1 = "archivo1.txt"
    archivo2 = "archivo2.txt"
    main(archivo1, archivo2)

