# COVID-19 Vaccination Semi-auto Slot Booking Script
## Update:
### **We are getting all kinds of attention now - which I do not want to handle. So there won't be any additional commits to this project. It has been put on indefinite hold.**



### Important: 
- This is a proof of concept project. I do NOT endorse or condone, in any shape or form, automating any monitoring/booking tasks. **Use at your own risk.**
- This CANNOT book slots automatically. It doesn't skip any of the steps that a normal user would have to take on the official portal. You will still have to enter the OTP and Captcha.
- Do NOT use unless all the beneficiaries selected are supposed to get the same vaccine and dose. 
- There is no option to register new mobile or add beneficiaries. This can be used only after beneficiary has been added through the official app/site.
- API Details (read the first paragraph at least): https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2
- BMC Link: https://www.buymeacoffee.com/pallupz
- And finally, I know code quality isn't great. Suggestions are welcome.

### Noteworthy Forks
- https://github.com/bombardier-gif/covid-vaccine-booking : I haven't tried this personally but, it looks like a promising, completely automated solution that would require a bit more setting up.

### Usage:


Step to install Airmore : https://medium.com/@erayerdin/send-sms-with-python-eab7a5854d3a (Android)

To keep screen on : https://play.google.com/store/apps/details?id=moe.zhs.caffeine&hl=en_IN&gl=US (Andriod)

Replace the IP in read_sms.py with the one in Airmore

Use **Python 3.7** and install all the dependencies with:
```
sudo apt-get install python3-gi

sudo apt-get install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev

pip install -r requirements.txt
