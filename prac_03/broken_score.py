def score_result(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter Score Again... "))
    else:
        if score >= 90:
            result = "Excellent"
        if score >= 50 and score < 90:
            result = "Passable"
        if score < 50:
            result = "Bad"
    return result

def main():
    score = float(input("Enter score: "))
    print(score_result(score))
main()
