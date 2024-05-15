from selene import browser, be, have


def test_test3():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Gustavo')
    browser.element('[id="lastName"]').type('Krasavo')
    browser.element('[id="userEmail"]').type('gustavo@gmail.com')
    browser.element('[id="gender-radio-1"]').press()
    browser.element('[id="userNumber"]').type(2342342342)
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[aria-label="Choose Wednesday, May 15th, 2024"]').click()
    browser.element('[id="subjectInput"]').type('English')
