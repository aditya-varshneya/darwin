import config_run
import attendance_pool
url ='https://thbhrms.darwinbox.in/user/login'


def test_clock_in():
    attendance_pool.Testlogin().test_setup(url)
    attendance_pool.Testlogin().test_login(username=config_run.cred['username'],password=config_run.cred['password'])
    attendance_pool.attendance().clock_in()
