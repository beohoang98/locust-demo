from locust import HttpUser, between, task

class TestProject(HttpUser):
    host = "https://kcpm-nhom09-project.herokuapp.com"
    wait_time = between(5, 10) # in seconds

    @task
    def homepage(self):
        self.client.get("/")

    @task
    def search_page(self):
        self.client.get("/shoes-stall.html")
