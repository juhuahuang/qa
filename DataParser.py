# -*- coding: utf-8 -*-

import json


if __name__ == "__main__":
    answerable_qas = []
    not_answerable_qas = []

    with open(".\\SquadData\\train-v2.0.json", 'r', encoding='utf-8') as reader:
        rawData = json.load(reader)
        rawData = rawData['data']
        for data in rawData:
            title = data['title']
            paragraphs = data['paragraphs']
            for paragraph in paragraphs:
                context = paragraph['context']
                qas = paragraph['qas']
                for qa in qas:
                    question = qa['question']
                    if qa['is_impossible']:
                        not_answerable_qas.append((context, question))
                    else:
                        answers = [a['text'] for a in qa['answers']]
                        answerable_qas.append((context, question, answers))
        