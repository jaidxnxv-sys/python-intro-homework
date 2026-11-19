from datetime import datetime

def print_date():
  try:
    #current date and time
    today = datetime.now()
    #format date
    formatted_date = today.strftime("Today is %B %d, %Y")
    #print
    print(formatted_date)
  except Exception as e:
    print(f'Error Occured: {e}')

if __name__ == '__main__':
  print_date()