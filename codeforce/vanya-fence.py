NUMBER_OF_FRIENDS, FENCE_HEIGHT = map(int, input().split())
PERSON_HEIGHTS_ARRAY = list(map(int, input().split()))
MIN_ROAD_WIDTH = 0
for i in range(NUMBER_OF_FRIENDS):
    if (PERSON_HEIGHTS_ARRAY[i] > FENCE_HEIGHT):
        MIN_ROAD_WIDTH = MIN_ROAD_WIDTH+2
    else:
        MIN_ROAD_WIDTH = MIN_ROAD_WIDTH+1
print(MIN_ROAD_WIDTH)
