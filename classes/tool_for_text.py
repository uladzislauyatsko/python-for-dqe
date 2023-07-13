import classes


def specify_choice(user_selection):
    match user_selection:
        case '1':
            news = classes.News()
            print('You have 2 options. Post as it is (1) or update before sending (2)')
            action = input('Specify your action (1-2): ')
            if action == '1':
                news.post_new_evidence(news.text_of_news, news.city, news.date_of_post)
                print('Your news are posted to text_with_output file. Good Job!')
            else:
                news.text_of_news = input('Please update the text: ')
                news.city = input('Please update the city: ')
                news.post_new_evidence(news.text_of_news, news.city, news.date_of_post)
        case '2':
            advertising = classes.Advertising()
            print('You have 2 options. Post as it is (1) or update before sending (2)')
            action = input('Specify your action (1-2): ')
            if action == '1':
                days_to_expire = advertising.calculate_days_to_expire()
                advertising.post_your_ad(advertising.ad_text, days_to_expire)
                print('Your ad is posted to text_with_output file. Good Job!')
            else:
                advertising.ad_text = input('Please update the text: ')
                days_to_expire = advertising.calculate_days_to_expire()
                advertising.post_your_ad(advertising.ad_text, days_to_expire)
        case '3':
            twitter = classes.TwitterPost()
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
                        print('Your news are posted to text_with_output file. Good Job!')
                    else:
                        twitter.text_of_news = input('Please update the text: ')
                        twitter.city = input('Please update the city: ')
                        twitter.post_new_evidence(twitter.text_of_news, twitter.city, twitter.date_of_post)
                        print('Your news are posted to text_with_output file. Good Job!')
                case '2':
                    print('You have 2 options. Post as it is (1) or update before sending (2)')
                    action = input('Specify your action (1-2): ')
                    if action == '1':
                        days_to_expire = twitter.calculate_days_to_expire()
                        twitter.post_your_ad(twitter.ad_text, days_to_expire)
                        print('Your ad is posted to text_with_output file. Good Job!')
                    else:
                        twitter.ad_text = input('Please update the text: ')
                        days_to_expire = twitter.calculate_days_to_expire()
                        twitter.post_your_ad(twitter.ad_text, days_to_expire)
                        print('Your ad is posted to text_with_output file. Good Job!')
                case '3':
                    print('You have 2 options. Post as it is (1) or update before sending (2)')
                    action = input('Specify your action (1-2): ')
                    if action == '1':
                        twitter.post_your_ideas(twitter.user_name, twitter.post_text, twitter.date_of_post)
                        print('Your ideas are posted to text_with_output file. Good Job!')
                    else:
                        twitter.ad_text = input('Please update the text: ')
                        twitter.user_name = input('Please update the username')
                        twitter.post_your_ideas(twitter.user_name, twitter.post_text, twitter.date_of_post)
                        print('Your ideas are posted to text_with_output file. Good Job!')
        case _:
            print('Wrong parameter! Please select from 1 to 4')


while True:
    print('Welcome! Here you can get some stuff for you. Here is options list.\n'
          'Use numbers to select proper option:\n'
          '1. News\n'
          '2. Advertising\n'
          '3. Twitter post\n'
          '4. Exit.')
    user_choice = input('Please specify your option from 1 to 4: ')
    if user_choice == '4':
        print('Thank you for your time!')
        break
    specify_choice(user_choice)
