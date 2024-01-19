# Fibonacci API Project
## Overview
The Fibonacci API is a sophisticated backend service designed to calculate the n-th Fibonacci number for a given input. This project demonstrates the effective integration of modern software development tools and practices to create a high-performance, scalable, and secure API.

## Technologies Used
- **Python & Django REST Framework:** Core programming language and framework for building the API.<br />

- **Docker:** Utilized for containerization, ensuring consistent environments across different stages of development and deployment.<br />

- **uWSGI:** Serves as an application server interface, enhancing the communication between our web server and Django application.<br />

- **Nginx:** Used as a reverse proxy to provide load balancing, which improves the efficiency and security of the application.<br />

- **AWS EC2:** Hosts the application, providing a scalable and reliable infrastructure.<br />

- **Redis Cache:** Employs caching to optimize the performance of Fibonacci number calculations.<br />

- **GitHub Actions:** Automates CI/CD pipelines, streamlining the development process.<br />

- **Swagger:** Offers clear and interactive API documentation for easy understanding and usage.<br />

- **Flake8:** Ensures adherence to coding standards and improves code quality.<br />

## Software Design Principles and Patterns
The project is built with a focus on the SOLID principles, ensuring a modular, maintainable, and scalable codebase. Each component is designed to have a single responsibility and is easily interchangeable, providing flexibility and ease of future enhancements.

- **Single Responsibility Principle:** Each class should have only one responsibility and that responsibility should be entirely encapsulated by the class.<br />
  - Fibonacci Class is solely responsible for calculating Fibonacci numbers.
  - RedisCache Class exclusively manages cache operations related to Redis.
  - CacheFactory Class is solely responsible for getting proper type of Cache.
  - OperationFactory Class only responsible for getting proper type of operation.<br /><br />
- **Open/Closed Principle:** Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.<br />
  - The OperationFactory and CacheFactory classes can be extended to accommodate new types of operations or caches without altering existing code.<br /><br />
- **Dependency Inversion Principle:** High-level modules should not depend on low-level modules; both should depend on abstractions.<br />
  - The CachedOperations class depends on the CacheInterface for interacting with the RedisCache, thus relying on an abstraction rather than a concrete class.<br /><br />
- **Factory Pattern:** The Factory Pattern is a design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
  - OperationFactory and CacheFactory classes are examples of the Factory Pattern, used to create instances of different types of operations (e.g., Fibonacci) and caches (e.g., RedisCache). This pattern simplifies object creation and promotes loose coupling by allowing the creation of objects without specifying the exact class of object that will be created.

## Testing
Comprehensive testing strategies were employed, including both unit and integration tests, to ensure the reliability and functionality of the API. This approach guarantees that all aspects of the application perform as expected under various scenarios.

## Error Handling
The API is designed to handle errors effectively, ensuring a robust and user-friendly experience. Key aspects of our error handling include:
- Input Validation: The API accepts input values for n that are integers between 1 and 99,999.
- Error Responses: If a request is made with a value outside this range, the API responds with a HTTP 400 Bad Request status code, along with a descriptive error message.
  
## ⚙️ Build and Run instructions
This project is containerized using Docker, simplifying the build and run process. Follow the steps below to get the project up and running on your local machine.
### Prerequisites
Docker and Docker Compose installed on your system.
### Building the Project
- Clone the repository to your local machine.
- Navigate to the root directory of the project.
- Run the following command to build the Docker containers:<br />
`docker-compose build`
### Running the Project
Once the build process is complete, you can start the project using the following command:<br />
`docker-compose up`<br />
This command starts all the necessary services defined in the docker-compose.yml file.
### Accessing the API
After starting the services, the API will be accessible at **http://127.0.0.1:8000/api/calc-fib/**. You can test it by appending ?n=<number> to calculate the n-th Fibonacci number. For example:<br />
`http://127.0.0.1:8000/api/calc-fib/?n=15`
### Running Tests
To run the automated tests for this project, use the following command:<br />
`docker-compose run --rm app sh -c "python3 manage.py test"`
### Accessing the Deployed API
The API is also deployed and can be accessed at the following URL:<br />
`http://ec2-54-221-189-178.compute-1.amazonaws.com/api/calc-fib/?n=23` <br />
Replace 23 with any integer to compute the corresponding Fibonacci number.

## API Documentation with Swagger
This project includes API documentation using Swagger, a powerful tool for designing, documenting, and consuming RESTful web services.
### Accessing the Documentation
To view the API documentation, simply navigate to the following URL after starting the project: <br />
`http://127.0.0.1:8000/api/docs/` <br />
or if you are using deployed API:<br />
`http://ec2-54-221-189-178.compute-1.amazonaws.com/api/docs/`
### Using Swagger Documentation
The Swagger UI provides a clear and interactive way to explore the API's endpoints. It allows you to: <br />

- View detailed information about each endpoint, including HTTP method, request parameters, response models, and more.
- Try out the API directly from the browser by sending requests to the various endpoints and viewing the responses.
- See the correct syntax for calling each endpoint, which can be helpful for integrating the API into your own projects.
