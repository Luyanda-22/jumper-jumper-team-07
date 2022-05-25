
"""This is a dictionary of the four possible "guys" you will see
when you play the game. The guy starting at 0 is the guy you start
out with, and ranging from 0 to 4, depending on how many lives you've
lost, that'll be the guy that you see."""
guy = {
  
0: """
            ___  
           /___\ 
           \   / 
            \ /               
             0   
            /|\  
            / \  
          
           ^^^^^^^""",

1:"""                 
           /___\ 
           \   / 
            \ /  
             0   
            /|\  
            / \  
                    
           ^^^^^^^""",
                   
2:"""          
           \   / 
            \ /  
             0   
            /|\  
            / \  

          ^^^^^^^""",

3:"""          
            \ /  
             0   
            /|\  
            / \  

          ^^^^^^^""",

4:"""

             x   
            /|\  
            / \  
          
          ^^^^^^^"""}

'''def print_jumper(self):
    """PUT COMMENT HERE"""
    for x in range(0, len(self.jumper)):
      print(self.jumper[x])

  def remove_line(self):
    """PUT COMMENT HERE"""
    self.jumper.remove(self.jumper[0])'''