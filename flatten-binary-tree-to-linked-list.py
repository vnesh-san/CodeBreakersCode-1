class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
          return None
        
        self.dfs(root, [])
        
    def dfs(self, vert, visited = []):
      if vert in visited:
        return None
      
      visited.append(vert)
      if vert.left == None and vert.right == None:
        return vert
      
      left_vert = None
      right_vert = None 
      if vert.left:
        left_vert = self.dfs(vert.left, visited) # O(n)
      if vert.right:
        right_vert = self.dfs(vert.right, visited) # O(n)
        
      if left_vert:
        left_vert_tail = left_vert
        while left_vert_tail.right:
          left_vert_tail = left_vert_tail.right
        
        left_vert_tail.right = right_vert
        vert.right = left_vert
        vert.left = None 
      else:
        vert.right = right_vert
        vert.left = None 
      
        
      return vert

  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
      return None

    if not root.left and not root.right:
      return root

    return self.dfs(root, []) #n

  # 2nd attempt
  def dfs(self, vert, visited = []) -> TreeNode:
    if vert in visited:
      return

    visited.append(vert)

    if not vert.left and not vert.right:
      return vert

    left_child = None
    right_child = None
    if vert.left:
      left_child = self.dfs(vert.left, visited) #n
    if vert.right:
      right_child = self.dfs(vert.right, visited) #n

    if left_child:
      last_left_node = left_child
      while last_left_node.right:
        last_left_node = last_left_node.right
      
      if last_left_node:
        last_left_node.right = right_child

    if left_child:
      vert.right = left_child
    else:
      vert.right = right_child
      
    vert.left = None 

    return vert
  
  # 3rd attempt
  def dfs(self, vert: TreeNode) -> None:
    if not vert.left and not vert.right:
      return vert
    
    left_child = None
    right_child = None
    
    if vert.left:
      left_child = self.dfs(vert.left)
    if vert.right:
      right_child = self.dfs(vert.right)
   
    last_left_child = left_child
    while last_left_child and last_left_child.right: #n
      last_left_child = last_left_child.right
    
    if left_child:
      vert.right = left_child
      last_left_child.right = right_child 
    else:
      vert.right = right_child
      
    vert.left = None
    return vert

# 4th attempt
def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
      return None
      
    if root.left is None and root.right is None:
      return root 
    
    return self.traverse_tree(root) #n

  def traverse_tree(self, root):
    if root.left is None and root.right is None: 
      return root
    
    left_child = None
    right_child = None
    last_right_node_left_child = None

    if root.left:
      left_child = self.traverse_tree(root.left) #n
    
    if root.right:
      right_child = self.traverse_tree(root.right) #n
    
    if left_child:
       last_right_node_left_child = left_child
      while last_right_node_left_child.right is not None:
        last_right_node_left_child = last_right_node_left_child.right
    
    if last_right_node_left_child:
      last_right_node_left_child.right = right_child
      last_right_node_left_child.left = None
    
    if left_child: 
      root.right = left_child
    else: 
      root.right = right_child
    
    root.left = None
    return root 
