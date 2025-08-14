# Testing Instructions for Subway Config

## Prerequisites
- SilverBullet software installed and configured
- Valid proxy list (required due to Subway's bot protection)
- Test credentials: `james21trill@icloud.com:Easypass1!`

## Testing Steps

### 1. Validate Config Structure
```bash
python3 test-subway-config.py
```

### 2. Load Config in SilverBullet
1. Open SilverBullet
2. Load the `subway-2025.loli` config file
3. Configure proxy settings (required - set to rotate proxies)
4. Set bot count to 1-5 for initial testing

### 3. Prepare Test Data
Create a wordlist file with the test credential:
```
james21trill@icloud.com:Easypass1!
```

### 4. Run Test
1. Load the wordlist in SilverBullet
2. Start the checking process
3. Monitor for the following scenarios:

#### Expected Success Output
```
[HIT][proxy_ip] james21trill@icloud.com:Easypass1! - [MVP Points: 1250][Rewards Balance: $5.00][Tier Status: Gold][Free Subs: 2][Points Expiry: 2025-12-31]
```

#### Potential Issues and Solutions

**CAPTCHA Challenge**
- If reCAPTCHA appears, the config includes an empty `g-recaptcha-response` field
- SilverBullet should handle this automatically with proper CAPTCHA solving services
- If manual intervention needed, contact user for assistance

**2FA Required**
- If 2FA is triggered, the login will fail at the main login step
- Contact user immediately to confirm 2FA code from their email
- May need to implement 2FA bypass or manual intervention workflow

**Challenge Validation Page**
- If you see "Challenge Validation" page instead of login, this is Subway's bot protection
- The config now includes a challenge validation block with 5-second delay
- May need to adjust delay timing based on challenge complexity

**Access Denied / Rate Limiting**
- Increase proxy rotation frequency
- Reduce bot count
- Add delays between requests

**Invalid Session Tokens**
- The config uses placeholder tokens that should be dynamically captured
- Verify that CSRF tokens are being properly extracted from the initial session setup

### 5. Validation Checklist
- [ ] Config loads without syntax errors
- [ ] Session establishment succeeds (Block 1)
- [ ] Email validation returns success (Block 2)  
- [ ] Main login completes without 2FA (Block 3)
- [ ] Rewards status verification succeeds (Block 4)
- [ ] Account data retrieval captures all fields (Block 5)
- [ ] All capture rules extract data properly

## Troubleshooting

### Common Error Patterns
- `403 Forbidden` - Bot detection triggered, need better proxies
- `429 Too Many Requests` - Rate limiting, reduce bot count
- `Invalid CSRF token` - Session setup failed, check initial request
- `Authentication failed` - Credentials invalid or 2FA required
- `Rewards not found` - Account may not be enrolled in MVP program

### Debug Mode
Enable verbose logging in SilverBullet to see detailed request/response data for troubleshooting.

## Security Notes
- Always use high-quality residential proxies
- Rotate User-Agent strings if detection increases
- Monitor for new anti-bot measures on Subway's website
- Keep config updated with latest security headers and patterns
