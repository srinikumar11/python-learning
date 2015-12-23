import datetime
import webbrowser


answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    ans = input('What date would you like? Please use the MM/DD format, enter "quit", to quit ')
    if ans.upper() == 'QUIT':
        break;
    
    try:
        date = datetime.datetime.strptime(ans, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
        webbrowser.get('safari').open_new(output)
    except ValueError:
        print("thats not a valid format")