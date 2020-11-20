from locust import between, task
from config.urls import Pages, BASE_URL
from config.users import users
from locust_plugins.users import HttpUserWithResources
from random import choice

class AnonymousTest(HttpUserWithResources):
    wait_time = between(3, 5)
    host = BASE_URL
    
    def on_start(self):
        (email, password) = choice(users)

        self.client.post(Pages.Login, data = {
            "email": email,
            "password": password
        })

    @task
    def home(self):
        self.client.get(Pages.Home)

    @task
    def products_list(self):
        self.client.get(Pages.ShoesHome)

    @task
    def products_list_with_sort(self):
        self.client.get(Pages.ShoesHome + "?sort=-1")
