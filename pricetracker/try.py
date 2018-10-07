from mailchimp3 import MailChimp
from mailchimp import Mailchimp

api_key = "f64ade9b515e78990f880188e670d9b0-us19"
username = "aakash21696"
# client = MailChimp(mc_api = api_key, mc_user = username)
# all_campaigns = client.campaigns.all(get_all = True)
campaign_id = "9ed1e00b7f"
mailchimp = Mailchimp(api_key)
mailchimp.campaigns.send(campaign_id)
