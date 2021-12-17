from brownie import accounts, MoodDiary, config


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    mood = MoodDiary.deploy({"from": account})
    print(f"MoodDiary contract address: {mood.address}")


def main():
    deploy()
