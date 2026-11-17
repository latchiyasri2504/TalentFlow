
def send_otp(channel: str, destination: str, otp: str):
    if channel not in ["email", "whatsapp", "browser"]:
        raise ValueError("Unsupported OTP channel")

    # Development mode: display OTP in the VS Code terminal.
    print("========== TALENTFLOW OTP ==========")
    print(f"Channel: {channel}")
    print(f"Destination: {destination}")
    print(f"OTP: {otp}")
    print("====================================")

    return True
