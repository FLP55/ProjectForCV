class MainURL:
    @staticmethod
    def get_url_from_dict(key: str) -> str:
        all_url = {"base_url": "https://dev-api.jointml.ru"}
        return all_url[key]
