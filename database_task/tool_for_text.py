import classes
from functions import strings_to_functions

def specify_choice(user_selection):
    match user_selection:
        case '1':
            news = classes.News()
            csv_processor = classes.CsvProcessor()
            print('You have 2 options. Post as it is (1) or update before sending (2)')
            action = input('Specify your action (1-2): ')
            if action == '1':
                news.post_new_evidence(news.text_of_news, news.city, news.date_of_post)
                csv_processor.word_counter()
                csv_processor.detailed_counter()
                print('Your news are posted to text_with_output file. Good Job!')
            else:
                news.text_of_news = input('Please update the text: ')
                news.city = input('Please update the city: ')
                news.post_new_evidence(news.text_of_news, news.city, news.date_of_post)
                csv_processor.word_counter()
                csv_processor.detailed_counter()
        case '2':
            advertising = classes.Advertising()
            csv_processor = classes.CsvProcessor()
            print('You have 2 options. Post as it is (1) or update before sending (2)')
            action = input('Specify your action (1-2): ')
            if action == '1':
                days_to_expire = advertising.calculate_days_to_expire()
                advertising.post_your_ad(advertising.ad_text, days_to_expire)
                csv_processor.word_counter()
                csv_processor.detailed_counter()
                print('Your ad is posted to text_with_output file. Good Job!')
            else:
                advertising.ad_text = input('Please update the text: ')
                days_to_expire = advertising.calculate_days_to_expire()
                advertising.post_your_ad(advertising.ad_text, days_to_expire)
                csv_processor.word_counter()
                csv_processor.detailed_counter()
        case '3':
            twitter = classes.TwitterPost()
            csv_processor = classes.CsvProcessor()
            print('You have 3 options to do with your twitter post:\n'
                  '1. Send a news\n'
                  '2. Place an advertising\n'
                  '3. Share your own ideas in your post\n')
            type_of_post = input('Please specify your post type: ')
            match type_of_post:
                case '1':
                    print('You have 2 options. Post as it is (1) or update before sending (2)')
                    action = input('Specify your action (1-2): ')
                    if action == '1':
                        twitter.post_new_evidence(twitter.text_of_news, twitter.city, twitter.date_of_post)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                        print('Your news are posted to text_with_output file. Good Job!')
                    else:
                        twitter.text_of_news = input('Please update the text: ')
                        twitter.city = input('Please update the city: ')
                        twitter.post_new_evidence(twitter.text_of_news, twitter.city, twitter.date_of_post)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                        print('Your news are posted to text_with_output file. Good Job!')
                case '2':
                    print('You have 2 options. Post as it is (1) or update before sending (2)')
                    action = input('Specify your action (1-2): ')
                    if action == '1':
                        days_to_expire = twitter.calculate_days_to_expire()
                        twitter.post_your_ad(twitter.ad_text, days_to_expire)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                        print('Your ad is posted to text_with_output file. Good Job!')
                    else:
                        twitter.ad_text = input('Please update the text: ')
                        days_to_expire = twitter.calculate_days_to_expire()
                        twitter.post_your_ad(twitter.ad_text, days_to_expire)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                        print('Your ad is posted to text_with_output file. Good Job!')
                case '3':
                    print('You have 2 options. Post as it is (1) or update before sending (2)')
                    action = input('Specify your action (1-2): ')
                    if action == '1':
                        twitter.post_your_ideas(twitter.user_name, twitter.post_text, twitter.date_of_post)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                        print('Your ideas are posted to text_with_output file. Good Job!')
                    else:
                        twitter.ad_text = input('Please update the text: ')
                        twitter.user_name = input('Please update the username')
                        twitter.post_your_ideas(twitter.user_name, twitter.post_text, twitter.date_of_post)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                        print('Your ideas are posted to text_with_output file. Good Job!')
        case '4':
            reader = classes.FileReader()
            csv_processor = classes.CsvProcessor()
            print('You have 2 options: \n'
                  '1. Write from file with current folder. \n'
                  '2. specify path on your own.')
            user_option = input('Please specify your option: ')
            match user_option:
                case '1':
                    text = reader.read_file_with_items()
                    if text != 'Format mismatch!':
                        normalized_text = strings_to_functions.normalize_text(reader.read_file_with_items())
                        reader.write_file_from_another(normalized_text)
                        reader.delete_input_file()
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                    else:
                        print('Incorrect text format!')
                case '2':
                    path_to_file = input('Please specify your path\\to\\file: ')
                    text = reader.read_file_with_items()
                    if text != 'Format mismatch!':
                        normalized_text = strings_to_functions.normalize_text(reader.read_file_with_items(path_to_file))
                        reader.write_file_from_another(normalized_text)
                        reader.delete_input_file(path_to_file)
                        csv_processor.word_counter()
                        csv_processor.detailed_counter()
                    else:
                        print('Incorrect text format!')
        case '5':
            json_validator = classes.JsonProcessor()
            print('Please select options: \n'
                  '1. Take JSON from the current folder\n'
                  '2. Specify path to JSON file.\n')
            user_option = input('Please specify your option: ')
            match user_option:
                case '1':
                    json_validator.json_schema_validator()
                    json_validator.remove_json()
                case '2':
                    path_to_file = input('Please specify path to file: ')
                    json_validator.json_schema_validator(path_to_file)
                    json_validator.remove_json()
        case '6':
            xml_validator = classes.XmlProcessor()
            print('Please select options: \n'
                  '1. Take XML from the current folder\n'
                  '2. Specify path to XML file.\n')
            user_option = input('Please specify your option: ')
            match user_option:
                case '1':
                    xml_validator.xml_schema_validator()
                    xml_validator.remove_xml()
                case '2':
                    path_to_file = input('Please specify path to file: ')
                    xml_validator.xml_schema_validator(path_to_file)
                    xml_validator.remove_xml()
        case '7':
            print('Please select options to insert to database: \n'
                  '1. Record news to Database\n'
                  '2. Record ads to Database\n'
                  '3. Record twits to your database.')
            user_option = input('Please specify your option: ')
            match user_option:
                case '1':
                    news = input('Please specify your news: ')
                    city = input('Please specify city of news: ')
                    date_of_post = input('Please specify date of post: ')
                    classes.DbProcessor.insert_record_into_news(news, city, date_of_post)
                case '2':
                    ads = input('Please specify your ads: ')
                    expiration_date = input('Please specify expiration date: ')
                    classes.DbProcessor.insert_records_into_ads(ads, expiration_date)
                case '3':
                    user_name = input('Please specify your username: ')
                    post_text = input('Please share your ideas: ')
                    date_of_post = input('Please specify date of post: ')
                    classes.DbProcessor.insert_records_into_twits(user_name, post_text, date_of_post)
                
        case _:
            print('Wrong parameter! Please select from 1 to 5')


while True:
    print('Welcome! Here you can get some stuff for you. Here is options list.\n'
          'Use numbers to select proper option:\n'
          '1. News\n'
          '2. Advertising\n'
          '3. Twitter post\n'
          '4. Input from file\n'
          '5. JSON input\n'
          '6. XML input\n'
          '7. Insert into database\n'
          '8. Exit.')
    user_choice = input('Please specify your option from 1 to 8: ')
    if user_choice == '8':
        print('Thank you for your time!')
        break
    specify_choice(user_choice)