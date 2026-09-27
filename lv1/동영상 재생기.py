from datetime import timedelta

# 동일 코드 반복을 줄이기 위해 메소드로 제작
def to_time(value):
    minute, second = map(int, value.split(":"))
    return timedelta(minutes=minute, seconds=second)

def solution(video_len, pos, op_start, op_end, commands):
    # 편하게 비교할 수 있도록 필요한 변수들을 형변환
    start_time = to_time("00:00")
    ten_seconds = to_time("00:10")
    len_time = to_time(video_len)
    pos_time = to_time(pos)
    op_start_time = to_time(op_start)
    op_end_time = to_time(op_end)
    
    for command in commands:
        # 오프닝 자동 건너뛰기
        if(op_start_time <= pos_time < op_end_time):
            pos_time = op_end_time
        
        if command == "next":
            if len_time - pos_time < ten_seconds:
                pos_time = len_time
            else:
                pos_time += timedelta(seconds=10)
        else:
            if pos_time - start_time < ten_seconds:
                pos_time = start_time
            else:
                pos_time -= timedelta(seconds=10)
        
    # 마지막 command 실행 후 체크
    if(op_start_time <= pos_time < op_end_time):
        pos_time = op_end_time
            
    # timedelta는 "0.00:00" 과 같은 형태로 리턴되어 형식에 맞게 수정
    result_arr = str(pos_time).split(":")
    return f"{result_arr[1]}:{result_arr[2]}"
