# script_importacao.py

import json
from .models import Curso, Disciplina, Projeto, AreaCientifica, Docente

def importar_curso(ficheiro_json):
    with open(ficheiro_json, 'r') as file:
        data = json.load(file)

    curso = Curso.objects.create(
        nome=data['nome'],
        apresentacao=data['apresentacao'],
        objetivos=data['objetivos'],
        competencias=data['competencias']
    )

    for disciplina_data in data['disciplinas']:
        area_cientifica, _ = AreaCientifica.objects.get_or_create(nome=disciplina_data['area_cientifica'])
        disciplina = Disciplina.objects.create(
            nome=disciplina_data['nome'],
            ano=disciplina_data['ano'],
            semestre=disciplina_data['semestre'],
            ects=disciplina_data['ects'],
            curricularIUnitReadableCode=disciplina_data['curricularIUnitReadableCode'],
            area_cientifica=area_cientifica
        )
        for docente_nome in disciplina_data['docentes']:
            docente, _ = Docente.objects.get_or_create(nome=docente_nome)
            disciplina.docentes.add(docente)

        projeto_data = disciplina_data.get('projeto', None)
        if projeto_data:
            projeto = Projeto.objects.create(
                descricao=projeto_data['descricao'],
                conceitos_aplicados=projeto_data['conceitos_aplicados'],
                tecnologias_utilizadas=projeto_data['tecnologias_utilizadas'],
                imagem=projeto_data['imagem'],
                video_link=projeto_data['video_link'],
                github_link=projeto_data['github_link'],
                disciplina=disciplina
            )

        curso.disciplinas.add(disciplina)

    return curso
