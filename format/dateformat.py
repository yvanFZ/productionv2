import datetime

def dateformat(string_date):
    # Try to parse the date string using different formats
    formats = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d', '%Y/%m/%d']
    if string_date != None:
        for format in formats:
            try:
                date = datetime.datetime.strptime(string_date, format)
            
                date_string_juiste_format = date.strftime('%d-%m-%Y')
                # print('Date format:', date_string_juiste_format)
                return date_string_juiste_format
            except ValueError:
                pass
    else:
        return string_date