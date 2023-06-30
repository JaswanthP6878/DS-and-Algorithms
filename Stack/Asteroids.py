'''
735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
 Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. 

If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                st.append(i)
            else :
                while (st):
                    left_moving = (-1) *asteroids[i]
                    y = st[-1]
                    if left_moving == asteroids[y]:
                        asteroids[y] = asteroids[i] = 0
                        st.pop()
                        break
                    elif left_moving > asteroids[y]:
                        asteroids[y] = 0
                        st.pop()
                    else :
                        asteroids[i] = 0
                        break
        return [i for i in asteroids if i != 0]                
