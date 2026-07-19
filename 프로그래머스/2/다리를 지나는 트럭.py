from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = list(reversed(truck_weights))

    bridge = deque()
    time = 1

    truck = truck_weights.pop()
    bridge.append((truck, time + bridge_length))
    weight -= truck
    truck_to_bridge = True

    while truck_weights:
        # 다리에 트럭이 진입할 수 있는지 확인
        if len(bridge) < bridge_length and weight >= truck_weights[-1]:
            if truck_to_bridge:
                time += 1

            # 현재 시간에 빠져나가는 트럭이 있는지 확인
            if bridge and bridge[0][1] == time:
                out_truck, _ = bridge.popleft()
                truck_to_bridge = False
                weight += out_truck

            truck = truck_weights.pop()
            bridge.append((truck, time + bridge_length))
            weight -= truck
            truck_to_bridge = True

        else:
            out_truck, time = bridge.popleft()
            truck_to_bridge = False
            weight += out_truck

    # 다리 위에 트럭이 남아 있다면 마지막 트럭이 다리를 빠져나오는 시간까지 계산
    if bridge:
        answer = bridge[-1][-1]

    return answer


bridge_length_input = 3
weight_input = 3
truck_weights_input = [2, 1, 1, 1, 1]

print(solution(bridge_length_input, weight_input, truck_weights_input))