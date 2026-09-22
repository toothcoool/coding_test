"""
    채점 결과

    정확성: 58.3
    효율성: 41.7
    합계: 100.0 / 100.0

    1. collection.Counter를 사용하여 participant와 completion의 요소 별 개수를 구하고 서로 빼서 남은 요소를 반환합니다.
    {
    "stanko": 1,
    "ana": 1,
    "mislav": 1
    }
    
    2. 남은 요소의 키를 리스트로 변환 후 문자열로 합쳐서 반환합니다.
"""

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return "".join(list(answer.keys()))