def solution(mats, park):
    # 가장 큰 돗자리부터 확인하기 위해 내림차순 정렬
    mats.sort(reverse=True)
    
    row = len(park)
    columns = len(park[0])
    
    # 각 위치를 오른쪽 아래 꼭짓점으로 하는
    # 가장 큰 정사각형의 한 변 길이를 저장할 DP 배열
    enable = [[0] * columns for _ in range(row)]
    
    for y in range(row):
        for x in range(columns):
            if park[y][x] == '-1':
                # 위, 왼쪽, 왼쪽 위 대각선 중 가장 작은 값에 1을 더함
                # 현재 위치까지 이어지는 가장 큰 정사각형의 크기를 구함
                enable[y][x] = min(
                    enable[y-1][x],
                    enable[y-1][x-1],
                    enable[y][x-1]
                ) + 1
    
    # 전체 공원에서 만들 수 있는 가장 큰 정사각형의 크기
    # 각 행의 최댓값을 구한 뒤, 그중 가장 큰 값을 구함
    enable_length = max(map(max, enable))
    
    # 가장 큰 돗자리부터 확인하여 설치 가능한 첫 번째 돗자리를 반환
    for mat in mats:
        # 공원에서 만들 수 있는 정사각형보다 크면 설치할 수 없음
        if mat > enable_length:
            continue
        
        return mat
    
    # 설치할 수 있는 돗자리가 없는 경우
    return -1