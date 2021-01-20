from api import _Api

HEADER ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
                 'YaBrowser/20.11.3.179 Yowser/2.5 Safari/537.36'
}

class Api(_Api):
    def __init__(self):
        super().__init__('CryptonatorApi')

    def _update_rate(self, xrate):
        rate = self._get_api_rate(xrate.from_currency, xrate.to_currency)
        return rate

    def _get_api_rate(self, from_currency, to_currency):
        aliases_map = {1000: "btc", 980: "uah", 643: "rub"}

        if from_currency not in aliases_map:
            raise ValueError(f"Invalid from_currency: {from_currency}")

        if to_currency not in aliases_map:
            raise ValueError(f"Invalid to_currency: {to_currency}")

        url_end = f"{aliases_map[from_currency]}-{aliases_map[to_currency]}"
        url = f"https://api.cryptonator.com/api/ticker/{url_end}"
        response = self._send_request(url=url, method="get", headers=HEADER)
        response_json = response.json()
        self.log.debug("Cryptonator response: %s" % response_json)
        rate = self._find_rate(response_json)

        return rate

    def _find_rate(self, response_data):
        if "ticker" not in response_data:
            raise ValueError(f"Invalid cryptonator response: ticker not set")

        if "price" not in response_data["ticker"]:
            raise ValueError(f"Invalid cryptonator response: ticker.price not set")

        return float(response_data["ticker"]["price"])
