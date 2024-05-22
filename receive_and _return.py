#Receive and return
#Demonstrate parameters and return values
def display (message):
    print(message)
    def give_me_five():
        five=5
        return five
    def ask_yes_no(question):
        """Ask a yes  or no question"""
        respond=None
        while respond not in("y","n"):
            respond =input(question).lower()
            return respond
        #main 
        display("Here's a message for you.\n")
        number=give_me_five()
        print("here's what l got from the give_me_five():",number)
        answer=ask_yes_no("\nPlease enter 'y'or'n':")
        print("Thanks for Entering:")
