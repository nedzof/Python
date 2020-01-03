import pymssql
from faker import Faker
import random

tbl = 'schema.name'
db = 'name'
V_host="192.168.01.01:1434"
dataCount = 2000

cnxn = pymssql.connect(server=V_host)
cursor = cnxn.cursor()
cursor.execute("USE [{}] DELETE FROM {}".format(db,tbl))
cnxn.commit()


fakerDE = Faker(['de_DE'])
fakerCH = Faker(['de_CH'])
fakerFR = Faker(['fr_CH'])
for i in range(1,dataCount +1):
        firstname = fakerCH.first_name() 
        lastname = fakerCH.last_name()
        address = fakerDE.address()
        phone = fakerFR.phone_number()
        ssn = fakerCH.ssn()
        query = "USE ["+db+"] INSERT INTO ["+tbl+"] VALUES ('{}','{}','{}','{}','{}')".format(i,firstname+' '+lastname,address,phone,ssn)
        cursor.execute(query)
        cnxn.commit()
        print('[*]: ', query.split('VALUES')[1])


cursor.close()
cnxn.close()
print('[+] FINISHED: ',dataCount,' Rows inserted! [+]')


"""
class FakeData:

        rowNumber = 0

        def __init__(self, name, salary):
                FakeData.rowNumber += 1
                self.name = name
                self.salary = salary

        def create(self):
                firstname = faker.first_name() 
                lastname = faker.last_name()
                address = faker.address()
                phone = faker.phone_number()
                ssn = faker.ssn()
"""


"""
Language de_CH
faker.providers.address
fake.address()
# '82668 Giada Underpass\nSchumacherchester, SD 97196'

fake.building_number()
# '598'

fake.city()
# 'Spörriland'

fake.city_prefix()
# 'North'

fake.city_suffix()
# 'chester'

fake.country()
# 'Germany'

fake.country_code(representation="alpha-2")
# 'RW'

fake.military_apo()
# 'PSC 0613, Box 1320'

fake.military_dpo()
# 'Unit 4568 Box 2816'

fake.military_ship()
# 'USNS'

fake.military_state()
# 'AA'

fake.postalcode()
# '48182'

fake.postalcode_in_state(state_abbr=None)
# '03276'

fake.postalcode_plus4()
# '72370-4914'

fake.postcode()
# '38414'

fake.postcode_in_state(state_abbr=None)
# '58431'

fake.secondary_address()
# 'Apt. 689'

fake.state()
# 'California'

fake.state_abbr(include_territories=True)
# 'OK'

fake.street_address()
# '274 Elmar Highway Suite 569'

fake.street_name()
# 'Klaus Burgs'

fake.street_suffix()
# 'Heights'

fake.zipcode()
# '65743'

fake.zipcode_in_state(state_abbr=None)
# '87832'

fake.zipcode_plus4()
# '05156-3228'
faker.providers.automotive
fake.license_plate()
# '5DB 889'
faker.providers.bank
fake.bank_country()
# 'GB'

fake.bban()
# 'FMXX17274103845527'

fake.iban()
# 'GB41MGRU96285896790265'
faker.providers.barcode
fake.ean(length=13)
# '4403882661561'

fake.ean13(leading_zero=None)
# '4449025236036'

fake.ean8()
# '21556203'

fake.upc_a(upc_ae_mode=False, base=None, number_system_digit=None)
# '345211743521'

fake.upc_e(base=None, number_system_digit=None, safe_mode=True)
# '15818025'
faker.providers.color
fake.color(hue=None, luminosity=None, color_format="hex")
# '#aefce3'

fake.color_name()
# 'SandyBrown'

fake.hex_color()
# '#88345b'

fake.rgb_color()
# '195,175,162'

fake.rgb_css_color()
# 'rgb(233,119,236)'

fake.safe_color_name()
# 'aqua'

fake.safe_hex_color()
# '#ff7700'
faker.providers.company
fake.bs()
# 'syndicate clicks-and-mortar supply-chains'

fake.catch_phrase()
# 'Optimized optimizing methodology'

fake.company()
# 'Hartmann, Keller and Fankhauser'

fake.company_suffix()
# 'Ltd'
faker.providers.credit_card
fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
# '06/26'

fake.credit_card_full(card_type=None)
# 'Maestro\nAna Kägi\n503858341301 10/22\nCVV: 993\n'

fake.credit_card_number(card_type=None)
# '4892615556939'

fake.credit_card_provider(card_type=None)
# 'VISA 16 digit'

fake.credit_card_security_code(card_type=None)
# '113'
faker.providers.currency
fake.cryptocurrency()
# ('XRP', 'Ripple')

fake.cryptocurrency_code()
# 'XDN'

fake.cryptocurrency_name()
# 'Dash'

fake.currency()
# ('CNY', 'Renminbi')

fake.currency_code()
# 'BWP'

fake.currency_name()
# 'Swazi lilangeni'
faker.providers.date_time
fake.am_pm()
# 'PM'

fake.century()
# 'XV'

fake.date(pattern="%Y-%m-%d", end_datetime=None)
# '1972-11-24'

fake.date_between(start_date="-30y", end_date="today")
# datetime.date(2005, 12, 16)

fake.date_between_dates(date_start=None, date_end=None)
# datetime.date(2019, 12, 10)

fake.date_object(end_datetime=None)
# datetime.date(2011, 11, 10)

fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)
# datetime.date(1950, 12, 23)

fake.date_this_century(before_today=True, after_today=False)
# datetime.date(2008, 11, 10)

fake.date_this_decade(before_today=True, after_today=False)
# datetime.date(2017, 9, 16)

fake.date_this_month(before_today=True, after_today=False)
# datetime.date(2019, 12, 7)

fake.date_this_year(before_today=True, after_today=False)
# datetime.date(2019, 2, 20)

fake.date_time(tzinfo=None, end_datetime=None)
# datetime.datetime(2006, 5, 22, 16, 10, 23)

fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)
# datetime.datetime(966, 9, 24, 11, 39, 9)

fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)
# datetime.datetime(1999, 5, 7, 8, 58, 24)

fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
# datetime.datetime(2019, 12, 10, 15, 12, 33)

fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2008, 4, 21, 15, 25, 45)

fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2016, 12, 12, 14, 26, 40)

fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2019, 12, 4, 13, 34, 54)

fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2019, 6, 23, 21, 6, 59)

fake.day_of_month()
# '26'

fake.day_of_week()
# 'Saturday'

fake.future_date(end_date="+30d", tzinfo=None)
# datetime.date(2020, 1, 7)

fake.future_datetime(end_date="+30d", tzinfo=None)
# datetime.datetime(2019, 12, 23, 15, 24, 54)

fake.iso8601(tzinfo=None, end_datetime=None)
# '2010-08-15T00:28:40'

fake.month()
# '10'

fake.month_name()
# 'September'

fake.past_date(start_date="-30d", tzinfo=None)
# datetime.date(2019, 11, 28)

fake.past_datetime(start_date="-30d", tzinfo=None)
# datetime.datetime(2019, 11, 18, 19, 38, 10)

fake.time(pattern="%H:%M:%S", end_datetime=None)
# '11:11:15'

fake.time_delta(end_datetime=None)
# datetime.timedelta(0)

fake.time_object(end_datetime=None)
# datetime.time(0, 5, 38)

fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None)
# <generator object Provider.time_series at 0x7f529b735c78>

fake.timezone()
# 'Asia/Dubai'

fake.unix_time(end_datetime=None, start_datetime=None)
# 1058973020

fake.year()
# '1993'
faker.providers.file
fake.file_extension(category=None)
# 'webm'

fake.file_name(category=None, extension=None)
# 'est.html'

fake.file_path(depth=1, category=None, extension=None)
# '/officiis/debitis.js'

fake.mime_type(category=None)
# 'model/x3d+binary'

fake.unix_device(prefix=None)
# '/dev/xvdn'

fake.unix_partition(prefix=None)
# '/dev/sdx2'
faker.providers.geo
fake.coordinate(center=None, radius=0.001)
# Decimal('-8.656935')

fake.latitude()
# Decimal('-19.9183895')

fake.latlng()
# (Decimal('21.102877'), Decimal('-154.453381'))

fake.local_latlng(country_code="US", coords_only=False)
# ('38.96372', '-76.99081', 'Chillum', 'US', 'America/New_York')

fake.location_on_land(coords_only=False)
# ('43.78956', '7.60872', 'Ventimiglia', 'IT', 'Europe/Rome')

fake.longitude()
# Decimal('-131.868665')
faker.providers.internet
fake.ascii_company_email(*args, **kwargs)
# 'andreia73@leu-isler.com'

fake.ascii_email(*args, **kwargs)
# 'rmarti@yahoo.com'

fake.ascii_free_email(*args, **kwargs)
# 'itenjakub@hotmail.com'

fake.ascii_safe_email(*args, **kwargs)
# 'tiziano54@example.org'

fake.company_email(*args, **kwargs)
# 'jochen32@schurch.org'

fake.domain_name(*args, **kwargs)
# 'schweizer.com'

fake.domain_word(*args, **kwargs)
# 'graf'

fake.email(*args, **kwargs)
# 'sutergabriele@forster-roos.net'

fake.free_email(*args, **kwargs)
# 'jwegmann@yahoo.com'

fake.free_email_domain(*args, **kwargs)
# 'hotmail.com'

fake.hostname(*args, **kwargs)
# 'db-44.schnyder-wegmann.com'

fake.image_url(width=None, height=None)
# 'https://placeimg.com/131/509/any'

fake.ipv4(network=False, address_class=None, private=None)
# '188.58.246.154'

fake.ipv4_network_class()
# 'c'

fake.ipv4_private(network=False, address_class=None)
# '10.252.133.176'

fake.ipv4_public(network=False, address_class=None)
# '79.105.38.113'

fake.ipv6(network=False)
# '5876:aacb:5942:820f:cc31:93a3:763:4976'

fake.mac_address()
# '5d:88:2e:de:ea:66'

fake.safe_email(*args, **kwargs)
# 'fischeraziz@example.net'

fake.slug(*args, **kwargs)
# 'perferendis-odio'

fake.tld()
# 'org'

fake.uri()
# 'http://www.stettler.com/home.htm'

fake.uri_extension()
# '.html'

fake.uri_page()
# 'category'

fake.uri_path(deep=None)
# 'explore/list'

fake.url(schemes=None)
# 'http://www.muller.info/'

fake.user_name(*args, **kwargs)
# 'agnieszkavogt'
faker.providers.isbn
fake.isbn10(separator="-")
# '1-78167-873-1'

fake.isbn13(separator="-")
# '978-1-01-501647-7'
faker.providers.job
fake.job()
# 'Customer service manager'
faker.providers.lorem
fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
# ('Ipsa magnam quibusdam error sapiente tenetur. Eveniet molestiae repudiandae '
#  'impedit facere alias.')

fake.paragraphs(nb=3, ext_word_list=None)
# [   'Accusantium quisquam itaque quibusdam consequuntur. Error eius '
#     'repellendus minus minus. Magni ipsum cum aperiam facilis iure.',
#     'Illo facere inventore autem odit similique. Modi qui incidunt at. Facere '
#     'repellendus quis neque in.',
#     'Odit perferendis architecto. Ullam corrupti reprehenderit voluptatum '
#     'nesciunt velit. Fugiat accusantium eligendi ea nostrum.']

fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
# 'Et vitae tenetur similique.'

fake.sentences(nb=3, ext_word_list=None)
# [   'Itaque magnam esse nemo.',
#     'Explicabo perferendis minima molestias dolores architecto dolor incidunt.',
#     'Laudantium vero dolore.']

fake.text(max_nb_chars=200, ext_word_list=None)
# ('Quod ratione voluptates est aut. Voluptatum sint ducimus atque vel '
#  'laboriosam reiciendis.')

fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
# [   'Totam rem aliquam totam itaque consequuntur reprehenderit quis. Corporis '
#     'sequi aut occaecati qui unde. Incidunt possimus quo architecto.\n'
#     'Fugit ut et necessitatibus reiciendis unde natus.',
#     'Non quo assumenda. Tenetur accusantium nam earum magnam excepturi ipsam. '
#     'Ab earum architecto tenetur animi impedit deleniti. Officia consequuntur '
#     'laborum sed accusantium unde.\n'
#     'Non dolore eum.',
#     'Distinctio culpa distinctio quam fuga. Doloremque porro nobis sint '
#     'libero.\n'
#     'Modi temporibus aut eveniet possimus dolorum voluptatem cumque. Aliquam '
#     'cum illo eos.']

fake.word(ext_word_list=None)
# 'ad'

fake.words(nb=3, ext_word_list=None, unique=False)
# ['dolores', 'culpa', 'quo']
"""
