from selenium.webdriver.common.by import By

MAIN_PAGE_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header")]')

HEADER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')

SECTION_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")/button[text()="Заказать"]')

QUESTION = (By.ID, 'accordion__heading-{}')

ANSWER = (By.ID, '//div[@id="accordion__panel-{}"]/p')
