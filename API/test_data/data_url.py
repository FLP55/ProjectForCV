class MainURL:
    @staticmethod
    def get_url_from_dict(key: str) -> str:
        all_url = {"base_url": "http://172.17.1.27:8000"}
        return all_url[key]
