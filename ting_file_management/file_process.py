import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    if file is None:
        return None

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(file_data)

    sys.stdout.write(str(file_data))


def remove(instance):

    if not instance:
        sys.stdout.write("Não há elementos\n")
        return None

    file = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n"
    )
    return file


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        sys.stderr.write("Posição inválida\n")
        return None

    sys.stdout.write(str(instance.search(position)))
