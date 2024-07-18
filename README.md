##  📖 Table Of Contents
- About
- How to Build
- Documentation
- Code explanation
- Feedback and Contributions
- Contacts

## 🚀 About
The LinkedIn Job Application Bot is an automated script designed to apply for a job on LinkedIn. The bot uses Selenium to interact with the LinkedIn job application page, automatically filling in the necessary details and submitting the application.

## 📝 How to Build
**Prerequisites**
  - Python 3.x
  - selenium library
  - Webdriver

**To build the project follow these steps:**
  - **installation:**
```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed
            
# Clone the repository
git clone https://github.com/Akwaowo91/Automating-Job-Application.git
cd Automating-Job-Application       

# Install the required package
pip install selenium
```
  - **Setup Web-Driver:**
      - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and ensure it's in your system's PATH.
        
  - **Configuration:**
      - Set your LinkedIn credentials and other personal information:
          - Edit the script linkedin_job_application_bot.py and replace the placeholders for your email, password, and phone number with your actual values.
        ```shell
        email_phone.send_keys("your email")
        password.send_keys("your password")
        enter_phone_num.send_keys("your number")
        ```

   - **Documentation:**
     - Selenium: https://www.selenium.dev/documentation/
    
## 📄 Code Explanation
   - When you execute the code will execute the following:
       - Open LinkedIn and navigate to the specified job posting.
       - Sign in using the provided credentials.
       - Fill in the necessary details for the job application.
       - Submit the application.

## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Automating job application project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Automating job application project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
