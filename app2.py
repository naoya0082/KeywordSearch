# 使えそうだったので講義内のコードをコピー
import requests


class AddressSearcher:
    def __init__(self):
        self.base_url = f"http://zipcloud.ibsnet.co.jp/api/search"  # apiのアドレス

    def search(self, postal_code):
        url = f"{self.base_url}?zipcode={postal_code}"
        response = requests.get(url)
        response_dict = response.json()

        if response_dict["results"] is None:
            return "該当するデータは見つかりませんでした。"

        return self.location(response_dict)
