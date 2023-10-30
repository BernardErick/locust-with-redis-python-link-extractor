from locust import HttpUser, between, task
import argparse

class WebsiteUser(HttpUser):
    host = "http://localhost"
    wait_time = between(1, 5)
    urls_to_extract = [
        "https://brazino777.com/pt/",
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.twitter.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org",
    ]
    @task
    def extract_links(self):
        for id in range(10):
            url = self.urls_to_extract[id]
            self.client.get(f"/?url={url}")
        
    def on_stop(self):
        # Este método será chamado quando o teste de carga terminar
        import os

        # Verifique se o arquivo "results_stats.csv" existe na raiz do projeto
        if os.path.exists("results_stats.csv"):
            num_users = str(self.environment.parsed_options.num_users)
            csv_name = num_users + "_users_for_results_stats.csv"
            os.rename("results_stats.csv", csv_name)