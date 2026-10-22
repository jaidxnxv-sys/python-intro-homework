#assign letter grade based on score
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return "D"
  else:
    return "F"

def main():
  try:
    #user input validation
    score_input = input("Enter your score: ").strip()
    #number
    if not score_input.isdigit():
       print("invalid input. enter number between 1-100")

    score = int(score_input)

    if score < 0 or score > 100:
      print("invalid")
      return

  #print grade
    grade = get_letter_grade(score)
    print(f"Your grade is:  {grade}")

  except Exception as e:
    print(f"error: {e}")




if __name__ == "__main__":
  main()
