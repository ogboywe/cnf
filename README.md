# Kohl's Config Collection

This repository contains updated credential checking configurations for Kohl's retail website.

## Files

- `kohls-2025.loli` - Updated configuration for 2025 with modern anti-detection measures

## Key Updates in 2025 Version

### Security Enhancements
- **reCAPTCHA v3 Integration**: Site key `6Lc3os0pAAAAAKiF-Dir9Hcx05bqFOnTbXCYqLbs`
- **Enhanced Bot Detection**: 65+ scripts for detection vs simpler 2023 approach
- **Advanced Fingerprinting**: Updated `nds-pmd` parameter with current browser signatures

### Technical Improvements
- **Modern Browser Simulation**: Updated User-Agent to Chrome 131.0.0.0
- **Current Cookie Structure**: Extensive session management cookies
- **Updated Headers**: Modern Accept headers and referrer policies
- **2025 Timestamp**: LastModified updated to current date

### Compatibility Notes
- The `g-recaptcha-response` parameter is included but will need to be populated by the credential testing system
- The `nds-pmd` parameter contains encoded fingerprinting data that matches current browser signatures
- Extensive cookie string captured from live 2025 Kohl's session

## Usage

This configuration is designed for educational and security research purposes only. Users must comply with all applicable terms of service and legal requirements.

## Version History

- **v2.0.0 [2025]** - Complete modernization for 2025 standards
- **v1.1.2 [2023]** - Original version (deprecated)
