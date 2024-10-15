from src.client_analytics.adesa.adesa import ADESAAnalytics

if __name__ == "__main__":
    client_factory = {
        "ADESA": ADESAAnalytics(input_fn="/Users/komalpawar/Downloads/adesa.csv", client="ADESA")
    }
    client = "ADESA"
    client_factory[client].perform_analytics()
