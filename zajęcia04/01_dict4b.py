dzien = input('Wpisz dzień tygodnia po polsku: ')

dni_tygodnia = {'poniedziałek': 'Monday',
                'wtorek': 'Tuesday',
                'środa': 'Wednesday',
                'czwartek': 'Thursday',
                'piątek': 'Friday',
                'sobota': 'Saturday',
                'niedziela': 'Sunday'}

print(f'{dzien} po angielsku to: {dni_tygodnia[dzien]}')
