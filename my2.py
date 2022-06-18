from functools import cmp_to_key
import itertools

n = int(input("Введите число ваакансий:  "))
vacancies = [input("Введите название вакансии и количество мест через запятую:  ").split(',') for _ in range(n)]

k = int(input("Введите число участников:  "))
candidates = [input("Введите имя кандидата, название вакакнсии, количество решенных задач и количество штрафных баллов через запятую:  ").split(',') for _ in range(k)]

def candidates_by_vacancy(vac):
    all_candidates_by_vacancy = [cand for cand in candidates if cand[1] == vac[0]]
    if len(all_candidates_by_vacancy)<= int(vac[1]):
        return [cand[0] for cand in all_candidates_by_vacancy]

    all_candidates_by_vacancy = sorted(all_candidates_by_vacancy, key=lambda point: (-int(point[2]), int(point[3])))
    all_candidates_by_vacancy = [cand[0] for cand in all_candidates_by_vacancy]
    return all_candidates_by_vacancy[:int(vac[1]):]



matrix_vacancies_candidates = [  candidates_by_vacancy(i) for i in vacancies]

res = list( itertools.chain(*matrix_vacancies_candidates))

print(*res, sep='\n')


