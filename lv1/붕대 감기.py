def solution(bandage, health, attacks):
    # 현재 체력을 담을 now 변수 선언
    now = health
    # 편의를 위해 dictionary 로 형변환
    dict_attacks = dict(attacks)
    
    cnt = 0
    # 1부터 마지막 공격시간까지 for 문 실행
    for i in range(1, attacks[-1][0] + 1):
        
        # attacks[i][0] 의 값들(keys)에 i 가 해당되는지 확인
        if(i in dict_attacks.keys()):
            # 해당된다면 공격 및 연속 회복 초기화
            now -= dict_attacks.get(i)
            cnt = 0
        else:
            # attacks 시간에 해당되지 않을 경우 heal
            if now < health:
                now += bandage[1]
                cnt += 1
            else: 
                # 실제 힐링이 필요하지 않은 경우에도 연속힐 적립
                cnt += 1
            
            # 연속힐 추가
            if cnt == bandage[0]:
                now += bandage[2]
                cnt = 0
            
            # health 보다 now 가 클 경우 health 로 덮어쓰기
            if now > health:
                now = health
        
        # 현재 체력이 0일 경우 -1 리턴
        if now <= 0:
            return -1 
                        
    return now