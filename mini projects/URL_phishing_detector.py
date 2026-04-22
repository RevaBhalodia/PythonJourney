def is_phishing(url):
    suspicious_keywords = ["login", "verify", "bank", "secure"]
    
    if "https" not in url:
        return True
    if any(word in url for word in suspicious_keywords):
        return True
    if url.count('.') > 3:
        return True

    return False

print(is_phishing("http://secure-login-bank.com"))