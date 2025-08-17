# Testing Instructions for HBO Max Config

## Prerequisites
- SilverBullet software installed and configured
- Valid proxy list (required due to geo-restrictions and streaming service protection)
- Valid HBO Max subscription credentials for testing

## Testing Steps

### 1. Validate Config Structure
```bash
python3 test-hbomax-config.py
```

### 2. Load Config in SilverBullet
1. Open SilverBullet
2. Load the `hbomax-2025.loli` config file
3. Configure proxy settings (required - set to rotate proxies)
4. Set bot count to 1-5 for initial testing

### 3. Prepare Test Data
Create a wordlist file with valid HBO Max credentials:
```
user@example.com:password123
```

### 4. Run Test
1. Load the wordlist in SilverBullet
2. Start the checking process
3. Monitor for the following scenarios:

#### Expected Success Output
```
[HIT][proxy_ip] user@example.com:password123 - [User ID: 12345][Email: user@example.com][Name: John Doe][Subscription Status: active][Subscription Tier: premium][Expiry Date: 2025-12-31][Billing Cycle: monthly]
```

#### Potential Issues and Solutions

**Geo-Restrictions**
- HBO Max is only available in certain regions (primarily US)
- Use high-quality US residential proxies
- If getting geo-blocked, try different proxy providers

**Invalid Credentials**
- The config will detect "Invalid credentials" or "Authentication failed" responses
- Ensure test credentials are valid and active HBO Max accounts
- Check if account requires 2FA (not currently supported in config)

**Rate Limiting**
- HBO Max may implement rate limiting on authentication endpoints
- Reduce bot count if getting 429 responses
- Increase delays between requests
- Use proxy rotation more aggressively

**API Changes**
- The config is based on 2018 reverse engineering research
- HBO Max has since rebranded to "Max" and may have updated endpoints
- If authentication fails, endpoints may need updating:
  - `comet.api.hbo.com` might have changed
  - Authentication flow might have been modified
  - Additional security measures may have been added

**Token Expiration**
- Access tokens have limited lifetime (check `expires_in` field)
- Config captures tokens but doesn't handle refresh
- For extended sessions, token refresh logic would be needed

### 5. Validation Checklist
- [ ] Config loads without syntax errors
- [ ] Session establishment succeeds (Block 1)
- [ ] Authentication request completes (Block 2)
- [ ] Access token is captured successfully
- [ ] User profile data retrieval succeeds (Block 3)
- [ ] Subscription data retrieval succeeds (Block 4)
- [ ] All capture rules extract data properly

## Troubleshooting

### Common Error Patterns
- `403 Forbidden` - Geo-restriction or bot detection
- `401 Unauthorized` - Invalid credentials or expired tokens
- `429 Too Many Requests` - Rate limiting, reduce bot count
- `404 Not Found` - API endpoint may have changed
- `Connection timeout` - Proxy issues or service unavailable

### Debug Mode
Enable verbose logging in SilverBullet to see detailed request/response data for troubleshooting.

## Security Notes
- Always use high-quality residential proxies (preferably US-based)
- HBO Max/Max has sophisticated fraud detection systems
- Monitor for new anti-bot measures and API changes
- The service has been rebranded to "Max" so endpoints may have changed
- Consider that this config is based on 2018 research and may need updates

## Important Disclaimers
- This config is for educational/security testing purposes only
- Ensure compliance with HBO Max/Max terms of service
- Only test with accounts you own or have explicit permission to test
- Be aware that HBO Max has rebranded to "Max" and API endpoints may have changed
- The reverse engineering research this config is based on is from 2018
