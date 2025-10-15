**BillStation Login/Logout Automation**

This script automates the login and logout flow on the [BillStation staging site](https://app.staging.thebillstation.com) using Selenium WebDriver in Python.

* Logs into the app using test credentials
* Verifies dashboard and wallet balance
* Logs out of the application
* Runs in headless Chrome by default

**Setup & Run**

1. Clone the repo

git clone https://github.com/bolaji1998/BillStation.git
cd BillStation


2. Install dependencies

pip install selenium webdriver-manager

3. Run the test

python BillStation.py


To see the browser, comment out the headless line in the script.

* Only tested on the staging environment
* Uses webdriver-manager to auto-install ChromeDriver
* Ensure Chrome is installed on your machine
