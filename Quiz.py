def main():
    
    qs = {"What is the first name of Iron Man?" : "Tony", "Who is called the god of lightning in Avengers?" : "Thor" , "Who carries a shield of American flag theme in Avengers?" : "Captain America" , "Which avenger is green in color?" : "Hulk" , "Which avenger can change it's size?" : "AntMan" , "Which Avenger is red in color and has mind stone?" : "Vision"}

    print("*** Quiz ***\n")
    name = input("Please enter your name: ").title()
    print()
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(qs), len(qs)))
    
def quiz(qs):
    score = 0
    for q,a in qs.items():
        if input(q).lower() == a.lower():
            score += 1
            print("Correct.")
        else:
            print("Sorry, correct answer is \"{}\".".format(a))
            return score
 
if __name__ == "__main__":
    main()