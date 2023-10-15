
import capsolver

# Consider using environment variables for sensitive information
PROXY = "http://username:password@ip:port"
capsolver.api_key = "capsolver.com key"

def solve_recaptcha_v2():
    solution = capsolver.solve({
        "type": "ReCaptchaV2Task",
        "websiteURL": "https://www.google.com",
        "websiteKey": "6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b",
        "enterprisePayload": {
            "s": "Keep getting this value, as it's different each time."
        },
        "proxy": PROXY
    })
    return solution



def main():

    print("Solving reCaptcha v2")
    solution = solve_recaptcha_v2()
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
