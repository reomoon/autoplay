# Pages/front login
class Login:
    def __init__(self, page):
        # page 객체를 받아서 self.page에 저장
        self.page = page 
        
        # 로그인 요소 정의
        self.signin_link = page.locator('a.header_signIn')
        self.username_input = page.locator('input[name="userName"]')
        self.password_input = page.locator('input[name="password"]')
        self.signin_button = page.locator('#btn-signin')

    def login(self, username, password):
        # 로그인 동작 수행
        self.signin_link.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signin_button.click()



        





