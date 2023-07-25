import os
import string
import sys
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
    
    @staticmethod
    def post_new_evidence(text_of_news: str, city: str, date_of_post) -> None:
        with open('text_with_output', 'a') as file:
            file.write(('-' * 10) + '\n')
            file.write('News: \n')
            file.write(text_of_news + '\n')
            file.write(f'Issued city: {city} \t Date_of_post: {date_of_post} \n')
            file.write(('-' * 10) + '\n')
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
    
    @staticmethod
    def calculate_days_to_expire(self):
        if (self._expiration_date - date.today()).days <= 0:
            return 'Expired'
        else:
            return (self._expiration_date - date.today()).days
    
    @staticmethod
    def post_your_ad(ad_text: str, expiration_date) -> None:
        with open('text_with_output', 'a') as file:
            file.write(('-' * 10) + '\n')
            file.write('Ad: \n')
            file.write(ad_text + '\n')
            file.write(f'Days_to_expire: {expiration_date} \n')
            file.write(('-' * 10) + '\n')
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
    
    @staticmethod
    def post_your_ideas(user_name: str, post_text: str, date_of_post) -> None:
        with open('text_with_output', 'a') as file:
            file.write(('-' * 10) + '\n')
            file.write(f'Posted by {user_name}: \n')
            file.write(post_text + '\n')
            file.write(f'Date_of_post: {date_of_post} \n')
            file.write(('-' * 10) + '\n')
        return
    
    @staticmethod
    def post_new_evidence(text_of_news: str, city: str, date_of_post) -> None:
        with open('text_with_output', 'a') as file:
            file.write(('-' * 10) + '\n')
            file.write(text_of_news + '\n')
            file.write(f'Issued city: {city} \t Date_of_post: {date_of_post} \n')
            file.write(('-' * 10) + '\n')
        return
    
    @staticmethod
    def post_your_ad(ad_text: str, expiration_date) -> None:
        with open('text_with_output', 'a') as file:
            file.write(('-' * 10) + '\n')
            file.write('Ad: ')
            file.write(ad_text + '\n')
            file.write(f'Days_to_expire: {expiration_date} \n')
            file.write(('-' * 10) + '\n')
        return


class FileReader:
    def read_file_with_items(self, path=f'{sys.path[0]}\\text_to_input.txt') -> str:
        with open(path, 'r') as file_to_read:
            text = file_to_read.read()
            if text.startswith('-' * 10 + '\n') and text.endswith('-' * 10 + '\n'):
                return text
            else:
                return 'Format mismatch!'
    
    def write_file_from_another(self, text: str) -> None:
        with open('text_with_output', 'a') as file:
            file.write(text)
            return
    
    def delete_input_file(self, path=f'{sys.path[0]}\\text_to_input.txt') -> None:
        os.remove(path)
        return


class CsvProcessor:
    def word_counter(self) -> None:
        import csv
        with open('text_with_output', 'r') as file_reader:
            reader = file_reader.read()
        
        with open('word_counter.csv', 'w') as word_counter:
            writer = csv.writer(word_counter, delimiter='-')
            words = list(set(reader.lower().split()))
            for word in words:
                writer.writerow([f'{word}', f'{reader.lower().count(word)}'])
        return
    
    def detailed_counter(self):
        import csv
        with open('text_with_output', 'r') as file_reader:
            reader = file_reader.read()
        
        with open('detailed_counter.csv', 'w') as detailed_counter:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(detailed_counter, fieldnames=headers)
            writer.writeheader()
            for char in string.ascii_lowercase:
                writer.writerow({'letter': f'{char}',
                                 'count_all': f'{reader.lower().count(char)}',
                                 'count_uppercase': f'{reader.count(char.upper())}',
                                 'percentage': f'{reader.lower().count(char) * 100 / len(reader)}'})
        return


class JsonProcessor:
    def json_schema_validator(self, path=f'{sys.path[0]}\\file_to_input.json'):
        import json
        json_to_review = json.load(open(path))
        if sorted(json_to_review.keys()) == sorted(['type', 'text_of_news', 'city', 'date_of_post']):
            News.post_new_evidence(json_to_review['text_of_news'],
                                   json_to_review['city'], json_to_review['date_of_post'])
            csv_processor = CsvProcessor()
            csv_processor.word_counter()
            csv_processor.detailed_counter()
        elif sorted(json_to_review.keys()) == sorted(['type', 'ad_text', 'days_to_expire']):
            Advertising.post_your_ad(json_to_review['ad_text'], json_to_review['days_to_expire'])
            csv_processor = CsvProcessor()
            csv_processor.word_counter()
            csv_processor.detailed_counter()
        elif sorted(json_to_review.keys()) == sorted(['type', 'user_name', 'post_text', 'date_of_post']):
            TwitterPost.post_your_ideas(json_to_review['user_name'], json_to_review['post_text'],
                                        json_to_review['date_of_post'])
            csv_processor = CsvProcessor()
            csv_processor.word_counter()
            csv_processor.detailed_counter()
        else:
            return 'Incorrect file structure!'
    
    @staticmethod
    def remove_json(path=f'{sys.path[0]}\\file_to_input.json'):
        os.remove(path)
        return


class XmlProcessor:
    def xml_schema_validator(self, path=f'{sys.path[0]}\\file_to_input.xml'):
        import xml.etree.ElementTree as ET
        xml_file = ET.parse(path)
        root = xml_file.getroot()
        child_elements = list(root)
        list_of_tags = []
        for element in child_elements:
            list_of_tags.append(element.tag)
        if sorted(list_of_tags) == sorted(['type', 'text_of_news', 'city', 'date_of_post']):
            News.post_new_evidence(root.find('text_of_news').text,
                                   root.find('city').text, root.find('date_of_post').text)
            csv_processor = CsvProcessor()
            csv_processor.word_counter()
            csv_processor.detailed_counter()
        elif sorted(list_of_tags) == sorted(['type', 'ad_text', 'days_to_expire']):
            Advertising.post_your_ad(root.find('ad_text').text, root.find('days_to_expire').text)
            csv_processor = CsvProcessor()
            csv_processor.word_counter()
            csv_processor.detailed_counter()
        elif sorted(list_of_tags) == sorted(['type', 'user_name', 'post_text', 'date_of_post']):
            TwitterPost.post_your_ideas(root.find('user_name').text, root.find('post_text').text,
                                    root.find('date_of_post').text)
            csv_processor = CsvProcessor()
            csv_processor.word_counter()
            csv_processor.detailed_counter()
        else:
            print('Incorrect file structure!')
    
    @staticmethod
    def remove_xml(path=f'{sys.path[0]}\\file_to_input.xml'):
        os.remove(path)
        return
