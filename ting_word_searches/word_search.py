def exists_word(word, instance):
    files = []

    for file in instance._data:
        name = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        occurrences = [
            {"linha": line + 1}
            for line, line_content in enumerate(lines)
            if word.lower() in line_content.lower()
        ]

        if occurrences:
            files.append(
                {
                    "palavra": word,
                    "arquivo": name,
                    "ocorrencias": occurrences,
                }
            )

    return files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
