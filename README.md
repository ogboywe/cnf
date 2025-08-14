# Retail Config Collection

This repository contains updated credential checking configurations for major retail websites.

## Files

- `kohls-2025.loli` - Updated Kohl's configuration for 2025 with modern anti-detection measures
- `bathandbodyworks-2025.loli` - Bath & Body Works configuration for 2025 with 4-block authentication flow

## Key Updates in 2025 Versions

### Kohl's Config (`kohls-2025.loli`)
#### Security Enhancements
- **reCAPTCHA v3 Integration**: Site key `6Lc3os0pAAAAAKiF-Dir9Hcx05bqFOnTbXCYqLbs`
- **Enhanced Bot Detection**: 65+ scripts for detection vs simpler 2023 approach
- **Advanced Fingerprinting**: Updated `nds-pmd` parameter with current browser signatures

#### Technical Improvements
- **Modern Browser Simulation**: Updated User-Agent to Chrome 131.0.0.0
- **Current Cookie Structure**: Extensive session management cookies
- **Updated Headers**: Modern Accept headers and referrer policies
- **2025 Timestamp**: LastModified updated to current date

#### Compatibility Notes
- The `g-recaptcha-response` parameter is included but will need to be populated by the credential testing system
- The `nds-pmd` parameter contains encoded fingerprinting data that matches current browser signatures
- Extensive cookie string captured from live 2025 Kohl's session

### Bath & Body Works Config (`bathandbodyworks-2025.loli`)
#### Multi-Block Authentication Flow
- **Key Check Block**: GET request to login page for session establishment
- **Email Verification Block**: POST to validate email exists before login attempt
- **Main Login Block**: POST with credentials and comprehensive anti-detection measures
- **Account Info Block**: GET to retrieve rewards balance and member tier information

#### Security Features
- **PerimeterX Bot Protection**: Handles advanced bot detection system
- **Modern Chrome 131 Simulation**: Current User-Agent and browser fingerprinting
- **Comprehensive Cookie Management**: Session, tracking, and authentication cookies
- **CSRF Token Handling**: Dynamic token extraction and submission
- **reCAPTCHA Integration**: Prepared for reCAPTCHA challenges

#### Capture Capabilities
- **Rewards Balance**: Extracts current rewards dollar amount
- **Points Balance**: Captures loyalty points total
- **Member Tier**: Identifies membership level (regular, VIP, etc.)

## Usage

This configuration is designed for educational and security research purposes only. Users must comply with all applicable terms of service and legal requirements.

## Version History

### Kohl's
- **v2.0.0 [2025]** - Complete modernization for 2025 standards
- **v1.1.2 [2023]** - Original version (deprecated)

### Bath & Body Works
- **v1.0.0 [2025]** - Initial release with 4-block authentication flow and modern anti-detection
