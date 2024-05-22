#tic-tac-toe
X="X"
O="O"
Empty=""
TIE="TIE"
NUM_SQUARE=9
def display_instruct():
    print(
        """Welcome to the greatest intellectual challenge of all time :Tic-Tac-Toe.
        This will be  a showdown between your human brain and the silicon processor.
        
        You willl make  your move known by enterring a number between 0-8.The number will correspond to the board position as illustrated:
                         0|1|2
                         3|4|5
                         6|7|8
       prepare yourself ,human.The ultimate battle is about to begin.\n                  """
    )
    def ask_yes_no(question):
        """Ask a yes  or no question"""
        respond=None
        while respond not in("y","n"):
            respond =input(question).lower()
            return respond
        #main 
       
       
        answer=ask_yes_no("\nPlease enter 'y'or'n':")
        print("Thanks for Entering:")
        def ask_number(question,low,high):
            """Ask for a number within the range"""
            respond=None 
            while  respond not in range(low,high):
                respond=int(input(question))
                return respond
            def pieces():
                go_first=ask_yes_no("Do you require to  respond the first move?(y/n:)")
                if go_first=="y":
                    print("Then take the first move.You will need it.")
                    human=X
                    computer=O
                else:
                    print("\nYour bravery will be your undoing...l will go first.")
                    computer=X
                    human=O
                    return computer,human