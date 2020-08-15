'''
Choose Your Own Adventure: Wilderness Escape
Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure. Our users get a unique story experience by picking the next chapter of their adventure. We use the tree data structure to keep track of the different paths a user may choose. Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.
'''

######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece # data
    self.choices = [] # references to other nodes

  def add_child(self, node):
    # creates parent-child relationship
    #print("Adding " + child_node.story_piece)
    self.choices.append(node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.story_piece + " from " + self.story_piece)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      choice=input("Enter your choice (1 or 2): ")
      if choice not in ['1','2']:
        print("Please make a valid choice: either 1 or 2")
      else:
        chosen_index=int(choice)
        chosen_index-=1
        chosen_child=story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node=chosen_child


######
# TESTING AREA
######
print("Once upon a time…")
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
user_choice=input("What is your name? ")
print(user_choice)

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_b_1=TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")

choice_b_2=TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_1)

story_root.traverse()