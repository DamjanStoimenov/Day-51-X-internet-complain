from internet import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot(driver_path="/Users/Darko/PycharmProjects/Day-51-X internet complain/drivers/chromedriver")
bot.get_internet_speed()
bot.tweet_at_provider()