from allure_commons.types import Severity

from demoqa_tests.model.data.user import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm
import allure


@allure.tag("UI test")
@allure.severity(Severity.CRITICAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.label("owner", "OAO")
@allure.description("Verify registration process is successful")
def test_registration_user():

    # GIVEN
    with allure.step('Init Form'):
        practice_form = PracticeForm(test_user)

    # WHEN
    with allure.step('Enter users\'s registration data and send form'):
        practice_form.submit_form()

    # THEN
    with allure.step('Verify all sent data correctly submitted'):
        practice_form.should_have_submitted()
