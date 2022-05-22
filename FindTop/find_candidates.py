import copy
import json


def find_top_20(candidates: list, len_candidates: int = 20) -> list:
    """ Функция принимает на вход список поступающих.
    И необходимое количество возвращаемых кандидатов.
    возвращает список с  именами 20 человек, набравших наибольшее
    СУММАРНОЕ количество баллов (с учетом extra баллов)"""
    final_candidates = []
    len_candidates = len_candidates
    sort_fields = ['total_scores', 'computer_science', 'math']
    copy_candidates = copy.deepcopy(candidates)
    for item in copy_candidates:
        item['total_scores'] = sum([x for x in item['scores'].values()]) + item['extra_scores']
        item_copy = {**item['scores']}
        item.update(item_copy)
        del item['scores']
    copy_candidates = sorted(copy_candidates, key=lambda x: (x['total_scores'], x['computer_science'], x['math']), reverse=True)

    def add_candidates(candidates, key_selection, len_candidates, count=0):
        count = count
        final_candidates = []
        len_candidates = len_candidates
        last_total_scores = int
        identic_candidates = []
        for item in candidates:
            if len(final_candidates) < len_candidates:
                if last_total_scores != item[key_selection] and (not identic_candidates):
                    identic_candidates.append(item)
                elif last_total_scores == item[key_selection]:
                    identic_candidates.append(item)
                elif last_total_scores != item[key_selection] and (identic_candidates):
                    length_difference = len_candidates - len(final_candidates)
                    if len(identic_candidates) <= length_difference:
                        final_candidates.extend(identic_candidates)
                        identic_candidates = []
                        identic_candidates.append(item)
                    elif (len(identic_candidates) > length_difference) and length_difference and identic_candidates:
                        try:
                            final_candidates.extend(add_candidates(identic_candidates, key_selection=sort_fields[count], len_candidates=length_difference, count=count + 1))
                        except IndexError:
                            final_candidates.extend(identic_candidates)
                            print('количество кандидатов с одинаковыми баллами превышает допустимое количество кандидатов')
            last_total_scores = item[key_selection]

        length_difference = len_candidates - len(final_candidates)
        if len(identic_candidates) <= length_difference:
            final_candidates.extend(identic_candidates)
        elif (len(identic_candidates) > length_difference) and length_difference and identic_candidates:
            try:
                final_candidates.extend(add_candidates(identic_candidates, key_selection=sort_fields[count], len_candidates=length_difference, count=count + 1))
            except IndexError:
                final_candidates.extend(identic_candidates)
                print('количество кандидатов с одинаковыми баллами превышает допустимое количество кандидатов')

        return final_candidates if final_candidates else identic_candidates

    final_candidates = add_candidates(copy_candidates, key_selection=sort_fields[0], len_candidates=len_candidates, count=1)
    final_candidates = [(item['name']) for item in final_candidates]
    return final_candidates


if __name__ == '__main__':
    with open('FindTop/candidates.json', 'r') as f:
        candidates = json.load(f)
    final_candidates = find_top_20(candidates, len_candidates=20)
