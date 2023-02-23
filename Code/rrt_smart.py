import pygame
import random
from math import sqrt

# For Node Class
def dist(a,b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


# Set the dimensions of the screen
W = 800
H = 600

# Define the class for the nodes of the tree
class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parentIs = None
        self.cost = 0


def RRT_star(start, goal, obstacles):
    nodes = [start]
    iteration = 5000 # No. of iterations
    stride = 0.1 # value of jump towards random point
    bias = 5

    for i in range(iteration):
        if random.randint(1,10) < bias:
            # Generate the Random Point
            r_x = random.randint(0,W)
            r_y = random.randint(0,H)
            rand_node = Node(r_x, r_y)
        else:
            r_x = goal.x
            r_y = goal.y
            rand_node = Node(r_x, r_y)
        

        # Find Closest Node
        closest_node = start # By default
        for node in nodes:
            if dist(rand_node, node) < dist(rand_node, closest_node):
                # print(dist(rand_node, node), dist(rand_node, closest_node))
                closest_node = node
        
        # Move Toward the random point
        new_x = closest_node.x + stride*(r_x - closest_node.x)
        new_y = closest_node.y + stride*(r_y - closest_node.y)
        new_node = Node(new_x, new_y)
        new_node.parentIs = closest_node

        # Check if it collides with an obstacle
        collision =  False
        for obstacle in obstacles:
            if sqrt((new_node.x - obstacle[0]) ** 2 + (new_node.y - obstacle[1]) ** 2) < obstacle[2]:
                collision = True
                break
            
        if collision == False:
            nodes.append(new_node)
        else:
            continue

        # Check if goal is reached
        if dist(new_node,goal) < 10:
            goal.parentIs = new_node
            nodes.append(goal)
            print(len(nodes))
            return nodes
        
    # If no path is found in this iteration
    print("Goal Not reached in this Iteration")
    print(len(nodes))
    return nodes
    

def main():
    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # Define Start and Goal Location
    start = Node(10,10)
    goal = Node(700,500)

    # Define Obstacle Location and their radius
    obstacles = [(300, 300, 50), (200, 100, 85), (550, 470, 75)]

    path = RRT_star(start, goal, obstacles)
    print(len(path))

    # create a list of nodes till goal from the path
    if path is not None:
        path_node = []
        node = path[-1] # take last node(Goal Node if it is found)
        print(node.x,node.y, node.parentIs)
        #until we reach the start node 
        while node.parentIs != start:
            path_node.append(node)
            node = node.parentIs
        path_node.append(start)
        path_node.reverse()

    pygame.init()
    # Set the dimensions of the screen
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("RRT Smart")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Create Screen
        screen.fill(white)

        # Draw Obstacles
        for obstacle in obstacles:
            pygame.draw.circle(screen, black, (obstacle[0], obstacle[1]), obstacle[2])

        # Draw the nodes and edges of the tree
        for node in path:
            if node.parentIs is not None:
                pygame.draw.line(screen, blue, (node.x, node.y), (node.parentIs.x, node.parentIs.y))

            pygame.draw.circle(screen, green, (node.x, node.y), 3)

        # Draw the path if it exists
        if path is not None:
            for i in range(len(path_node) - 1):
                pygame.draw.line(screen, red, (path_node[i].x, path_node[i].y), (path_node[i+1].x, path_node[i+1].y),width=4)

        # Draw the start and goal points
        pygame.draw.circle(screen, black, (start.x, start.y), 10)
        pygame.draw.circle(screen, red, (goal.x, goal.y), 10)

        # Update the screen
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

