from shapely.geometry import LineString, MultiLineString
import math

def point_line_distance(point, line_start, line_end):
    # Calculate the perpendicular distance from a point to a line
    x, y = point
    x1, y1 = line_start
    x2, y2 = line_end

    # Calculate the squared length of the line segment
    line_length_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2

    # Check if the line segment has zero length
    if line_length_sq == 0:
        return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

    # Calculate the absolute distance
    distance = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.sqrt(line_length_sq)

    return distance

def douglas_peucker(line, tolerance):
    #Check geometry type
    if isinstance(line, LineString):
         points = list(line.coords)
    elif isinstance(line, MultiLineString):
         points = [list(coords) for part in line for coords in part.coords]
    else:
        print(f"Unexpected geometry type: {type(line)}")
        raise ValueError("Input geometry must be LineString or MultiLineString")

    # Find the point with the maximum distance
    max_distance = 0
    max_distance_index = 0
    
    line_start = points[0]
    line_end = points[-1]
    
    for i in range(1, len(points) - 1):
        distance = point_line_distance(points[i], line_start, line_end)
        
        if distance > max_distance:
            max_distance = distance
            max_distance_index = i
    
    # Check if the maximum distance is greater than the tolerance
    if max_distance > tolerance:
        # Split the polyline at the point with the maximum distance
        left_part = douglas_peucker(points[:max_distance_index + 1], tolerance)
        right_part = douglas_peucker(points[max_distance_index:], tolerance)
        
        return left_part[:-1] + right_part
    else:
        return [line_start, line_end]
