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
james21trill@icloud.com:Easypass1!
user@example.com:password123
```

### 4. Run Test
1. Load the wordlist in SilverBullet
2. Start the checking process
3. Monitor for the following scenarios:

**Multi-Step Authentication Flow:**
The config now implements the complete HBO Max authentication flow discovered through network monitoring:
1. **Credential Submission**: POST to `https://auth.hbomax.com/login` with email/password
2. **Session Bootstrap**: GET to `/session-context/headwaiter/v1/bootstrap` to establish request context
3. **Token Acquisition**: GET to `/token?realm=bolt` with proper session context
4. **Data Capture**: Retrieve user profile and subscription information

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
- The config has been updated with current 2025 API endpoints discovered through network monitoring of successful HBO Max authentication
- HBO Max now uses multiple API subdomains: `default.any-any.prd.api.hbomax.com` and `default.beam-amer.prd.api.hbomax.com`
- **Multi-step authentication flow implemented:**
  1. Credential submission: `https://auth.hbomax.com/login` (POST with email/password)
  2. Session bootstrap: `https://default.any-any.prd.api.hbomax.com/session-context/headwaiter/v1/bootstrap` (GET)
  3. Token acquisition: `https://default.any-any.prd.api.hbomax.com/token?realm=bolt` (GET)
- User profile endpoint: `https://default.beam-amer.prd.api.hbomax.com/users/me`
- Subscription/entitlements endpoint: `https://default.any-any.prd.api.hbomax.com/entitlements/userEntitlementsSummary/me`
- Authentication flow uses session-based authentication followed by token-based API access
- All endpoints discovered through real network monitoring during successful login with valid credentials

**Token Expiration**
- Access tokens have limited lifetime (check `expires_in` field)
- Config captures tokens but doesn't handle refresh
- For extended sessions, token refresh logic would be needed

### 5. Validation Checklist
- [ ] Config loads without syntax errors
- [ ] Credential submission succeeds (Block 1: POST to auth.hbomax.com/login)
- [ ] Session bootstrap succeeds (Block 2: GET to session-context/headwaiter/v1/bootstrap)
- [ ] Token acquisition succeeds (Block 3: GET to token?realm=bolt)
- [ ] Access token is captured successfully
- [ ] User profile data retrieval succeeds (Block 4: GET to users/me)
- [ ] Subscription data retrieval succeeds (Block 5: GET to entitlements/userEntitlementsSummary/me)
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
- The config has been updated with current 2025 API endpoints discovered through network monitoring
- API endpoints have been updated from deprecated `comet.api.hbo.com` to current multi-step authentication flow
- **Authentication Flow**: The config now implements the complete credential submission → session bootstrap → token acquisition sequence discovered through network monitoring of successful HBO Max authentication
