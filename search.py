# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
#
#
#
#Em da chay duoc 3 thuat toan DFS,BFS,UCS,ASTAR.

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	fringe = util.Stack()
	closedSet = set()
	fringe.push((problem.getStartState(),[]))
	while fringe.isEmpty() == False:
		state,path = fringe.pop()
		if problem.isGoalState(state):
			return path
		if state not in closedSet:
			closedSet.add(state)
			successors = problem.getSuccessors(state)
			for successor in successors:
				fringe.push((successor[0], path + [successor[1]]))
	print 'No solution'
	return []
	util.raiseNotDefined()
	

def breadthFirstSearch(problem):
	fringe = util.Queue()
	closedSet = set()
	fringe.push((problem.getStartState(),[]))
	while fringe.isEmpty() == False:
		state,path = fringe.pop()
		if problem.isGoalState(state):
			return path
		if state not in closedSet:
			closedSet.add(state)
			successors = problem.getSuccessors(state)
			for successor in successors:
				fringe.push((successor[0], path + [successor[1]]))
	print'No solution'
	return []
	util.raiseNotDefined()

def uniformCostSearch(problem):
	fringe = util.PriorityQueue()
	closedSet = set()
	fringe.push((problem.getStartState(),[]),0)
	while fringe.isEmpty() == False:
		state, path = fringe.pop()
		if problem.isGoalState(state):
			return path
		if state not in closedSet:
			closedSet.add(state)
			for successor in problem.getSuccessors(state):
				tempState, move, cost = successor
				fringe.push((tempState, path + [move]), problem.getCostOfActions(path + [move]))
	return []
	util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [],0),0 + heuristic(problem.getStartState(),problem))
    closeset = set()
    while (fringe.isEmpty() == False):
        state, path, cost = fringe.pop()
        if problem.isGoalState(state):
            return path
        if state not in closeset:
            closeset.add(state)
            for i in problem.getSuccessors(state):
                fringe.push((i[0],path + [i[1]],cost+i[2]),cost+i[2] + heuristic(i[0], problem))
    return []
    util.raiseNotDefined()
#
#
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
