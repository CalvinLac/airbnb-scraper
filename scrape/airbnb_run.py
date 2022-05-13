from airbnb_parser import Parser
import time
import datetime

if __name__ == "__main__":
    # parameterize dates
    date_1 = datetime.date.today() + datetime.timedelta(days=7)
    date_2 = datetime.date.today() + datetime.timedelta(days=14)
    date_1 = date_1.strftime('%Y-%m-%d')
    date_2 = date_2.strftime('%Y-%m-%d')

    locations = {
        'Canmore': f'https://www.airbnb.ca/s/Canmore--Alberta--Canada/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Canmore%2C%20Alberta%2C%20Canada&place_id=ChIJMWNFlZXFcFMRLmkenl8xtkY&checkin={date_1}&checkout={date_2}&adults=2&source=structured_search_input_header&search_type=autocomplete_click'
        # 'Canmore2': f'https://www.airbnb.ca/s/Canmore--Alberta--Canada/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Canmore%2C%20Alberta%2C%20Canada&place_id=ChIJMWNFlZXFcFMRLmkenl8xtkY&checkin={date_1}&checkout={date_2}&adults=2&source=structured_search_input_header&search_type=autocomplete_click'
    }

    for location in locations:
        new_parser = Parser(locations[location], f'./{location}.csv')
        t0 = time.time()
        new_parser.parse()