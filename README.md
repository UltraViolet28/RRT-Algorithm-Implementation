# RRT-Algorithm-Implementation
This is a Python implementation of the RRT* algorithm, a popular path planning algorithm in robotics, and an accompanying visualization of the algorithm's execution. The visualization is implemented using the Pygame library.

## Requirements
To run this program, you will need Python 3 installed on your machine, as well as the Pygame library. You can install Pygame using pip:

`
pip install pygame
`
## Run the Code
To run the program for RRT* Smart, execute the rrt_start_smart.py file:

`python rrt_start_smart.py`

This will launch the visualization window. You can modify the start and goal positions, as well as the obstacle positions, in the main function of the code. The obstacles are listed as tuples represented by (x,y,radius)(* Obstacles here are circles).

Other factors like bias in case of *smart algorithms can be changed in the RRT_star function.

There are also other variations of the RRT algorithm in the codes folder like basic RRT, RRT* and RRT-smart. 

## Visualisation
The visualization shows the RRT* Smart Algorithm constructing a tree from the start node to the goal node while avoiding obstacles. The blue lines represent the connections between nodes in the tree, while the Red line represents the path from the start node to the goal node.

## Results
1. RRT Star Smart Variation
![RRT_StarSmart_pic2](https://user-images.githubusercontent.com/88196192/220945227-65ec26a9-54be-42e0-b705-fc78573a1df8.png)

2. RRT Star Smart Variation with bias = 6 (60% will be random points others will be towards goal)
![RRT_StarSmart_bias6](https://user-images.githubusercontent.com/88196192/220945962-7109a57c-64c6-414b-8893-70367b1aa79a.png)

3. RRT Star Variation
![RRT_Star_pic2](https://user-images.githubusercontent.com/88196192/220945961-a2605e9e-4f8f-4ede-a1f3-ff87a4d9c796.png)

4. RRT Star Variation
![RRT_Star_pic1](https://user-images.githubusercontent.com/88196192/220945963-6d44bc21-d210-49ab-936c-d81d1eabc4da.png)

5. RRT-Smart Variation
![RRT_Smart](https://user-images.githubusercontent.com/88196192/220945964-89d81bf9-c803-4cbc-a45b-79aab9be6c5e.png)

6. Normal RRT Variation
![RRT](https://user-images.githubusercontent.com/88196192/220945980-3f5c0871-178e-43d4-8f36-7a12ea613cab.png)

6. Case when an iteration fails to find the goal
![RRT_Iteration Failed](https://user-images.githubusercontent.com/88196192/220945992-e23510f6-794f-4dbf-8552-329409df77d7.png)

