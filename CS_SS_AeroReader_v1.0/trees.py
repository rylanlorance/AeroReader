def draw_minimax(tree, placements, i, maximizer, half):
    fill(255)
    
    center_x, center_y = placements[i]
    
    if maximizer:
        triangle(center_x - half,
                 center_y + half,
                 center_x + half,
                 center_y + half,
                 center_x,
                 center_y - half)
        
        fill(255, 0, 0)
        text(tree[i][1], center_x, center_y + half/2)
    
    else:
        triangle(center_x - half,
                 center_y - half,
                 center_x + half,
                 center_y - half,
                 center_x,
                 center_y + half)
        
        fill(255, 0, 0)
        text(tree[i][1], center_x, center_y - half/2)
    
    fill(0)
    text(tree[i][0], center_x, center_y)
    
    j = 2 * i + 1
    
    if j < len(tree) and tree[j][0] is not None:
        nx, ny = placements[j]
        
        line(center_x, center_y+15, nx, ny)
        draw_minimax(tree, placements, j, not maximizer, half) 
        
    j += 1
    if j < len(tree) and tree[j][0] is not None:
        nx, ny = placements[j]
        
        line(center_x, center_y+15, nx, ny)
        draw_minimax(tree, placements, j, not maximizer, half) 
    

def seven_tree(arr, maximizer, current, i):
    if current == 7:
        arr[i] = ('7', 1 * maximizer - 1 * (not maximizer)) # Store 1 if minimizer says 7, otherwise -1
        return
    
    seven_tree(arr, not maximizer, current + 1, 2 * i + 1)
    
    if current + 2 < 8:
        seven_tree(arr, not maximizer, current + 2, 2 * i + 2)
        
    left_score, right_score = arr[2 * i + 1][1], arr[2 * i + 2][1]
    
    if right_score == 0:
        arr[i] = (current, left_score) 
        return
    
    compare = max if maximizer else min
    
    arr[i] = (current, compare(left_score, right_score))
