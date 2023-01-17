from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls.checkboxes import Checkboxes
from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.radiobutton import Radiobutton
from demoqa_tests.utils import path_to_file, date_config, ads

class PracticeForm:
    def __init__(self, user):
        self.user = user

    def open_page(self):
        browser.open('/automation-practice-form')
        ads.remove_ads(amount=3, timeout=6)

    def fill_name(self):
        browser.element('#firstName').type(self.user.first_name)
        browser.element('#lastName').type(self.user.last_name)

    def fill_contacts(self):
        browser.element('#userEmail').type(self.user.email)
        browser.element('#userNumber').type(self.user.phone)

    def select_gender(self):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_by_value(self.user.gender)

    def select_birthday(self):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set_date(self.user.birthday)

    def input_subject(self):
        browser.element('#subjectsInput').type(self.user.subject).press_enter()

    def select_hobbies(self):
        check_hobbies = Checkboxes(browser.all('[for^=hobbies-checkbox]'))
        check_hobbies.select(self.user.hobbies)

    def upload_image(self):
        relative_path = 'resources/photo.png'
        path = path_to_file.create_path(relative_path)
        browser.element('#uploadPicture').set_value(path)

    def input_address(self):
        browser.element('#currentAddress').type(self.user.address)

    def select_state(self):
        dropdown = Dropdown('#state')
        dropdown.select(self.user.state)

    def select_city(self):
        dropdown = Dropdown('#city')
        dropdown.select(self.user.city)

    def submit(self):
        browser.element('#submit').press_enter()

    def scroll_to_bottom(self):
        browser.element('#state').perform(command.js.scroll_into_view)

    def submit_form(self):
        self.open_page()
        self.fill_name()
        self.fill_contacts()
        self.select_gender()
        self.select_birthday()
        self.input_subject()
        self.select_hobbies()
        self.upload_image()
        self.input_address()
        self.scroll_to_bottom()
        self.select_state()
        self.select_city()
        self.submit()
        return self

    def should_have_submitted(self):
        #browser.element('.table').all('td').even.should(have.texts(
        browser.all('tbody tr td:last-child').should(have.exact_texts(
            self.user.first_name + ' ' + self.user.last_name,
            self.user.email,
            self.user.gender,
            self.user.phone,
            self.user.birthday.strftime(date_config.datetime_view_format),
            self.user.subject,
            self.user.hobbies,
            self.user.image,
            self.user.address,
            self.user.state + ' ' + self.user.city))
        return self
