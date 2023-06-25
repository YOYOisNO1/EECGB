    #!/usr/bin/env python3
    
    
def solve():
        tram_stop, igor_pos, igor_desired_point = map(int, input().split())
        tram_meter_by_seconds, igor_meter_by_seconds = map(int, input().split())
        tram_pos, tram_direction = map(int, input().split())
    
        distance = abs(igor_desired_point - igor_pos)
        igor_time_to_walk = distance * igor_meter_by_seconds
    
        tram_time_to_change_direction = tram_meter_by_seconds * (
            tram_stop - tram_pos if tram_direction > 0 else tram_pos)
    
        if distance == 0:
            return 0
    
        if igor_meter_by_seconds <= tram_meter_by_seconds:
            return igor_time_to_walk
    
        igor_direction = (igor_desired_point - igor_pos) // distance
    
        already_walked = 0
    
        if (tram_direction == igor_direction and
                (tram_pos - igor_pos) * (igor_desired_point - igor_pos) > 0):
            already_walked += tram_time_to_change_direction
            already_walked += tram_stop * tram_meter_by_seconds
            tram_pos = 0 if igor_direction > 0 else tram_stop
        elif (tram_direction != igor_direction):
            already_walked += tram_time_to_change_direction
            tram_pos = 0 if igor_direction > 0 else tram_stop
    
        igor_pos += igor_direction * (already_walked / igor_meter_by_seconds)
    
        if igor_time_to_walk <= already_walked:
            return igor_time_to_walk
    
        igor_time_to_walk -= already_walked
    
        # So now the tram is behind igor, it is faster than it,
        # and igor has not got to the place yet.
    
        tram_time_to_ride = abs(
            igor_desired_point - tram_pos) * tram_meter_by_seconds
    
        return already_walked + min(igor_time_to_walk, tram_time_to_ride)
    
    
    if __name__ == '__main__':
        print(solve())