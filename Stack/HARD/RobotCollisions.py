'''
2751. Robot Collisions
There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.    
'''
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        '''
            Intuition: 
            Traverse from left to right the robots based on postions:
            all the right moving robots are placed on a stack.
            if we encounter a left moving robot we compare it with element 
            on top of a stack.
        '''
        
        n = len(positions)
        ind = [i for i in range(n)]
        ind.sort(key=lambda x: positions[x])
        s = []
        for x in ind:
            if directions[x] == 'L':
                while s:
                    y = s[-1]
                    if healths[x] == healths[y]:
                        healths[x] = healths[y] = 0
                        s.pop()
                        break
                    if healths[x] > healths[y]:
                        healths[x] -= 1
                        healths[y] = 0
                        s.pop()
                    else:
                        healths[x] = 0
                        healths[y] -= 1
                        break
            else:
                s.append(x)
        r = [x for x in healths if x]
        return r
