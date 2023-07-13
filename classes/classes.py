from datetime import date


class News:
    def __init__(self):
        self._text_of_news = input('Please specify your news: ')
        self._city = input('Please specify your city: ')
        self._date_of_post = date.today().strftime('%d-%m-%Y')
    
    @property
    def text_of_news(self):
        return self._text_of_news
    
    @property
    def city(self):
        return self._city
    
    @property
    def date_of_post(self):
        return self._date_of_post
    
    @text_of_news.setter
    def text_of_news(self, value):
        self._text_of_news = value
    
    @city.setter
    def city(self, value):
        self._city = value
    
    def post_new_evidence(self, text_of_news: str, city: str, date_of_post) -> None:
        with open('text_with_output', 'a') as file:
            file.write('News: ' + ('-' * 10) + '\n')
            file.write(text_of_news + '\n')
            file.write(f'Issued city: {city} \t Date_of_post: {date_of_post} \n\n')
        return


class Advertising:
    def __init__(self):
        self._ad_text = input('Please specify your ad: ')
        self._expiration_date_str = input('Please specify expiration date in yyyy-mm-dd format: ')
        self._expiration_date = date.fromisoformat(self._expiration_date_str)
    
    @property
    def ad_text(self):
        return self._ad_text
    
    @property
    def expiration_date(self):
        return self._expiration_date
    
    @ad_text.setter
    def ad_text(self, value):
        self._ad_text = value
    
    def calculate_days_to_expire(self):
        if (self._expiration_date - date.today()).days <= 0:
            return 'Expired'
        else:
            return (self._expiration_date - date.today()).days
    
    def post_your_ad(self, ad_text: str, expiration_date) -> None:
        with open('text_with_output', 'a') as file:
            file.write('Ad: ' + ('-' * 10) + '\n')
            file.write(ad_text + '\n')
            file.write(f'Days_to_expire: {expiration_date} \n\n')
        return


class TwitterPost(News, Advertising):
    def __init__(self):
        super().__init__()
        self._post_text = input('Specify text of your post: ')
        self._user_name = input('Specify your username: ')
        self._customer_name = input('Specify customer name: ')
    
    @property
    def post_text(self):
        return self._post_text
    
    @post_text.setter
    def post_text(self, value):
        self._post_text = value
    
    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    
    def post_your_ideas(self, user_name: str, post_text: str, date_of_post) -> None:
        with open('text_with_output', 'a') as file:
            file.write(f'Posted by {user_name}: ' + ('-' * 10) + '\n')
            file.write(post_text + '\n')
            file.write(f'Date_of_post: {date_of_post} \n\n')
        return
    
    def post_new_evidence(self, text_of_news: str, city: str, date_of_post) -> None:
        with open('text_with_output', 'a') as file:
            file.write(f'Posted by {self._user_name}. Please specify your_news: ' + ('-' * 10) + '\n')
            file.write(text_of_news + '\n')
            file.write(f'Issued city: {city} \t Date_of_post: {date_of_post} \n\n')
        return
    
    def post_your_ad(self, ad_text: str, expiration_date) -> None:
        with open('text_with_output', 'a') as file:
            file.write('Ad: ' + ('-' * 10) + '\n')
            file.write(f'Customer is {self._customer_name}: ')
            file.write(ad_text + '\n')
            file.write(f'Days_to_expire: {expiration_date} \n\n')
        return
