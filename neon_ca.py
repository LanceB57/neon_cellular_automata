from PIL import Image
from scipy.spatial import KDTree

def neighbors(x, y, grid):
    res = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 and x1 < len(grid) and 0 <= y1 and y1 < len(grid):
                res += grid[x1][y1]
    return res

def next_grid(grid, survive_vals, birth_vals):
    grid2 = [[0] * len(grid[0]) for i in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1 and neighbors(x, y, grid) in survive_vals:
                grid2[x][y] = 1
            elif grid[x][y] == 0 and neighbors(x, y, grid) in birth_vals:
                grid2[x][y] = 1
            else:
                grid2[x][y] = 0
    return grid2

def distance_grid(grid, radius):
    dists = [[radius] * len(grid[0]) for i in range(len(grid))]
    alive = []
    dead = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                alive.append( (x, y) )
                dists[x][y] = 0
            else:
                dead.append( (x, y) )
    
    tree = KDTree(alive)
    results = tree.query(dead)
    for i in range(len(dead)):
        x, y = dead[i]
        dists[x][y] = min(dists[x][y], results[0][i])
    return dists

def enlarge(grid, magnification):
    grid2 = [[0] * (magnification * len(grid[0])) for i in range(magnification * len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[x])):

            for dx in range(magnification):
                for dy in range(magnification):
                    grid2[magnification * x + dx][magnification * y + dy] = grid[x][y]
    return grid2

def neon_image(dists, radius, color, path):
    img = Image.new(mode='RGB', size=( len(dists[0]), len(dists) ))
    im = img.load()
    for x in range(len(dists)):
        for y in range(len(dists[x])):
            if dists[x][y] == 0:
                im[y, x] = (255, 255, 255)
            else:
                ratio = 1 - dists[x][y] / radius
                im[y, x] = (int(color[0] * ratio), int(color[1] * ratio), int(color[2] * ratio))
    img.save(path)

ITERATIONS = 128
SIDE_LEN = 257

grid = [[0] * SIDE_LEN for i in range(SIDE_LEN)]

grid[128][128] = 1

BIRTH_VALS = [1]
SURVIVE_VALS = [1, 2, 3]
COLOR = (2, 39, 247)
MAGNIFICATION = 4
RADIUS = 10

for i in range(ITERATIONS):
    dists = distance_grid(grid, RADIUS)
    enlarged_dists = enlarge(dists, MAGNIFICATION)
    neon_image(enlarged_dists, RADIUS, COLOR, "results/ca1/" + str(i) + ".jpg")
    grid = next_grid(grid, SURVIVE_VALS, BIRTH_VALS)
    if i % 10 == 0:
        print("Done with %dth iteration" % (i))