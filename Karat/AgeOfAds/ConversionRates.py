'''The people who buy ads on our network don't have enough data about how ads are working for their business. They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page after clicking one of their ads:

# Each user completed 1 purchase.
completed_purchase_user_ids = [
	"3123122444","234111110", "8321125440", "99911063"]

And our ops team provided us with some raw log data from our ad server showing every time a user clicked on one of our ads:

ad_clicks = [
	#"IP_Address,Time,Ad_Text",
	"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
	"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
	"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
	"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
	"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
	"122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
	"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

The client also sent over the IP addresses of all their users.

all_user_ips = [
	#"User_ID,IP_Address",
	"2339985511,122.121.0.155",
	"234111110,122.121.0.1",
	"3123122444,92.130.6.145",
	"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
	"8321125440,82.1.106.8",
	"99911063,92.130.6.144"
]

Write a function to parse this data, determine how many times each ad was clicked, then return the ad text, that ad's number of clicks, and how many of those ad clicks were from users who made a purchase.

Expected output:

1 of 2	 2017 Pet Mittens
0 of 1	 The Best Hollywood Coats
3 of 4	 Buy wool coats for your pets

purchases: number of purchase IDs
clicks: number of ad clicks
ips: number of IP addresses'''

def parse_ad_data(completed_purchase_user_ids, ad_clicks, all_user_ips):
    clicks_by_ad = {}
    for ad in ad_clicks:
        ad_text = ad.split(',')[2]
        if ad_text not in clicks_by_ad:
            clicks_by_ad[ad_text] = 0
        clicks_by_ad[ad_text] += 1
    
    user_ips = {}
    for user_ip in all_user_ips:
        user_id, ip = user_ip.split(',')
        user_ips[user_id] = ip
    
    purchases_by_ad = {}
    for purchase_id in completed_purchase_user_ids:
        if purchase_id not in user_ips:
            continue
        ip = user_ips[purchase_id]
        for ad in ad_clicks:
            ad_text, ip_address = ad.split(',')[2], ad.split(',')[0]
            if ip == ip_address:
                if ad_text not in purchases_by_ad:
                    purchases_by_ad[ad_text] = 0
                purchases_by_ad[ad_text] += 1
                break
    
    results = []
    for ad_text, clicks in clicks_by_ad.items():
        purchases = purchases_by_ad.get(ad_text, 0)
        result = f"{purchases} of {clicks} {ad_text}"
        results.append(result)
    
    return results

completed_purchase_user_ids = [
    "3123122444","234111110", "8321125440", "99911063"
]

ad_clicks = [
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
	"99911063,92.130.6.144"
]
ans = parse_ad_data(completed_purchase_user_ids, ad_clicks, all_user_ips)
for item in ans:
    print(item)