from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        first_num = queue.popleft() # 1
        cnt = 0
        for q in queue: # 2,3,2,3
            cnt += 1 # �ϴ� ���� ī��Ʈ�� ����
            if first_num > q: # [2,3,2,3]�� 1�� �񱳵�
                break # ���� ���������� ���̻� for���� �� �ʿ䰡 ����
        answer.append(cnt)
    return answer