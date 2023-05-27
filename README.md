# JobScout
JobScout is an intelligent job search assistant that keeps you updated with the latest opportunities. By leveraging web scraping techniques, it scours LinkedIn for job listings, extracting key details like titles, companies, locations, and descriptions. The data is stored in a structured format, making it easy to browse and search.

Hey, I found something interesting! If you're looking for up-to-date job opportunities, here's a brief overview of how LinkedIn job scraping and architecture can help you stay informed:

LinkedIn is a renowned professional networking platform that connects millions of users with various job openings. However, LinkedIn does not provide a public API for job data. Don't worry, though! We can still extract valuable job information by utilizing web scraping techniques.

To scrape job data from LinkedIn, we can leverage libraries like BeautifulSoup or Scrapy in Python. By sending HTTP requests and parsing the HTML content, we can extract essential details such as job titles, companies, locations, and descriptions.

Once we have the scraped job data, we can structure and store it in JSON format. JSON is a lightweight and easily readable data interchange format. Each job listing can be represented as a JSON object, and an array within a JSON file can store multiple job objects.

To persist the scraped job data, we can utilize an SQLite3 database. SQLite is a lightweight, file-based relational database system that eliminates the need for a separate server process. By parsing the JSON data, we can insert it into appropriate tables within the database. Each job listing can be stored as a row in a table, with columns representing attributes like title, company, location, and description.

Now, let's ensure you receive the latest job openings directly to your phone. We can achieve this by utilizing the Twilio API, which provides programmable messaging capabilities. By setting up a script to run at regular intervals, like every 24 hours, we can retrieve the most recent job data from the SQLite database. The script can format the relevant job information and send it to your designated phone number using the Twilio API's messaging service.

In summary, LinkedIn job scraping and architecture allow you to stay updated on current job opportunities. By scraping job data, storing it in JSON format within an SQLite3 database, and utilizing the Twilio API, you can receive daily notifications of the latest openings. Stay ahead in your job search with this automated and efficient system!



![Screenshot_2023-05-27-22-09-08-560_com google android apps messaging](https://github.com/piyush8884/JobScout/assets/64435441/6c947fe9-a4ce-43fa-9c98-a1e6a2d2bc50)
![Screenshot (35)](https://github.com/piyush8884/JobScout/assets/64435441/d6e5135c-e907-4ce7-a0c0-4ba059b5dbf7)
![Screenshot (36)](https://github.com/piyush8884/JobScout/assets/64435441/152b6cc2-d90f-4f28-a4ce-47499517f634)
